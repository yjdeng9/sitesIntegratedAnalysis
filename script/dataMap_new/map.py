import sys

from IsoformReader import IsoformReader
from MATKReader import ResultReader

# iso_path = sys.argv[1]
# peak_path = sys.argv[2]

iso_path = '/data/dengyongjie/altSplicing/datas/mandalorionData/isoform_list'
peak_path = '/data/dengyongjie/altSplicing/datas/matkData/peak.bed'


def count_distance(isoform, peak):
    if isoform.left < isoform.right:
        iso_start = isoform.left
        iso_end = isoform.right
    else:
        isoform.show()
        iso_start = isoform.right
        iso_end = isoform.left

    if peak.start < peak.end:
        peak_start = peak.start
        peak_end = peak.end
    else:
        peak_start = peak.end
        peak_end = peak.start

    distance = max(iso_start, peak_start)-min(iso_end, peak_end)
    if distance < 0:
        distance = 0

    return distance


iso_num = 0
match_num = 0
match_index = {}

iso_read = IsoformReader(iso_path)
peak_read = ResultReader(peak_path, 'peak')
iso_index = iso_read.iso_dict
peak_index = peak_read.peak_dict

for chromosome in iso_index.keys():
    if chromosome not in peak_index.keys():
        print("Notes: peak dict has't chromosome %s" % chromosome)
        continue

    match_index[chromosome] = []

    for tmp_iso in iso_index[chromosome]:
        iso_num = iso_num + 1
        for tmp_peak in peak_index[chromosome]:
            tmp_distance = count_distance(tmp_iso, tmp_peak)
            if tmp_distance <= 20:
                match_num = match_num + 1
                match_index[chromosome].append(tmp_distance)

print('matched: %d/%d, %f' % (match_num, iso_num, (match_num*100/iso_num)), end='')
print('%')

for chromosome in match_index.keys():
    print(chromosome, end='\t')
    print(len(match_index[chromosome]), end='\t')
    print(match_index[chromosome].count(0))


