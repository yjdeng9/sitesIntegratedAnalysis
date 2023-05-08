import os
import numpy as np
import shutil


def load_file(index_file):
    with open(index_file, 'r') as ir:
        left_ss_list = ir.readline().strip().split('\t')
        right_ss_list = ir.readline().strip().split('\t')
        m6a_list = ir.readline().strip().split('\t')
        um6a_list = ir.readline().strip().split('\t')

        re_left_ss_list = ir.readline().strip().split('\t')
        re_right_ss_list = ir.readline().strip().split('\t')
        re_m6a_list = ir.readline().strip().split('\t')
        re_um6a_list = ir.readline().strip().split('\t')
    print('Notes: get datas!')

    left_m6a_dis_list, left_um6a_dis_list = statistics(left_ss_list, m6a_list, um6a_list,
                                                       re_left_ss_list, re_m6a_list, re_um6a_list)
    right_m6a_dis_list, right_um6a_dis_list = statistics(right_ss_list, m6a_list, um6a_list,
                                                         re_right_ss_list, re_m6a_list, re_um6a_list)

    return left_m6a_dis_list, left_um6a_dis_list, right_m6a_dis_list, right_um6a_dis_list


def statistics(splice_sites, m6a_sites, um6a_sites, re_splice_sites, re_m6a_sites, re_um6a_sites):
    wing = 2000
    m6a_distance_list = []
    um6a_distance_list = []

    print('splice sites num: %d' % (len(splice_sites)+len(re_splice_sites)))

    for splice_site in splice_sites:
        if splice_site == '':
            continue
        int_ss = int(splice_site)
        m6a_list = list(map(int, m6a_sites))
        um6a_list = list(map(int, um6a_sites))

        tmp_m6a_dis = np.array(m6a_list) - int_ss
        tmp_um6a_dis = np.array(um6a_list) - int_ss

        for tmp_distance in tmp_m6a_dis:
            if -wing <= tmp_distance <= wing:
                m6a_distance_list.append(tmp_distance)

        for tmp_distance in tmp_um6a_dis:
            if -wing <= tmp_distance <= wing:
                um6a_distance_list.append(tmp_distance)

    for re_splice_site in re_splice_sites:
        if re_splice_site == '':
            continue
        int_re_ss = int(re_splice_site)
        re_m6a_list = list(map(int, re_m6a_sites))
        re_um6a_list = list(map(int, re_um6a_sites))

        tmp_m6a_dis = np.array(re_m6a_list) - int_re_ss
        tmp_um6a_dis = np.array(re_um6a_list) - int_re_ss

        for tmp_distance in tmp_m6a_dis:
            if -wing <= tmp_distance <= wing:
                m6a_distance_list.append(tmp_distance)

        for tmp_distance in tmp_um6a_dis:
            if -wing <= tmp_distance <= wing:
                um6a_distance_list.append(tmp_distance)

    print(len(m6a_distance_list))
    print(len(um6a_distance_list))
    return m6a_distance_list, um6a_distance_list


def load_path(index_path, out_path):
    # left_m6a_dis_list = []
    # left_um6a_dis_list = []
    # right_m6a_dis_list = []
    # right_um6a_dis_list = []

    for file in os.listdir(index_path):
        if '.index' not in file:
            continue
        file_path = os.path.join(indexes_path, file)

        base_name = file.replace('.index','')
        if base_name in ['X', '10', '11', '19', '6', '4', '7','8', '15', '14', '17', '3', '20', '9', '22']:
            continue
        print('> chromosome' + file.replace('.index', ''))

        count = 0
        for index, line in enumerate(open(file_path, 'r')):
            count += 1
        print(count)

        left_m6a_distances, left_um6a_distances, right_m6a_distances, right_um6a_distances = load_file(file_path)
        # left_m6a_dis_list.extend(left_m6a_distances)
        # left_um6a_dis_list.extend(left_um6a_distances)
        # right_m6a_dis_list.extend(right_m6a_distances)
        # right_um6a_dis_list.extend(right_um6a_distances)

        with open(os.path.join(out_path, 'tmp_m6a_left.distance'), 'a') as da:
            da.write(list2line(left_m6a_distances))
        with open(os.path.join(out_path, 'tmp_um6a_left.distance'), 'a') as da:
            da.write(list2line(left_um6a_distances))
        with open(os.path.join(out_path, 'tmp_m6a_right.distance'), 'a') as da:
            da.write(list2line(right_m6a_distances))
        with open(os.path.join(out_path, 'tmp_um6a_right.distance'), 'a') as da:
            da.write(list2line(right_um6a_distances))

    # return left_m6a_dis_list, left_um6a_dis_list, right_m6a_dis_list, right_um6a_dis_list


def list2line(a_list):
    a_line = ''
    a_list.sort()
    for data in a_list:
        a_line += str(data)
        a_line += '\t'
    return a_line


if __name__ == '__main__':
    indexes_path = '/data/dengyongjie/altSplicing/datas/mapData/index'
    out_path = '/data/dengyongjie/altSplicing/datas/mapData/distance'

    if os.path.exists(out_path):
        shutil.rmtree(out_path)
    os.makedirs(out_path)

    load_path(indexes_path, out_path)

    with open(os.path.join(out_path, 'tmp_m6a_left.distance'), 'r') as dr:
        total_m6a_ld = dr.readline().strip()
    with open(os.path.join(out_path, 'tmp_um6a_left.distance'), 'r') as dr:
        total_um6a_ld = dr.readline().strip()
    with open(os.path.join(out_path, 'tmp_m6a_right.distance'), 'r') as dr:
        total_m6a_rd = dr.readline().strip()
    with open(os.path.join(out_path, 'tmp_um6a_right.distance'), 'r') as dr:
        total_um6a_rd = dr.readline().strip()

    with open(os.path.join(out_path, 'total.distance'), 'w') as dw:
        dw.write(total_m6a_ld + '\n')
        dw.write(total_um6a_ld + '\n')
        dw.write(total_m6a_rd + '\n')
        dw.write(total_um6a_rd + '\n')
