import os
import pandas as pd 
from os.path import dirname, exists, join

module_dir = dirname(__file__)
if not exists(join(module_dir, 'downloader')): 
    os.system('git clone git@github.com:jehoons/downloader.git %s/downloader' % module_dir)

from dataset_achilles.downloader import _downloader

_baseurl = 'http://143.248.32.25/~jhsong/dataset/Perturbation/Achilles'

def return_loader(): 
    return _downloader(_baseurl+'/v2.4.6.tar.gz')


def load_rawreads():
    datafile = 'v2.4.6/Achilles_v2.19.1_rawreads.csv'
    return pd.read_csv(return_loader().find(datafile))


def load_rnai(): 
    datafile = 'v2.4.6/Achilles_v2.4.6.rnai.gct'
    return pd.read_csv(return_loader().find(datafile), sep='\t', skiprows=2)

