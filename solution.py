import pandas as pd
import numpy as np
from math import sqrt 

from scipy.stats import chi2, variation, norm
from statistics import variance


chat_id = 266642884 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    s2 = variance(x)
    s = sqrt(s2)
    q = sqrt((len(x) - 1) / chi2.ppf(alpha / 2, len(x) - 1)) - 1

    left = s * (1 - q) / sqrt(3)
    right = s * (1 + q) / sqrt(3)

    return left, right

