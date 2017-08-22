import os
from dataset_achilles.dataloader import _dataloader  
import pandas as pd 

# Tsherniak, Aviad, Francisca Vazquez, Phil G. Montgomery, Barbara A. Weir, Gregory Kryukov, Glenn S. 
# Cowley, Stanley Gill, et al. 2017. “Defining a Cancer Dependency Map.” Cell 170 (3): 564–576.e16. 
# doi:10.1016/j.cell.2017.06.010.

# ?rwxr-xr-x songj/197609          0 2017-08-15 23:27:10 v2.4.6/
# ?rw-r--r-- songj/197609        828 2017-08-15 13:36:55 v2.4.6/Achilles_Analysis_README_v2.19.2.txt
# ?rw-r--r-- songj/197609       1418 2017-08-15 13:39:01 v2.4.6/Achilles_Analysis_README_v2.4.6.txt
# ?rw-r--r-- songj/197609  388421933 2017-08-15 13:43:35 v2.4.6/Achilles_v2.19.1_rawreads.csv
# ?rw-r--r-- songj/197609  136983046 2017-08-15 13:40:31 v2.4.6/Achilles_v2.4.6.rnai.gct
# ?rw-r--r-- songj/197609   16231520 2017-08-15 13:39:00 v2.4.6/Achilles_v2.4.6_rawreads_cBOTv7_sbsv2.csv
# ?rw-r--r-- songj/197609  149219366 2017-08-15 13:40:35 v2.4.6/Achilles_v2.4.6_rawreads_cBOTv8_sbsv3.csv
# ?rw-r--r-- songj/197609      81851 2017-08-15 13:38:38 v2.4.6/Achilles_v2.4.6_v2.19.1_v2.20.1_SampleInfo.txt
# ?rw-r--r-- songj/197609  138291035 2017-08-15 13:40:22 v2.4.6/ExpandedGeneZSolsCleaned.csv
# ?rw-r--r-- songj/197609   50710752 2017-08-15 13:39:10 v2.4.6/SeedSolsCleaned.csv
# ?rw-r--r-- songj/197609   21015002 2017-08-15 13:36:52 v2.4.6/shrna_mapping_20150312.tsv
# ?rw-r--r-- songj/197609   20800239 2017-08-15 13:38:39 v2.4.6/TableS3_shRNAPerformance.csv

_baseurl = 'http://143.248.32.25/~jhsong/dataset/Perturbation/Achilles'

def return_loader(): 
    return _dataloader(_baseurl+'/v2.4.6.tar.gz')


def load_rawreads():
    datafile = 'v2.4.6/Achilles_v2.19.1_rawreads.csv'
    return pd.read_csv(return_loader().find(datafile))


def load_rnai(): 
    datafile = 'v2.4.6/Achilles_v2.4.6.rnai.gct'
    return pd.read_csv(return_loader().find(datafile), sep='\t', skiprows=2)

