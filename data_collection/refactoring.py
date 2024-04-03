import os

from .constants import LOVD_TABLES_DATA_TYPES

import pandas as pd
from pandas import DataFrame


def convert_lovd_to_datatype(df_dict):
    """
    Convert data from LOVD format table to desired data format based on specified data types.

    :param dict[str, tuple[DataFrame, list[str]] df_dict: Dictionary of LOVD tables saved as ``DataFrame``
    """
    # TODO: rewrite to cast using only `astype`, remove second loop, optimize int usage
    for table_name in df_dict:
        frame, notes = df_dict[table_name]
        for column in frame.columns:
            if column not in LOVD_TABLES_DATA_TYPES[table_name]:
                raise ValueError(f"Column {column} is undefined in LOVD_TABLES_DATA_TYPES")

            match LOVD_TABLES_DATA_TYPES[table_name][column]:
                case "Date":
                    frame[column] = pd.to_datetime(frame[column])
                case "Boolean":
                    frame[column] = (frame[column] != 0).astype('bool')
                case "String":
                    frame[column] = frame[column].astype('string')
                case "Integer64":
                    frame[column] = pd.to_numeric(frame[column]).astype('Int64')
                case "Double":
                    frame[column] = pd.to_numeric(frame[column]).astype('float')
                case _:
                    raise ValueError("Undefined data type")


def parse_lovd(path):
    """
    Converts data from text file with LOVD format to dictionary of tables.

    Key is name of table, value is tuple, where first element is data saved as
    pandas DataFrame and second element is list of notes provided for table.

    **IMPORTANT:** It doesn't provide types for data inside. Use ``convert_lovd_to_datatype`` for this.

    :param str path: path to text file
    :returns: dictionary of tables
    :rtype: dict[str, tuple[DataFrame, list[str]]]
    """

    # TODO: remove notes from dict, they should be logged using `logging` module
    # Check if the file exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file at {path} does not exist.")

    d = {}

    with open(path, encoding="UTF-8") as f:
        # skip header
        [f.readline() for _ in range(4)]  # pylint: disable=expression-not-assigned

        while True:
            line = f.readline()

            if line == '':
                break

            table_name = line.split("##")[1].strip()

            notes = []
            line = f.readline()
            while line.startswith("##"):
                notes.append(line[2:-1])
                line = f.readline()

            table_header = [column[3:-3] for column in line[:-1].split('\t')]
            frame = DataFrame([], columns=table_header)
            line = f.readline()
            while line != '\n':
                variables = [variable[1:-1] for variable in line[:-1].split('\t')]
                observation = DataFrame([variables], columns=table_header)
                frame = pd.concat([frame, observation], ignore_index=True)
                line = f.readline()

            d[table_name] = (frame, notes)

            # skip inter tables lines
            [f.readline() for _ in range(1)]  # pylint: disable=expression-not-assigned

    return d


def from_clinvar_name_to_cdna_position(name):
    """
    Custom cleaner to extract cDNA position from Clinvar `name` variable.

    :param str name:
    :returns: extracted cDNA
    :rtype: str
    """

    start = name.find(":") + 1
    ends = {'del', 'delins', 'dup', 'ins', 'inv', 'subst'}

    if "p." in name:
        name = name[:name.index("p.") - 1].strip()

    end = len(name)

    for i in ends:
        if i in name:
            end = name.index(i) + len(i)
            break

    return name[start:end]
