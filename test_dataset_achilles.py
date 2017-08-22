
def test_hello():
    
    import dataset_achilles

    loader = dataset_achilles.return_loader()

    xxx

    # loader.ls()    

    df0 = dataset_achilles.load_rawreads()
    
    datafile = 'v2.4.6/Achilles_v2.4.6.rnai.gct'

    # loader.cat(datafile)
    
    # loader.head(datafile)    
    
    # loader.tail('v2.4.6/Achilles_Analysis_README_v2.19.2.txt',3)

    df0 = dataset_achilles.load_rnai()

    print(df0.head())

    df1 = dataset_achilles.load_rawreads()

    print(df1.head())


