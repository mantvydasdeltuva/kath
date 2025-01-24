import os
import sys
import pandas as pd
from pathlib import Path
import urllib.request
import zipfile
from pathlib import Path
import sqlite3
import csv

sys.path.append(str(Path(__file__).parent.parent.parent))

from utils.progress import printProgressBar
from utils.log_config import get_logger

logger = get_logger(__name__)

def download_progress_hook(count, block_size, total_size):
    """Download progress callback for urlretrieve"""
    printProgressBar(count * block_size, total_size, 
                    prefix='Progress:', 
                    suffix='Complete', 
                    length=50)


class revel_initiator:
    """
    Initiates the REVEL data and database for the first time.
    Also validates the existence of REVEL data and database.
    """
    
    @staticmethod
    def install_revel():
        """Install REVEL data using Python."""
        # Setup paths
        base_dir = Path(__file__).parent
        data_dir = base_dir / 'data'
        zip_path = data_dir / 'revel-v1.3_all_chromosomes.zip'
        
        # Create directories
        data_dir.mkdir(parents=True, exist_ok=True)
        
        # Download file with progress bar
        url = 'https://rothsj06.dmz.hpc.mssm.edu/revel-v1.3_all_chromosomes.zip'
        try:
            print("Downloading REVEL data...")
            urllib.request.urlretrieve(url, zip_path, download_progress_hook)
            print()  # New line after progress bar
        except Exception as e:
            print(f"Failed to download REVEL file: {e}")
            return False

        # Extract files with progress bar
        try:
            print("Extracting files...")
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                # Get total files for progress
                file_list = zip_ref.namelist()
                total_files = len(file_list)
                
                # Extract with progress
                for i, file in enumerate(file_list, 1):
                    zip_ref.extract(file, data_dir)
                    printProgressBar(i, total_files, 
                                prefix='Extracting:', 
                                suffix='Complete', 
                                length=50)
        except Exception as e:
            print(f"Failed to extract files: {e}")
            return False
        
        # Cleanup
        try:
            os.remove(zip_path)
        except Exception as e:
            print(f"Failed to cleanup: {e}")
        
        print("REVEL installation completed successfully")
        return True
    
    
    @staticmethod
    def prepare_revel_database(revel_file):
        """Convert all rows of REVEL CSV (6GB) into a SQLite database, skipping invalid grch38_pos."""
        db_path = revel_file + '.db'
        
        if os.path.exists(db_path):
            print(f"REVEL database already exists at {db_path}")
            return db_path

        conn = sqlite3.connect(db_path)
        conn.execute('PRAGMA journal_mode=WAL')
        conn.execute('PRAGMA synchronous=NORMAL')

        conn.execute('''
            CREATE TABLE IF NOT EXISTS revel (
                chr TEXT,
                grch38_pos INTEGER,
                ref TEXT,
                alt TEXT,
                REVEL REAL,
                PRIMARY KEY (chr, grch38_pos, ref, alt)
            )
        ''')

        total_rows = sum(1 for _ in open(revel_file)) - 1
        chunk_size = 100_000
        processed = 0
        print(f"Found {total_rows:,} rows. Beginning conversion...")

        with open(revel_file) as f:
            reader = csv.DictReader(f)

            while True:
                chunk = []
                for _ in range(chunk_size):
                    try:
                        row = next(reader)
                    except StopIteration:
                        break
                    
                    try:
                        # Skip rows where grch38_pos is '.'
                        if row['grch38_pos'] == '.':
                            continue

                        chunk.append((
                            row['chr'],
                            int(row['grch38_pos']),
                            row['ref'],
                            row['alt'],
                            float(row['REVEL'])
                        ))

                        if not chunk:
                            break

                        conn.executemany('INSERT OR IGNORE INTO revel VALUES (?,?,?,?,?)', chunk)
                        processed += len(chunk)
                        printProgressBar(processed, total_rows, 
                                prefix='Progress:', 
                                suffix=f'Complete ({processed:,}/{total_rows:,} rows)', 
                                length=50)
                        
                    except Exception as e:
                        print(f"Error in processing row (Possibly not supporting \"X,Y ... \" chromosome types): {e}")
                    
                conn.commit()

        print("Creating indexes...")
        conn.execute('CREATE INDEX idx_pos ON revel(grch38_pos)')
        conn.execute('CREATE INDEX idx_chr_pos ON revel(chr, grch38_pos)')

        conn.close()
        print(f"Conversion complete. Database at {db_path}")
        return db_path
    
    
    @staticmethod
    def validate_revel_data(revel_file_path):
        
        if os.path.exists(revel_file_path):
            print(f"REVEL data already exists at {revel_file_path}")
            return True
        else:
            print(f"REVEL data does not exist at {revel_file_path}")
            return False
    
    
    @staticmethod
    def validate_revel_db(revel_db_file):
        if os.path.exists(revel_db_file):
            print(f"REVEL DB already exists at {revel_db_file}")
            return True
        else:
            print(f"REVEL DB does not exist at {revel_db_file}")
            return False
        

def assign_revel_scores(input_gene_data: pd.DataFrame, revel_db_file: str) -> pd.DataFrame:
    """
    Assigns REVEL scores with progress tracking and optimized processing.
    
    Args:
        input_gene_data: DataFrame with hg38_gnomad_format column
        revel_db_file: Path to REVEL SQLite database
        
    Returns:
        DataFrame with added REVEL scores
    """
    total_rows = input_gene_data.shape[0]
    logger.info(f"Starting REVEL score assignment for {total_rows} variants")
    
    for i in range(total_rows):
        hg38_gnomad_format = input_gene_data.loc[i, 'hg38_gnomad_format']
        
        if pd.isna(hg38_gnomad_format):
            input_gene_data.loc[i, 'REVEL'] = pd.NA
            continue
            
        try:
            chromosome, position, ref, alt = hg38_gnomad_format.split('-')
            revel_score = get_single_revel_score(chromosome, position, ref, alt, revel_db_file)
            input_gene_data.loc[i, 'REVEL'] = revel_score
            
            printProgressBar(
                i + 1, 
                total_rows,
                prefix='Assigning REVEL scores:',
                suffix=f'Complete ({i+1}/{total_rows})',
                length=50
            )
            
        except ValueError as ve:
            input_gene_data.loc[i, 'REVEL'] = pd.NA
            logger.error(f"Format error in variant {hg38_gnomad_format}: {ve}")
            
        except Exception as e:
            input_gene_data.loc[i, 'REVEL'] = pd.NA
            logger.error(f"Failed to get REVEL score for {hg38_gnomad_format}: {e}")
    
    logger.info("REVEL score assignment complete")
    return input_gene_data
    

def get_single_revel_score(chromosome, grch38_position, ref, alt, revel_db_file):


    conn = sqlite3.connect(revel_db_file)
    cursor = conn.cursor()
    
    query = '''
    SELECT chr, grch38_pos, ref, alt, REVEL
    FROM revel
    WHERE chr = ? AND grch38_pos = ? AND ref = ? AND alt = ?
    '''
    
    params = [chromosome, grch38_position, ref, alt]
    
    cursor.execute(query, params)
    
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return row[4]
    else:
        return pd.NA
    

def main_revel_pipeline(input_gene_dataset=None, data_store_dir=None):
    
    revel_filename = 'revel_with_transcript_ids'
    revel_db_filename = revel_filename + '.db'
    
    if data_store_dir:
        current_script_dir = data_store_dir
    else:
        print("Data store directory not provided. Using default folder.")
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
    
    if not input_gene_dataset:
        print("Input gene dataset not provided. Setting to default.")
        input_gene_dataset = os.path.join(current_script_dir, 'data', 'lovd_gnomad.csv')
        
    revel_data_file = os.path.join(current_script_dir, 'data', revel_filename)
    revel_db_file = os.path.join(current_script_dir, 'data', revel_db_filename)
    
    initializer = revel_initiator()
    
    # Validate REVEL data and database
    revel_data_exists = initializer.validate_revel_data(revel_data_file)
    revel_db_exists = initializer.validate_revel_db(revel_db_file)
    
    if not revel_data_exists:
        initializer.install_revel()
    
    if not revel_db_exists:
        initializer.prepare_revel_database(revel_data_file)
        
        
    # Read the input gene data
    try:
        input_gene_data = pd.read_csv(input_gene_dataset)
        
        # Assign REVEL scores
        print("Assigning REVEL scores... \n Errors will be logged.")
        input_gene_data = assign_revel_scores(input_gene_data, revel_db_file)
        
        return input_gene_data
        
    except FileNotFoundError:
        print(f"File not found: {input_gene_dataset}")
        yield FileNotFoundError
    
    except pd.errors.EmptyDataError:
        print(f"Empty file: {input_gene_dataset}")
        yield pd.errors.EmptyDataError

if __name__ == '__main__':
    main_revel_pipeline()
    
