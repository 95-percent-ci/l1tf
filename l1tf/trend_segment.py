# -*- coding: UTF-8 -*-
"""
Result Extraction
=====================

Functions defined here are used to extract all the linear segment once L1 trend is computed.

"""
import numpy as np


def extract_segment(trend, slope_tol=1e-6):
    """
    This function extracts segments of trend which have the same slope

    :param trend: trend of the signal
    :type trend: :class:`numpy.ndarray`

    :param slope_tol: Required Tolerance for calculation of slope
    :type slope_tol: float

    :return: Change points in the extracted trend
    :rtype: :class:`numpy.ndarray`
    """
    second_difference = np.abs(np.diff(trend, n=2))
    change_points = np.ravel(np.where(second_difference > slope_tol))
    change_points += 2
    return np.concatenate(([0], change_points, [len(trend) - 1]))


def get_result(trend, signal, change_points):
    """
    This function returns fit results for each segment. Values for each segment are stored in a list.

    :param trend: L1 trend of signal
    :type trend: :class:`numpy.ndarray`

    :param signal: Signal
    :type signal: :class:`numpy.ndarray`

    :param change_points: change points in the extracted trend
    :type change_points: :class:`numpy.ndarray`

    :return: A tuple of dictionary,where

            * in the first element

                * key is 'segment_result'
                * values are stored in a list. Each list element is of :class:`l1tf.trend_segment.TrendResult` datatype.

            * in the second element

                * key is 'overall_mse'
                * stores total mean square error between the trend and the signal.


    :rtype: dict
    """
    list_result = []
    overall_mse = np.sum(np.square(signal) - np.square(trend)) / len(signal)
    for j in range(len(change_points) - 1):
        change_point_ind = change_points[j: j + 2]
        segment_result = TrendResult(change_point_ind, trend, signal)
        segment_result.get_slope_intercept()
        segment_result.get_segment_fit_result(signal)
        list_result.append(vars(segment_result))
    result_dict = {'segment_result': list_result, 'overall_mse': overall_mse}
    return result_dict


class TrendResult(object):
    """
    This class instantiates an object will following attributes: slope, intercept, start, end, segment_trend, residual,
    y.

    :ivar change_point_ind: Change point indices for particular segment
    :vartype change_point_ind: :class:`numpy.ndarray`

    :ivar trend: Extracted L1 trend of signal
    :vartype trend: :class:`numpy.ndarray`

    :ivar signal: Original Signal
    :vartype y: :class:`numpy.ndarray`
    """

    @staticmethod
    def check(change_point_ind, trend, signal):
        """
        Function to check for valid inputs.

        :param change_point_ind: change point indices for particular segment
        :type change_point_ind: :class:`numpy.ndarray`

        :param trend: Extracted L1 trend of signal
        :type trend: :class:`numpy.ndarray`

        :param signal: Original Signal
        :type signal: :class:`numpy.ndarray`

        :return: Nothing
        :rtype: None
        """
        if not any((issubclass(type(signal), np.ndarray), issubclass(type(trend), np.ndarray))):
            raise TypeError("Signal or Trend is not of type 'numpy.ndarray'")

        if not any((signal.dtype == 'float64', trend.dtype == 'float64')):
            raise TypeError("Signal or trend is not of data type 'np.float64'")

        if np.sum(np.isinf(signal)) or np.sum(np.isinf(trend)) > 0:
            raise ValueError("Signal or trend should not have inf values")

        if np.sum(np.isnan(signal)) > 0 or np.sum(np.isnan(trend)) > 0:
            raise ValueError("Signal or trend should not have NaN values")

        if np.sum(np.iscomplex(signal)) > 0 or np.sum(np.iscomplex(trend)) > 0:
            raise ValueError("Signal or trend should not have imaginary values")

        if not issubclass(type(change_point_ind), np.ndarray):
            raise TypeError("Change points is not of the type 'numpy.ndarray'")

        if np.sum(np.isnan(change_point_ind)) > 0 or np.sum(np.isinf(change_point_ind)) > 0:
            raise TypeError(" Change point should not contain nan or inf values ")

    def __init__(self, change_point_ind, trend, signal):
        self.check(change_point_ind, trend, signal)
        self.slope = None
        self.intercept = None
        self.start = None
        self.end = None
        self.segment_trend = None
        self.segment_mse = None
        self.residual = None
        self.signal = None
        if self.start is None and self.end is None and self.segment_trend is None and self.signal is None:
            self.start = change_point_ind[0]
            self.end = change_point_ind[-1]
            self.segment_trend = trend[self.start: self.end + 1]
            self.signal = signal[self.start: self.end + 1]

    def get_slope_intercept(self):
        """
        calculates slope and intercept and stores values in class object attribute : slope and intercept.

        :return: Nothing
        :rtype: None
        """
        if self.slope is None and self.intercept is None:
            if not np.isinf((self.segment_trend[-1] - self.segment_trend[0]) / len(self.segment_trend)):
                self.slope = (self.segment_trend[-1] - self.segment_trend[0]) / len(self.segment_trend)
                self.intercept = self.segment_trend[-1] - self.slope * self.end
            else:
                self.slope = np.inf
                self.intercept = self.start

    def get_segment_fit_result(self, signal):
        """
        Calculates residue and mean square error in a segment. It stores values in class object attribute : segment_mse
        and residual

        :param signal: Original Signal
        :type signal: :class:`numpy.ndarray`

        :return: Nothing
        :rtype: None
        """
        if self.segment_mse is None and self.residual is None:
            self.segment_mse = np.sum(np.square(signal[self.start:self.end + 1]) - np.square(self.segment_trend)) / len(
                self.segment_trend)
            self.residual = np.sum(np.subtract(signal[self.start: self.end + 1], self.segment_trend))
