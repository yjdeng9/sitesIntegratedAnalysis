import os


def open_tmp_files(tmp_path):
    for file in os.listdir(tmp_path):
        if '.tmp' not in file:
            continue
        with open(os.path.join(tmp_path, file), 'r') as fr:
            chromosome = file.replace('.tmp','')
            line = fr.readline()
            line = line.strip()
            seq_dict[chromosome] = line


def site_io(site_file):
    with open(site_file, 'r') as sr:
        for line in sr:
            sl = line.strip().split('\t')

            chromosome = sl[0]

            if sl[5] is '+':
                position = int(sl[1])
            else:
                position = int(sl[1])

            if chromosome not in seq_dict.keys():
                print('Notes: chromosome %s has not seq!' % chromosome)
                continue

            base = seq_dict[chromosome][position]
            if base is not 'A':
                print(line.strip())
                print(seq_dict[chromosome][position])


if __name__ == '__main__':
    tmp_file_path = '/data/dengyongjie/altSplicing/datas/mapData/tmp/'
    m6a_site = '/data/dengyongjie/altSplicing/datas/matkData/m6A_sites.bed'

    seq_dict = {}
    open_tmp_files(tmp_file_path)
    site_io(m6a_site)
