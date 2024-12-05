import numpy as np
import pandas as pd
from numpy.testing import assert_equal, assert_array_equal
from pandas.testing import assert_frame_equal


def nearest_value(X: np.ndarray, a):
    distance = np.abs(np.subtract(X, a))
    mn = np.min(distance)
    where = np.where(distance == mn)
    t = X[*where]  # Не понимаю как реализовать X[*where] в 3.8 не работает, зато пашет в 3.12
    return min(t)




Y = np.array([[ 2,  2],
        [12,  12]])
b = 7
X = np.array([[ 1,  2, 13],
              [15,  6,  8],
              [ 7, 18,  9]])
a = 7.2

print(nearest_value(X, a))

######################################################
assert_equal(
    nearest_value(np.array([ 1,  2, 13]), 10),
    13)
######################################################
assert_equal(
    nearest_value(np.array([ -1,  0]), -0.5),
    -1)
######################################################
assert_equal(
    nearest_value(np.array([[[ 1], [2],[3]],[[4],[5],[6]]]), 4.5),
    4)
######################################################
assert_equal(
    nearest_value(np.array([[ 1,  2, 13],
                            [15,  6,  8],
                            [ 7, 18,  9]]), 7.2),
    7)
######################################################
assert_equal(
    nearest_value(np.array([[ -1,  -2],
                            [-15,  -6]]), -100),
    -15)
######################################################
assert_equal(
    nearest_value(np.array([[ 2,  2],
                            [12,  12]]), 7),
    2)
######################################################
assert_equal(
    nearest_value(np.array([[ -2,  -2],
                            [-12,  -12]]), -7),
    -12)
######################################################