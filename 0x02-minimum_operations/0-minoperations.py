#!/usr/bin/python3
"""min operations function"""


def minOperations(n):
    """min operations function"""
    if n <= 1:
        return 0
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    result = sum(factors)
    return result
