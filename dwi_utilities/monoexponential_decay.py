"""
@author: pritesh-mehta
"""

import numpy as np

def func(x, a, c):
    """monoexponential decay function
    """
    return a * np.exp(-c * x)

def log_func(x, a, c):
    """logarithm of monoexponential decay function - easier to fit linear 
    model
    """
    return a - c * x