from __future__ import division
from scipy import stats
import numpy as np
import statsmodels.api as sm

def linregress(security):
    """
    takes stock return data and runs a least squares regression against market return data
    :param market_returns: pandas time series return data
    :param stock_returns: pandas time series return data
    :return: beta, alpha, r_value, p_value, std_err
    """
    # todo: provide time series data with stock_returns and get a matched market_returns data set
    # todo: have linregress fetch stock data
    security_returns, market_returns = _get_returns(security)

    return stats.linregress(security_returns, market_returns)


def sml(security):
    beta, alpha, r_value, p_value, std_err = linregress(security)
    rf = _get_risk_free_rate()
    rm = _get_market_risk_premium()
    return rf + beta * (rm - rf)

def _get_returns(stock):
    pass

def _get_risk_free_rate():
    pass

def _get_market_risk_premium():
    pass