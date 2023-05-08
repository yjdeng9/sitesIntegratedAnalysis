#!/bin/bash

config = $1
echo $config
# fastq-dump --gzip --split-3 -A ./SRA/${config}.sra -O ./fastq/
# fastqc -t 8 -o ./fastqc_out/ -f fastq SRR*.fastq.gz