class Site:
    def __init__(self):
        self.chr = ''
        self.position = 0
        self.score = 0.0
        self.direction = ''


class Peak:
    def __init__(self):
        self.chr = ''
        self.start = 0
        self.end = 0
        self.score = 0.0

    def show(self):
        print('%s\t%d\t%d\t%f' % (self.chr, self.start, self.end, self.score))


class ResultReader:
    def __init__(self, input_file, f_type):
        self.peak_dict = {}

        self.input_file = input_file
        if f_type is 'peak':
            self.read_peak_bed()

        if f_type is 'site':
            self.read_site_bed()

    def read_site_bed(self):
        with open(self.input_file, 'r') as pr:
            for line in pr:
                notes = line.strip().split('\t')

                site = Site()
                site.chr = notes[0]
                site.position = int(notes[1])
                site.score = float(notes[4])
                site.direction = notes[5]

                chromosome = 'chr'+site.chr

                if chromosome in self.peak_dict.keys():
                    self.peak_dict[chromosome].append(site)
                else:
                    self.peak_dict[chromosome] = []
                    self.peak_dict[chromosome].append(site)

    def read_peak_bed(self):
        with open(self.input_file, 'r') as pr:
            for line in pr:
                notes = line.strip().split('\t')

                peak = Peak()
                peak.chr = notes[0]
                peak.start = int(notes[1])
                peak.end = int(notes[2])
                peak.score = float(notes[4])

                chromosome = 'chr'+peak.chr

                if chromosome in self.peak_dict.keys():
                    self.peak_dict[chromosome].append(peak)
                else:
                    self.peak_dict[chromosome] = []
                    self.peak_dict[chromosome].append(peak)


if __name__ == '__main__':
    peak_bed = '/data/dengyongjie/altSplicing/datas/matkData/peak.bed'
    pr = ResultReader(peak_bed, 'peak')
    peak_list = pr.peak_dict
    print(len(peak_list))
