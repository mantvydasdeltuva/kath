FROM python:3.12-slim

# Set app files directory
ARG APP_DIR="/kath/back_end"

# Install required packages and delete cached data
RUN apt-get update && \
    apt-get install curl gzip unzip redis-server -y --no-install-recommends  && \
    rm -rf /var/lib/apt/lists/*

# Copy backend files to the image and install required python packages globally so replacing the backend directory via mounting doesn't hide them later.
WORKDIR ${APP_DIR}
COPY . .
RUN MAKEFLAGS="-j$(nproc)" pip install --no-cache-dir --break-system-packages --root-user-action ignore -r ./requirements.txt

# Downloading and extracting hg38.fa.gz file needed for SpliceAI
WORKDIR ${APP_DIR}/src/workspace/fasta/
RUN curl -O https://hgdownload.cse.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz && gunzip hg38.fa.gz

# Downloading hg19ToHg38.over.chain.gz file needed for pyliftover into it's cache directory
WORKDIR /root/.pyliftover/
RUN curl -O http://hgdownload2.cse.ucsc.edu/goldenPath/hg19/liftOver/hg19ToHg38.over.chain.gz

# Downloading and extracting revel-v1.3_all_chromosomes.zip file needed for REVEL
WORKDIR ${APP_DIR}/src/workspace/revel
RUN curl -O https://rothsj06.dmz.hpc.mssm.edu/revel-v1.3_all_chromosomes.zip && unzip revel-v1.3_all_chromosomes.zip
WORKDIR ${APP_DIR}/src/
RUN python3 scripts/revel.py workspace/revel/revel_with_transcript_ids workspace/revel/revel_with_transcript_ids.db

# Start redis and flask
WORKDIR ${APP_DIR}
ENTRYPOINT []
CMD redis-server --daemonize yes && gunicorn -c gunicorn_config.py run:app
