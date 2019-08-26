# -*- coding: UTF-8 -*-
"""
Tridiagonal matrix
=====================

Helper functions defined here create sparse toeplitz matrix for computation of the L-1 trend. Toeplitz matrix is a
matrix in which each descending diagonal from left to right is a constant. Following is an example of Toeplitz matrix.


"""
import numpy as np
from scipy.linalg import toeplitz


def derivative_matrix(length):
    """
    Get Sparse toeplitz matrix for the computation of l1 trend.

    :param length: length of the input signal
    :type length: int

    :return: der_matrix
    :rtype: :class:`numpy.ndarray`
    """
    row = np.zeros(length)
    row[0] = 1
    row[1] = -2
    row[2] = 1

    col = np.zeros(length - 2)
    col[0] = 1

    der_matrix = toeplitz(col, row)

    return der_matrix
