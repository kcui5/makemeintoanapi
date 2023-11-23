import numpy as np
from pd_alt import getSumTwo

def getSum(x, y):
    a = np.array([x, y, 3])
    return np.sum(a) + getSumTwo()
