
old_fasta = '/data/dengyongjie/altSplicing/datas/ensemblData/Homo_sapiens.GRCh38.dna.primary_assembly.fa'
new_fasta = '/data/dengyongjie/altSplicing/datas/mapData/Homo_sapiens.GRCh38.new.fa'

with open(old_fasta) as f:
    fw = open(new_fasta, 'w')
    line = f.read()
    line = line.replace('\n', '').replace('>', '\n>').replace('REF', 'REF_')
    for aa in line:
        fw.write(aa)
    fw.close()
