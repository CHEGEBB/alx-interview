#!/usr/bin/python3
'''
0-pascal_triangle
'''


def pascal_triangle(n):
    '''
    Returns a list of lists of integers representing Pascal’s triangle of n.
    '''
    if n <= 0:
        return []

    pascal_list = [[1]]

    for i in range(1, n):
        prev_row = pascal_list[-1]
        new_row = [1]
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        pascal_list.append(new_row)

    return pascal_list
