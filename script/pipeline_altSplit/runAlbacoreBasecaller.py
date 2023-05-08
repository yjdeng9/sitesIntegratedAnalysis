import os
import sys


def main():
    # os.system('source activate py36')
    # http://denbi-nanopore-training-course.readthedocs.io/en/latest/basecalling/basecalling.html
    # basecallor_1d = '/home/dengyj/anaconda3/envs/py36/bin/full_1dsq_basecaller.py'
    # basecallor = '/home/dengyj/anaconda3/envs/py36/bin/read_fast5_basecaller.py'
    basecallor = 'read_fast5_basecaller.py'
    flow_cell = 'FLO-MIN106'
    seq_kit = 'SQK-RNA001'

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # input_path = '/data/dengyongjie/altSplicing/datas/rawData/Naopore_raw_data/'
    # output_path = '/data/dengyongjie/altSplicing/datas/basecallingData/'

    if not os.path.exists(input_path):
        print('Error: fast5 file path is\'t existing! ')
        return
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    print("Notes:")
    print("   Input: %s\n   Output: %s\n"%(input_path, output_path))

    command = 'python %s -f %s -k %s -i %s -t %d -s %s -o fast5 -r' % \
              (basecallor, flow_cell, seq_kit, input_path, 40, output_path)
    os.system(command)

    # os.system('source deactivate')


if __name__ == '__main__':
    main()
