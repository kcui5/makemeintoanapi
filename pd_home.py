import numpy as np
from pd_alt import getSumTwo

def getSum():
    x = np.array([1, 2, 3])
    return np.sum(x) + getSumTwo()