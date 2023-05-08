import os
import shutil


def add_line(out_path):
    for file in os.listdir(out_path):
        if '.tmp' not in file:
            continue
        with open(os.path.join(out_path,file), 'a') as fa:
            fa.write('\n')


def genome_io(fasta_file, out_path):
    with open(fasta_file, 'r') as fr:
        name = 'zero'
        fw = open(os.path.join(out_path, name + '.tmp'),'w')

        for line in fr:
            if line.startswith('>'):
                fw.close()
                print('Success: get chromosome %s seq!' % name)
                name = line.strip().replace('>', '').split(' ')[0]
                fw = open(os.path.join(out_path, name + '.tmp'),'w')
            else:
                fw.write(line.strip())
        fw.close()
        print('Success: get chromosome %s seq!' % name)
        os.remove(os.path.join(out_path, 'zero.tmp'))
    add_line(out_path)


def gtf_io(gtf_file, out_path):
    with open(gtf_file, 'r') as gr:
        for line in gr:
            if line.startswith('#'):
                continue

            sl = line.strip().split('\t')
            if not sl[2] == 'exon':
                continue

            chromosome = sl[0]
            start = sl[3]
            end = sl[4]
            direction = sl[6]

            out_file = os.path.join(out_path, chromosome + '.tmp')
            if not os.path.exists(out_file):
                print('Notes: chromosome %s has not seq!' % chromosome)
                continue
            with open(out_file, 'a') as ga:
                ga.write(start+':'+end+':'+direction+'\t')
    add_line(out_path)
    print('Success: get gtf data!')


def iso_io(iso_file, out_path):
    left_dict = {}
    right_dict = {}

    with open(iso_file, 'r') as ir:
        for line in ir:
            sl = line.strip().split('\t')
            notes = sl[2].split('_')

            chromosome = notes[0]
            left = int(notes[2])
            right = int(notes[3])

            if chromosome in left_dict.keys():
                left_dict[chromosome].add(left)
            else:
                left_dict[chromosome] = set()
                left_dict[chromosome].add(left)

            if chromosome in right_dict.keys():
                right_dict[chromosome].add(right)
            else:
                right_dict[chromosome] = set()
                right_dict[chromosome].add(right)
        ir.close()

    for chromosome in left_dict.keys():
        out_file = os.path.join(out_path, chromosome + '.tmp')
        if not os.path.exists(out_file):
            print('Notes: chromosome %s has not seq!' % chromosome)
            continue
        with open(out_file, 'a') as ia:
            for data in left_dict[chromosome]:
                ia.write(str(data)+'\t')
            ia.write('\n')

        with open(out_file, 'a') as ia:
            for data in right_dict[chromosome]:
                ia.write(str(data)+'\t')
            ia.write('\n')

    print('Success: get isoform data!')


def ss_io(ss_bed, out_path):
    left_dict = {}
    right_dict = {}

    with open(ss_bed, 'r') as ir:
        for line in ir:
            sl = line.strip().split('\t')

            chromosome = sl[0]
            left = int(sl[1])
            right = int(sl[2])

            if chromosome in left_dict.keys():
                left_dict[chromosome].add(left)
            else:
                left_dict[chromosome] = set()
                left_dict[chromosome].add(left)

            if chromosome in right_dict.keys():
                right_dict[chromosome].add(right)
            else:
                right_dict[chromosome] = set()
                right_dict[chromosome].add(right)
        ir.close()

    for chromosome in left_dict.keys():
        out_file = os.path.join(out_path, chromosome + '.tmp')
        if not os.path.exists(out_file):
            print('Notes: chromosome %s has not seq!' % chromosome)
            continue
        with open(out_file, 'a') as ia:
            for data in left_dict[chromosome]:
                ia.write(str(data)+'\t')
            ia.write('\n')

        with open(out_file, 'a') as ia:
            for data in right_dict[chromosome]:
                ia.write(str(data)+'\t')
            ia.write('\n')

    print('Success: get splice sites data!')


def site_io(site_file, out_path):
    with open(site_file, 'r') as sr:
        for line in sr:
            sl = line.strip().split('\t')

            chromosome = sl[0]

            direction = sl[5]
            position = int(sl[1])

            out_file = os.path.join(out_path, chromosome + '.tmp')
            if not os.path.exists(out_file):
                print('Notes: chromosome %s has not seq!' % chromosome)
                continue
            with open(out_file, 'a') as sa:
                sa.write(str(position)+':'+direction + '\t')
    add_line(out_path)
    print('Success: get m6A data!')


def main():
    # genome_fasta = '/data/dengyongjie/altSplicing/datas/ensemblData/Homo_sapiens.GRCh38.dna.primary_assembly.fa'
    # genome_gtf = '/data/dengyongjie/altSplicing/datas/ensemblData/Homo_sapiens.GRCh38.86.chr.gtf'
    # isoform_list = '/data/dengyongjie/altSplicing/datas/mandalorionData/isoform_list'
    # ss_list = '/data/dengyongjie/altSplicing/datas/mandalorionData/SS.bed'
    # m6a_site = '/data/dengyongjie/altSplicing/datas/matkData/m6A_sites.bed'

    # tmp_path = '/data/dengyongjie/altSplicing/datas/mapData/tmp'
    import sys
    import pandas as pd
    config = sys.argv[1]
    if config == 'total.distance':
        return 0
    else:
        config_df = pd.read_csv(config, sep='\t', header=None)

    genome_fasta = config_df.loc['genome_fasta',0]
    genome_gtf = config_df.loc['genome_gtf',0]
    isoform_list = config_df.loc['isoform_list', 0]
    ss_list = config_df.loc['ss_list', 0]
    m6a_site = config_df.loc['m6a_site', 0]
    tmp_path = config_df.loc['tmp_path', 0]

    if os.path.exists(tmp_path):
        shutil.rmtree(tmp_path)
    os.makedirs(tmp_path)

    genome_io(genome_fasta, tmp_path)
    gtf_io(genome_gtf, tmp_path)
    iso_io(isoform_list, tmp_path)
    ss_io(ss_list, tmp_path)
    site_io(m6a_site, tmp_path)


if __name__ == '__main__':
    main()

