import numpy as np

def getSumTwo():
    x = np.array([1, 2, 3, 4, 5])
    from fo.pd_home import getSumThree
    return np.sum(x) + getSumThree()