# -*- coding: UTF-8 -*-
"""

L1 Trend Filtering
********************

This is implementation of L-1 Trend Filtering as published in the paper  `S.-J. Kim, et al.,L-1 Trend Filtering,Society
for Industrial and Applied Mathematics
(2009) <https://web.stanford.edu/~boyd/papers/l1_trend_filter.html>`_

CVXOPT ( Python Software For Convex Optimization ) is used directly for solving quadratic programming. User is requested
to go through its documentation once. Link is provided below.

`CVXOPT documentation <https://cvxopt.org/userguide/index.html>`_
"""

import numpy as np
from cvxopt import spmatrix, matrix, solvers, sparse

from l1tf.get_tridiagonal_matrix import derivative_matrix


def l1_trend(signal, lamda, iter_max=1000, tol_abs=1e-7, tol_rel=1e-6, feas_rel=1e-7, refine=0):
    """
    This function checks if L-1 trend filtering can be done or not on the signal and initiates l1 trend filtering
    algorithm

    :param signal: Input signal
    :type signal: :class:`numpy.ndarray`

    :param lamda: Regularization paramater.
    :type lamda: float

    :param iter_max: Maximum number of iterations
    :type iter_max: int

    :param tol_abs: Absolute accuracy
    :type tol_abs: float

    :param tol_rel: Relative accuracy
    :type tol_rel: float

    :param feas_rel: Tolerance for feasibility conditions
    :type feas_rel: float

    :param refine: Number of iterative refinement steps when solving KKT equations
    :type refine: int

    :return: trend_ext: Extracted trend from the signal
    :rtype: :class:`numpy.ndarray`

    """

    if not issubclass(type(signal), np.ndarray):
        raise TypeError("Signal is not of type 'numpy.ndarray'")

    if not signal.dtype == 'float64':
        raise TypeError("Signal is not of data type 'np.float64'")

    length = len(signal)

    if not signal.shape == (length,):
        raise TypeError("Signal should be a 'numpy.ndarray' of shape (length,)")

    if np.sum(np.isinf(signal)) > 0:
        raise ValueError("Signal should not have inf values")

    if np.sum(np.isnan(signal)) > 0:
        raise ValueError("Signal should not have NaN values")

    if np.sum(np.iscomplex(signal)) > 0:
        raise ValueError("Signal should not have imaginary values")

    if np.iscomplex(lamda):
        raise ValueError("lamda_mul should not be a complex number")

    if np.isnan(lamda):
        raise ValueError("lamda_mul should not be a nan value")

    if not 0 <= lamda <= np.inf:
        raise ValueError("lamda_mul should lie in the interval [0, inf]")

    if length <= 3:
        raise ValueError("Signal length should at least be 3 ")

    diag_matrix = derivative_matrix(length)

    solvers.options["maxiters"] = iter_max
    solvers.options["abstol"] = tol_abs
    solvers.options["reltol"] = tol_rel
    solvers.options["feastol"] = feas_rel
    solvers.options["refinement"] = refine

    # Not showing progress
    solvers.options["show_progress"] = False

    temp = length - 2
    temp_ls = range(temp)
    sparse_diag_mat = sparse(matrix(diag_matrix))
    p_matrix = sparse_diag_mat * sparse_diag_mat.T
    sig = matrix(signal)
    q_matrix = -sparse_diag_mat * sig
    g_matrix = spmatrix([], [], [], (2 * temp, temp))
    g_matrix[:temp, :temp] = spmatrix(1.0, temp_ls, temp_ls)
    g_matrix[temp:, :temp] = -spmatrix(1.0, temp_ls, temp_ls)
    h_matrix = matrix(lamda, (2 * temp, 1), tc='d')
    dual_sol = solvers.qp(p_matrix, q_matrix, g_matrix, h_matrix)
    trend_ext = signal - np.dot(diag_matrix.T, dual_sol['x']).T
    trend_ext = np.ravel(trend_ext)

    return trend_ext
