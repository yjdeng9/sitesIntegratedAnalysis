
mkdir STAR_index && cd STAR_index
STAR --runMode genomeGenerate --genomeDir STAR_index_139/ \
--genomeFastaFiles hg19.fa \
--sjdbGTFfile gencode.v31lift37.annotation.gtf \
--sjdbOverhang 139

STAR --runThreadN 20 \
--genomeDir /data/dengyongjie/pipelinebase/m6apepi/processed/ref/STAR_index_139/ \
--readFilesIn ../qc_result/ctrl-DF1_FRIP190312488-1a_1.fastq ../qc_result/ctrl-DF1_FRIP190312488-1a_2.fastq \
--outSAMtype BAM SortedByCoordinate \
--outFileNamePrefix ctrl-DF1

