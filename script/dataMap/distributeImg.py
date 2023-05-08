import sys

import matplotlib.pyplot as plt
import numpy as np


def load_file(distance_file):
    with open(distance_file, 'r') as dr:
        left_m6a_dis_list = dr.readline().strip().split('\t')
        left_um6a_dis_list = dr.readline().strip().split('\t')
        right_m6a_dis_list = dr.readline().strip().split('\t')
        right_um6a_dis_list = dr.readline().strip().split('\t')

    print('Notes: get datas!')
    print('Notes: length of distances is %d/%d/%d/%d' % (len(left_m6a_dis_list),len(left_um6a_dis_list),len(right_m6a_dis_list),len(right_um6a_dis_list)))

    return left_m6a_dis_list, left_um6a_dis_list, right_m6a_dis_list, right_um6a_dis_list

def count_rate(wing, gap, distance_list):
    matched = []
    rate_list = []

    for tmp_distance in distance_list:
        if wing > int(tmp_distance) >= -wing:
            matched.append(int(tmp_distance))

    for i in range(-wing, wing, gap):
        tmp_add = 0
        for j in range(i, i + gap):
            tmp_add = tmp_add + matched.count(j)
        rate_list.append(tmp_add / len(matched))

    return rate_list


def draw_img(m6a_counts, um6a_counts, wing, gap):
    plt.plot(range(-wing, wing, gap), m6a_counts, color='yellowgreen', label='m6a')
    plt.plot(range(-wing, wing, gap), um6a_counts, color='pink', label='um6a')
    # plt.show()
    # plt.savefig('/data/dengyongjie/altSplicing/datas/matkData/test.png')
    plt.savefig(sys.argv[1] + '.png')


def draw_img_plus(m6a_lr, um6a_lr, m6a_rr, um6a_rr, wing, gap):
    fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(9, 6))
    ax0.plot(range(-wing, wing, gap), m6a_lr, color='yellowgreen', label='m6a')
    ax0.plot(range(-wing, wing, gap), um6a_lr, color='pink', label='um6a')
    ax0.set_title('5\'SS')
    ax0.text(-500, 0.05, 'pvalue=3.49e-08')

    ax1.plot(range(-wing, wing, gap), m6a_rr, color='yellowgreen', label='m6a')
    ax1.plot(range(-wing, wing, gap), um6a_rr, color='pink', label='um6a')
    ax1.set_title('3\'SS')
    ax1.text(500, 0.05, 'pvalue=0.89')

    # plt.show()
    plt.savefig('/data/dengyongjie/altSplicing/datas/matkData/distance_dist.png')


if __name__ == '__main__':
    # distance_file = 'C:/Users/alan/Desktop/altSplicing/datas/mapData/total.distance'
    # distance_file = '/data/dengyongjie/altSplicing/datas/mapData/distance/total.distance'
    wing = 1000
    gap = 3

    distance_file = sys.argv[1]

    left_m6a_distances, left_um6a_distances, right_m6a_distances, right_um6a_distances = load_file(distance_file)

    # left_m6a_rates = count_rate(wing, gap, left_m6a_distances)
    # left_um6a_rates = count_rate(wing, gap, left_um6a_distances)
    # right_m6a_rates = count_rate(wing, gap, right_m6a_distances)
    # right_um6a_rates = count_rate(wing, gap, right_um6a_distances)
    # draw_img_plus(left_m6a_rates, left_um6a_rates, right_m6a_rates, right_um6a_rates, wing, gap)

    total_m6a = left_m6a_distances + right_m6a_distances
    total_um6a = left_um6a_distances + right_um6a_distances
    tmp_um6a = np.array(total_um6a,dtype=int)
    tmp_um6a = 0-tmp_um6a
    total_um6a = list(tmp_um6a)
    m6a_rates = count_rate(wing, gap, total_m6a)
    um6a_rates = count_rate(wing, gap, total_um6a)
    draw_img(m6a_rates, um6a_rates, wing, gap)



