import os
import numpy as np
from scipy.stats import chisquare


def load_file(distance_file):
    with open(distance_file, 'r') as dr:
        left_m6a_dis_list = dr.readline().strip().split('\t')
        left_um6a_dis_list = dr.readline().strip().split('\t')
        right_m6a_dis_list = dr.readline().strip().split('\t')
        right_um6a_dis_list = dr.readline().strip().split('\t')

    print('Notes: get datas!')
    print('Notes: length of distances is %d/%d/%d/%d' % (len(left_m6a_dis_list),len(left_um6a_dis_list),len(right_m6a_dis_list),len(right_um6a_dis_list)))

    return left_m6a_dis_list, left_um6a_dis_list, right_m6a_dis_list, right_um6a_dis_list


def get_cutoff_count(a_list, min_cut, max_cut):
    a_list.sort()
    count = 0
    for value in a_list:
        if min_cut <= int(value) <= max_cut:
            count += 1
    return count


def chi_test(a1, a2, b1, b2):
    value_sum = a1+a2+b1+b2
    pa = (a1 + a2) / value_sum
    pb = (b1 + b2) / value_sum
    p1 = (a1 + b1) / value_sum
    p2 = (a2 + b2) / value_sum

    e_a1 = value_sum * pa * p1
    e_a2 = value_sum * pa * p2
    e_b1 = value_sum * pb * p1
    e_b2 = value_sum * pb * p2

    obs = np.array([a1, a2, b1, b2])
    o_exp = np.array([e_a1, e_a2, e_b1, e_b2])
    result = chisquare(obs, f_exp=o_exp)
    print(result)
    return result[0], result[1]


def do_chi_test(positive_list, negative_list, range_a, range_b):
    a_p_count = get_cutoff_count(positive_list, range_a[0], range_a[1])
    b_p_count = get_cutoff_count(positive_list, range_b[0], range_b[1])
    a_n_count = get_cutoff_count(negative_list, range_a[0], range_a[1])
    b_n_count = get_cutoff_count(negative_list, range_b[0], range_b[1])
    chisq, p = chi_test(a_p_count, b_p_count, a_n_count, b_n_count)
    return chisq, p


if __name__ == '__main__':
    # distance_file = 'C:/Users/alan/Desktop/altSplicing/datas/mapData/total.distance'
    # distance_file = '/data/dengyongjie/altSplicing/datas/mapData/distance/total.distance'
    gap = 200
    import sys
    distance_file = sys.argv[1]

    left_m6a_distances, left_um6a_distances, right_m6a_distances, right_um6a_distances = load_file(distance_file)
    print()
    print('>5\'SS')
    chisq_left, p_left = do_chi_test(left_m6a_distances, left_um6a_distances, [-500, 0], [-1000, -500])
    print('>3\'SS')
    chisq_right, p_right = do_chi_test(right_m6a_distances, right_um6a_distances, [-500, 0], [-1000, -500])







