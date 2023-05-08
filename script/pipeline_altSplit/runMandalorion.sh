source ~/.bashrc
main_path='/data/dengyongjie/altSplicing/datas'

python justAlignReads.py $main_path'/fastqData' $main_path'/ensemblData/Homo_sapiens.GRCh38.dna.primary_assembly.fa' $main_path'/mandalorionData'

python spliceSites.py $main_path'/mandalorionData/content_file' $main_path'/mandalorionData' 0.02 $main_path'/ensemblData/Homo_sapiens.GRCh38.86.chr.gtf' g

python defineAndQuantifyIsoforms.py $main_path'/mandalorionData/content_file' $main_path'/mandalorionData' 20 20