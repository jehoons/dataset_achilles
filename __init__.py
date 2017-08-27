import os
import pandas as pd 
from os.path import dirname, exists, join

#module_dir = dirname(__file__)
#if not exists(join(module_dir, 'downloader')): 
#    os.system('git clone git@github.com:jehoons/downloader.git %s/downloader' % module_dir)

from downloader import _downloader


def return_loader(): 
    _baseurl = 'http://143.248.32.25/~jhsong/dataset/Perturbation/Achilles'
    return _downloader(_baseurl+'/v2.4.6.tar.gz')


def load_rawreads():
    # Raw readcount file for cell lines using the 98k shRNA library. 
    datafile = 'v2.4.6/Achilles_v2.19.1_rawreads.csv'
    return pd.read_csv(return_loader().find(datafile))


def load_foldchange(): 
    # shRNA level log fold change scores (quantile normalized) for 216 cell lines
    # passing quality control with the 54k library
    datafile = 'v2.4.6/Achilles_v2.4.6.rnai.gct'
    return pd.read_csv(return_loader().find(datafile), sep='\t', skiprows=2)


def load_demeter_knockdown():
    # DEMETER inferred gene knockdown effect in cell lines 
    datafile = 'v2.4.6/ExpandedGeneZSolsCleaned.csv'
    # first column as index - 
    return pd.read_csv(return_loader().find(datafile), index_col=0)


def load_demeter_seed():
    datafile = 'v2.4.6/SeedSolsCleaned.csv'
    # first column as index - 
    return pd.read_csv(return_loader().find(datafile), index_col=0)


def load_demeter_perf():
    datafile = 'v2.4.6/TableS3_shRNAPerformance.csv'
    return pd.read_csv(return_loader().find(datafile), index_col='shRNAID')


def load_shrna_mapping():
    datafile = 'v2.4.6/shrna_mapping_20150312.tsv'
    return pd.read_csv(return_loader().find(datafile), sep='\t')
