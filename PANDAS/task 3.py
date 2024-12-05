import numpy as np
from numpy.testing import assert_array_equal


def tensor_mask(X, mask):
    T = abs(X-mask)
    return T


X = np.array([
    [[1, 0, 1],
     [1, 1, 1],
     [0, 0, 1]],

    [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]]
])
mask = np.array([[1, 1, 0],
                 [1, 1, 0],
                 [1, 1, 0]])


print(tensor_mask(X, mask))


######################################################
X = np.zeros(9, dtype=int).reshape((1,3,3))
mask = np.zeros(9, dtype=int).reshape((3,3))
assert_array_equal(tensor_mask(X, mask), np.zeros(9, dtype=int).reshape((1,3,3)))
######################################################
X = np.zeros(9*3, dtype=int).reshape((3,3,3))
mask = np.ones(9, dtype=int).reshape((3,3))
assert_array_equal(tensor_mask(X, mask), np.ones(9*3, dtype=int).reshape((3,3,3)))
######################################################
X = np.array([[[ 1, 0, 1],
               [ 1, 1, 1],
               [ 0, 0, 1]]])
mask = np.array([[1, 1, 0],
                 [1, 1, 0],
                 [1, 1, 0]])
assert_array_equal(tensor_mask(X, mask),
                   np.array([[[0, 1, 1],
                             [0, 0, 1],
                             [1, 1, 1]]]))
######################################################