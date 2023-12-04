# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.

import numpy as np

def mean(x):
    return sum(x) / len(x)

def pearson_correlation(x, y):
    mean_x = mean(x)
    mean_y = mean(y)
    
    diff_x = list(map(lambda i: i - mean_x, x))
    diff_y = list(map(lambda i: i - mean_y, y))
    
    numerator = sum(map(lambda a, b: a * b, diff_x, diff_y))
    denominator = np.sqrt(sum(map(lambda a: a ** 2, diff_x))) * np.sqrt(sum(map(lambda b: b ** 2, diff_y)))
    
    return numerator / denominator if denominator != 0 else 0

# Пример использования
array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]
correlation = pearson_correlation(array1, array2)
print(correlation)
