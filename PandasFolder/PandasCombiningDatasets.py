import pandas as pd
import numpy as np

def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind]
        for c in cols}
    return pd.DataFrame(data, ind)

mypd= make_df('ABCD',range(3))
print(mypd,mypd.ndim,mypd.size,mypd.shape,mypd.columns)
