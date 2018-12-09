"""
@param: n: An integer
@return: An integer, denote the number of trailing zeros in n!
"""

import math
from functools import reduce


def trailingZeros(n):
    # write your code here, try to do it without arithmetic operators.
    tmp = 0
    # for i in range(1, n + 1):
        # if i % 5 == 0:
            # tmp+=1
    sum = 0
    while n > 0:
        sum += int(n / 5)
        n /= 5
    return sum


print('number of \'0\':', trailingZeros(1001171717))
