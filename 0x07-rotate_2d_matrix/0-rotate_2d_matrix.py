#!/usr/bin/python3
"""
  0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """ rotate it 90 degrees clockwise. """
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
