#!/usr/bin/python3
"""
This function is used to generate the minimum number of operations
"""


def minOperations(n):
    ''' It returns the minimum number of operations
    Args: n (int): the number to calculate the minimum operations for
    '''
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
