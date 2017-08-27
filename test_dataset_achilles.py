import dataset_achilles
import pytest 

#@pytest.mark.skip(reason='noreason')
def test_loader():
    loader = dataset_achilles.return_loader()
    xxx
    
    loader.ls()    
    # datafile = 'v2.4.6/Achilles_v2.4.6.rnai.gct'
    # loader.cat(datafile)    
    # loader.head(datafile)
    # loader.tail('v2.4.6/Achilles_Analysis_README_v2.19.2.txt',3)

@pytest.mark.skip(reason='noreason')
def test_1():
    df = dataset_achilles.load_rawreads()
    print(df.head(2))

@pytest.mark.skip(reason='noreason')
def test_2(): 
    df = dataset_achilles.load_foldchange()
    print(df.head())

@pytest.mark.skip(reason='noreason')
def test_3(): 
    df = dataset_achilles.load_rawreads()

@pytest.mark.skip(reason='noreason')
def test_4(): 
    df = dataset_achilles.load_demeter_knockdown()

@pytest.mark.skip(reason='noreason')
def test_5(): 
    df = dataset_achilles.load_demeter_seed()

@pytest.mark.skip(reason='noreason')
def test_6(): 
    df = dataset_achilles.load_demeter_perf()
 
@pytest.mark.skip(reason='noreason')
def test_7(): 
    df = dataset_achilles.load_shrna_mapping()
