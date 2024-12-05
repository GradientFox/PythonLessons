import numpy as np
from numpy.testing import assert_equal, assert_array_equal

def sort_evens(X):
    condition = (X%2==0)
    sorted_array = np.sort(X[condition])
    index = np.where(condition)
    temp = X
    temp[index] = sorted_array
    return temp


A = np.array([43, 66, 34, 55, 78, 105, 2])
print(sort_evens(A))


######################################################
assert_array_equal(sort_evens(np.array([])), np.array([]))
######################################################
assert_array_equal(sort_evens(np.array([2, 0])), np.array([0, 2]))
######################################################
assert_array_equal(sort_evens(np.array([9, 3, 1, 5, 7])), np.array([9, 3, 1, 5, 7]))
######################################################
assert_array_equal(sort_evens(np.array([8, 12, 4, 10, 6, 2])), np.array([2, 4, 6, 8, 10, 12]))
######################################################