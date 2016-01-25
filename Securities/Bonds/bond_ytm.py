""" Get yield-to-maturity of a bond """
import scipy.optimize as optimize


def bond_ytm(price, par, T, coup, freq=2, guess=0.05):
    freq = float(freq)
    periods = T*freq
    coupon = coup/100.*par/freq
    dt = [(i+1)/freq for i in range(int(periods))]
    ytm_func = lambda(y): \
        sum([coupon/(1+y/freq)**(freq*t) for t in dt]) + \
        par/(1+y/freq)**(freq*t) - price

    return optimize.newton(ytm_func, guess)