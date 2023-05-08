import os
import sys
import pandas as pd


def main():
    config = sys.argv[1]
    if config == 'total.distance':
        return 0
    else:
        config_df = pd.read_csv(config, sep='\t', header=None)


    tmp_path = config_df.loc['tmp_path', 0]
    sites_path = config_df.loc['sites_path', 0]
    indexes_path = config_df.loc['indexes_path', 0]
    out_path = config_df.loc['out_path', 0]


    os.system('python 1_genTmpData.py %s' % config)
    os.system('python 2_tmp2sit.py %s %s' % (tmp_path, sites_path))
    os.system('python 3_site2index.py %s %s' % (sites_path, indexes_path))
    os.system('python 4_index2distance.py %s %s' % (indexes_path, out_path))



if __name__ == '__main__':
    main()


