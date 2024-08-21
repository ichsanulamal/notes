import pickle

def load_dict_from_pickle(filename):
    """
    Load a dictionary with DataFrame values from a pickle file.
    
    Parameters
    ----------
    filename : str
        The path to the file from which the data will be loaded.
    
    Returns
    -------
    data_dict : dict
        Dictionary with string keys and DataFrame values.
    """
    with open(filename, 'rb') as f:
        data_dict = pickle.load(f)
    return data_dict

def get_ohlcvs():
    # Example usage
    ohlcvs = load_dict_from_pickle('input.pkl')
    # print(ohlcvs)

    for k in list(ohlcvs.keys()):
        if k in ['steth',
                'weeth',
                'ezeth',
                'reth',
                'meth',
                'eeth',
                'rseth']:
            del ohlcvs[k]

        if 'usd' in k:
            del ohlcvs[k]

    return ohlcvs

def get_closes():
    ohlcvs = get_ohlcvs()
    return {ticker: df['close'] for ticker, df in ohlcvs.items()}