import pandas as pd
import numpy as np
from math import sqrt 

from scipy.stats import chi2, variation, norm
from statistics import variance


chat_id = 266642884 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    size = len(x)
    left = np.sqrt(size * (x ** 2).mean() / (3 * chi2.ppf(q=1 - alpha / 2, df=2 * size)))
    right = np.sqrt(size * (x ** 2).mean() / (3 * chi2.ppf(q=alpha / 2, df=2 * size)))
    
    return left, \
           right

