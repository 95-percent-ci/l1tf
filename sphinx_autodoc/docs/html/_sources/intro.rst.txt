Introduction
=============

Introduction
***************
Estimation of underlying trends in time series data is useful in a variety of disciplines ( econometrics, process
control engineering etc). :math:`l_1` trend filtering is a novel method of extracting trends from a time series data. It substitutes sum of
squares penalization term used in Hodrick-Prescott(H-P) Filtering by a sum of absolute values(i.e., an :math:`l_1` norm). This
produces trend estimates that are piecewise linear. Changes in slope in extracted trend can aid in extracting underlying
steady state condition in the signal. Mathematically it tries minimize following objective function.

.. math::
   (1/2)\sum_{t=1}^{n}(y_t - x_t)^2 + \lambda \sum_{t=1}^{n}|x_{t-1} - 2x_t + x_{t+1}|

Where :math:`\lambda` is a nonnegative parameter used to control the trade-off between smoothness of :math:`x` and
size of the residual. Same objective could also be written as

.. math::
   (1/2)||y-x||_2^2  + \lambda ||Dx||_1

where :math:`D` :math:`\in R^{(n-2)\times n}` is the second order difference matrix

.. math::

   \begin{bmatrix}
   1 & -2 & 1 & \cdots & \cdots & \cdots & \cdots & 0\\
   0 & 1 & -2 & 1 & & & & \vdots\\
   0 & 0 & 1 & -2 & \ddots & & & \vdots\\
   \vdots & 0 & \ddots & \ddots & \ddots & \ddots & & \vdots\\
   \vdots & & \ddots & \ddots & \ddots & \ddots & 1 & \vdots\\
   0 & & & \ddots & \ddots & 1 & -2 & 1\\
   \end{bmatrix}

The Lagrangian turns out be

.. math::
   (1/2)||y-x||_2^2  + \lambda ||z||_1 + \nu^T(Dx - z)

where :math:`z` = :math:`Dx`. The dual of lagrangian is a convex quadratic program and it is given by

.. math::
   g(\nu) = (1/2)\nu^T DD^T \nu - y^T D^T \nu

subject to

.. math::
   -\lambda \leq \nu \leq  \lambda

The solution :math:`\nu^{lt}` of the dual, :math:`l_1` trend estimate can be estimated via

.. math::
   x^{lt} = y - D^T v^{lt}

Implementation
***************
CVXOPT ( Python Software For Convex Optimization ) is used directly for solving quadratic programming.
CVXOPT quadratic programming solver is used for solving the dual formulation. It solves
quadratic program of form

.. math::
   minimize :(1/2)x^T P x + q^T x

   constraint : Gx \leq h

   Ax = b

where

.. math::
   P = DD^T, q = -D y

and

.. math::
   G = \begin{bmatrix}
       1 & 1 & \cdots & 1 \\
       1 & 1 & \cdots &  1 \\
       1 & 1 & \cdots &  1 \\
       \vdots & \vdots &  \vdots & \vdots \\
       -1 & -1 & \cdots &  -1 \\
       -1 & -1 & \cdots & -1 \\
       -1 & -1 & \cdots & -1 \\
       \end{bmatrix}_{2(n-2) \times (n-2)}
       h = \begin{bmatrix}
           \lambda \\
           \lambda \\
           \lambda \\
           \vdots \\
           \lambda\\
           \lambda \\
           \lambda \\
           \end{bmatrix}_{2(n-2) \times 1}

.. math::
   G[:n-2,:] = 1, G[n-2:,:] = -1



The user is requested to go through `CVXOPT documentation <https://cvxopt.org/userguide/index.html>`_
and `Quadratic programming  <https://cvxopt.org/userguide/coneprog.html>`_ for better understanding.




