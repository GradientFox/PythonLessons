import numpy as np
from numpy.testing import assert_array_equal


def num_sum(a: np.ndarray) -> np.ndarray:
    T = [sum(map(int, list(x))) for x in list(map(str, a))]
    return np.array(T)


a = np.array([1241, 354, 121])
print(num_sum(a))

######################################################
assert_array_equal(num_sum(np.array([82])), np.array([10]))
######################################################
assert_array_equal(num_sum(np.array([1241, 354, 121])), np.array([8, 12, 4]))
######################################################
assert_array_equal(num_sum(np.array([1, 22, 333, 4444, 55555])), np.array([1, 4, 9, 16, 25]))
######################################################
