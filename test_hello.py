import os

def test_this():
    from dataset_achilles import dataloader

    base_url = 'https://github.com/jehoons/dataloader/raw/master/testdata'
    
    testset1 = dataloader.dataloader(base_url+'/synergy_data.tar.gz')    
    testset1.ls()
    
    path = testset1.abspath('synergy_data/ch1_test_monoTherapy.csv')
    print(path)
    assert os.path.exists(path)

    testset2 = dataloader.dataloader(base_url+'/ch2_test_monoTherapy.csv.gz')
    path = testset2.abspath()
    print(path)
    assert os.path.exists(path)

    testset3 = dataloader.dataloader(base_url+'/ch2_test_monoTherapy_uncompressed.csv')
    path = testset3.abspath()
    print(path)
    assert os.path.exists(path)

