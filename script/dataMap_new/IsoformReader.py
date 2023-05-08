
class Isoform:
    def __init__(self):
        self.fasta_path = ''
        self.fastq_path = ''

        self.chr = ''

        self.left = 0
        self.right = 0
        self.median_left = 0.0
        self.median_right = 0.0

    def show(self):
        print('%s\t%d\t%d\t%f\t%f' % (self.chr, self.left, self.right, self.median_left, self.median_right))


class IsoformReader:
    def __init__(self, isoform_list):
        self.iso_dict = {}
        with open(isoform_list, 'r') as ir:
            for line in ir:

                notes = line.strip().split('\t')
                inf = notes[2].split('_')

                iso = Isoform()
                iso.fasta_path = notes[0]
                iso.fastq_path = notes[1]
                iso.chr = inf[0]
                iso.left = int(inf[2])  # 5'SS
                iso.right = int(inf[3])  # 3'SS
                iso.median_left = float(inf[4])
                iso.median_right = float(inf[5])

                chromosome = 'chr'+iso.chr

                if chromosome in self.iso_dict.keys():
                    self.iso_dict[chromosome].append(iso)
                else:
                    self.iso_dict[chromosome] = []
                    self.iso_dict[chromosome].append(iso)


if __name__ == '__main__':
    iso_list = '/data/dengyongjie/altSplicing/datas/mandalorionData/isoform_list'
    ir = IsoformReader(iso_list)
    print(len(ir.iso_dict))
