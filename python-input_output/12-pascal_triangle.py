#!/usr/bin/python3
"""
Function that returns the Pascal's triangle of n
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        list: Pascal's triangle as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        # Start each row with 1
        row = [1]
        # Compute the intermediate values
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        # End each row with 1
        row.append(1)
        triangle.append(row)

    return triangle
