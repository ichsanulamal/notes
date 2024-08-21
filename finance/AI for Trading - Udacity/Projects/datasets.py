import pickle
import pandas as pd
import numpy as np
from datetime import date

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

def get_ohlcvs(from_date=None, to_date=None):
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
                'rseth',
                'dai',
                'wbtc']:
            del ohlcvs[k]

        if 'usd' in k:
            del ohlcvs[k]

    if from_date != None:
        if to_date == None:
            to_date = date.today()

        for key in ohlcvs.keys():
            df:pd.DataFrame = ohlcvs[key]
            ohlcvs[key] = df.loc[from_date:to_date, :]

    return ohlcvs

def get_closes(ohlcvs):
    return pd.DataFrame({ticker: df['close'] for ticker, df in ohlcvs.items()}) 

def get_log_returns(closes_df: pd.DataFrame):
    return np.log(closes_df / closes_df.shift(1))


    