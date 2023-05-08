import os
import shutil


def joint_exon(exon_line):
    forward_list = []
    reverse_list = []

    exon_list = exon_line.strip().split('\t')
    for exon_inf in exon_list:
        exon_notes = exon_inf.split(':')
        if len(exon_notes) < 3:
            continue
        if exon_notes[2] is '+':
            forward_list.append([int(exon_notes[0]), int(exon_notes[1])])
        else:
            reverse_list.append([int(exon_notes[0]), int(exon_notes[1])])

    return forward_list, reverse_list


def touch_a(sequence, exon_list, base):
    exon_set = set()
    base_set = set()

    for row in exon_list:
        for i in range(row[0], row[1]+1):
            exon_set.add(i)
            if sequence[i] == base:
                base_set.add(i)
    return exon_set, base_set


def touch_um(site_line, total_a, total_re_a):
    site_list = site_line.strip().split('\t')

    m6a_set = set()
    re_m6a_set = set()

    um6a_set = set()
    re_um6a_set = set()

    for site_inf in site_list:
        site_notes = site_inf.split(':')
        if len(site_notes) < 2:
            continue
        position = int(site_notes[0])
        if site_notes[1] is '+' and position in total_a:
            m6a_set.add(position)

        if site_notes[1] is '-' and position in total_re_a:
            re_m6a_set.add(position)

    for site in total_a:
        if site not in m6a_set:
            um6a_set.add(site)
    for site in total_re_a:
        if site not in re_m6a_set:
            re_um6a_set.add(site)

    len_total_a = (len(total_a)+len(total_re_a))
    len_m6a = len(m6a_set)+len(re_m6a_set)
    len_uma6a = len(um6a_set)+len(re_um6a_set)
    len_raw_m6a = len(site_list)

    print('%d:%d ; %d:%d'%(len_total_a, (len_m6a+len_uma6a), len_m6a, len_raw_m6a))

    return m6a_set, re_m6a_set, um6a_set, re_um6a_set


def set2line(a_set):
    a_line = ''
    a_list = list(a_set)
    a_list.sort()
    for data in a_list:
        a_line += str(data)
        a_line += '\t'
    return a_line


def main(chr_file, out_path):
    with open(chr_file, 'r') as tr:
        sequence = tr.readline()
        sequence = sequence.strip()

        exon_line = tr.readline()
        forward_list, reverse_list = joint_exon(exon_line)
        forward_exon_set, a_sites = touch_a(sequence, forward_list, 'A')
        reverse_exon_set, re_a_sites = touch_a(sequence, reverse_list, 'T')

        if len(forward_exon_set) == 0 and len(reverse_exon_set) == 0:
            return

        out_name = os.path.basename(chr_file).replace('.tmp', '.site')
        with open(os.path.join(out_path, out_name), 'w') as sw:
            sw.write(set2line(forward_exon_set) + '\n')
            sw.write(set2line(reverse_exon_set) + '\n')

            left_iso_line = tr.readline().strip()
            right_iso_line = tr.readline().strip()
            sw.write(left_iso_line + '\n')
            sw.write(right_iso_line + '\n')

            left_ss_line = tr.readline().strip()
            right_ss_line = tr.readline().strip()
            sw.write(left_ss_line + '\n')
            sw.write(right_ss_line + '\n')

            # //touch_非iso的ss

            site_line = tr.readline()
            m6a_set, re_m6a_set, um6a_set, re_um6a_set = touch_um(site_line, a_sites, re_a_sites)
            sw.write(set2line(m6a_set) + '\n')
            sw.write(set2line(um6a_set) + '\n')
            sw.write(set2line(re_m6a_set) + '\n')
            sw.write(set2line(re_um6a_set) + '\n')


if __name__ == '__main__':
    # tmp_path = '/data/dengyongjie/altSplicing/datas/mapData/tmp'
    # out_path = '/data/dengyongjie/altSplicing/datas/mapData/site'

    import sys
    tmp_path = sys.argv[1]
    out_path = sys.argv[2]

    if os.path.exists(out_path):
        shutil.rmtree(out_path)
    os.makedirs(out_path)

    for file in os.listdir(tmp_path):
        if '.tmp' not in file:
            continue
        file_path = os.path.join(tmp_path, file)
        count = 0
        for index, line in enumerate(open(file_path, 'r')):
            count += 1
        if count < 7:
            continue
        print('\n> chromosome' + file.replace('.tmp', ''))
        main(file_path, out_path)