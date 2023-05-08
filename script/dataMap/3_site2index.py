import os
import shutil


def main(site_file, out_path):
    with open(site_file, 'r') as sr:
        forward_exon_line = sr.readline()
        forward_exon_list = forward_exon_line.strip().split('\t')
        reverse_exon_line = sr.readline()
        reverse_exon_list = reverse_exon_line.strip().split('\t')

        left_ss_list = sr.readline().strip().split('\t')
        right_ss_list = sr.readline().strip().split('\t')

        m6a_list = sr.readline().strip().split('\t')
        um6a_list = sr.readline().strip().split('\t')
        re_m6a_list = sr.readline().strip().split('\t')
        re_um6a_list = sr.readline().strip().split('\t')

        left_ss_set = set(list(map(int, left_ss_list)))
        right_ss_set = set(list(map(int, right_ss_list)))
        m6a_set = set(list(map(int, m6a_list)))
        um6a_set = set(list(map(int, um6a_list)))
        re_m6a_set = set(list(map(int, re_m6a_list)))
        re_um6a_set = set(list(map(int, re_um6a_list)))
    print('Notes: load datas!')

    forward_exons = list(map(int, forward_exon_list))
    forward_exons.sort()
    reverse_exons = list(map(int, reverse_exon_list))
    reverse_exons.sort()
    print('Notes: sorted exons!')

    left_indexes = []
    right_indexes = []
    m6a_indexes = []
    um6a_indexes = []
    forward_index = 0
    for forward_site in forward_exons:
        forward_index += 1
        if forward_site in left_ss_set:
            left_indexes.append(forward_index)
        if forward_site in right_ss_set:
            right_indexes.append(forward_index)
        if forward_site in m6a_set:
            m6a_indexes.append(forward_index)
        if forward_site in um6a_set:
            um6a_indexes.append(forward_index)

    re_left_indexes = []
    re_right_indexes = []
    re_m6a_indexes = []
    re_um6a_indexes = []
    reverse_index = 0
    for reverse_site in reverse_exons:
        reverse_index += 1
        if reverse_site in left_ss_set:
            re_left_indexes.append(reverse_index)
        if reverse_site in right_ss_set:
            re_right_indexes.append(reverse_index)
        if reverse_site in re_m6a_set:
            re_m6a_indexes.append(reverse_index)
        if reverse_site in re_um6a_set:
            re_um6a_indexes.append(reverse_index)

    out_name = os.path.basename(site_file).replace('.site', '.index')
    out_file = os.path.join(out_path, out_name)
    with open(out_file, 'w') as iw:
        iw.write(list2line(right_indexes)+'\n')
        iw.write(list2line(left_indexes) + '\n')
        iw.write(list2line(m6a_indexes) + '\n')
        iw.write(list2line(um6a_indexes) + '\n')
        print('Notes: Success in writing forward indexes!')

        iw.write(list2line(re_right_indexes) + '\n')
        iw.write(list2line(re_left_indexes) + '\n')
        iw.write(list2line(re_m6a_indexes) + '\n')
        iw.write(list2line(re_um6a_indexes) + '\n')
        print('Notes: Success in writing reverse indexes!')


def list2line(a_list):
    a_line = ''
    a_list.sort()
    for data in a_list:
        a_line += str(data)
        a_line += '\t'
    return a_line


if __name__ == '__main__':
    # sites_path = '/data/dengyongjie/altSplicing/datas/mapData/site'
    # out_path = '/data/dengyongjie/altSplicing/datas/mapData/index'

    import sys
    sites_path = sys.argv[1]
    out_path = sys.argv[2]

    if os.path.exists(out_path):
        shutil.rmtree(out_path)
    os.makedirs(out_path)

    for file in os.listdir(sites_path):
        if '.site' not in file:
            continue
        file_path = os.path.join(sites_path, file)
        count = 0
        for index, line in enumerate(open(file_path, 'r')):
            count += 1
        if count < 8:
            continue
        print('> chromosome'+file.replace('.site', ''))
        main(file_path, out_path)
