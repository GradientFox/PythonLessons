import numpy as np

def replace_nans(X):
    print([len([x for x in i if x != np.nan]) for i in X[:,]])


X = np.array([[np.nan,      4,  np.nan],
              [np.nan, np.nan,       8],
              [np.nan,      5,  np.nan]])

print(replace_nans(X))