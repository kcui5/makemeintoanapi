import numpy as np
from fo.pd_home import getSumThree

def getSumTwo():
    x = np.array([1, 2, 3, 4, 5])
    return np.sum(x) + getSumThree()