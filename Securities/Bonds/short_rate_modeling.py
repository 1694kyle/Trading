""" Simulate interest rate path by the Vasicek model """
import math
import numpy as np

def vasicek(r0, K, theta, sigma, T=1., N=10, seed=777):
    np.random.seed(seed)
    dt = T/float(N)
    rates = [r0]
    for i in range(N):
        dr = K*(theta-rates[-1])*dt + sigma*np.random.normal()
        rates.append(rates[-1] + dr)
    return range(N+1), rates

""" Simulate interest rate path by the CIR model """

def cir(r0, K, theta, sigma, T=1.,N=10,seed=777):
    np.random.seed(seed)
    dt = T/float(N)
    rates = [r0]
    for i in range(N):
        dr = K*(theta-rates[-1])*dt + \
            sigma*math.sqrt(rates[-1])*np.random.normal()
        rates.append(rates[-1] + dr)
    return range(N+1), rates

""" Simulate interest rate path by the Rendleman-Barter model """

def rendleman_bartter(r0, theta, sigma, T=1.,N=10,seed=777):
    np.random.seed(seed)
    dt = T/float(N)
    rates = [r0]
    for i in range(N):
        dr = theta*rates[-1]*dt + \
             sigma*rates[-1]*np.random.normal()
        rates.append(rates[-1] + dr)
    return range(N+1), rates

""" Simulate interest rate path by the Brennan Schwartz model """

def brennan_schwartz(r0, K, theta, sigma, T=1., N=10, seed=777):
    np.random.seed(seed)
    dt = T/float(N)
    rates = [r0]
    for i in range(N):
        dr = K*(theta-rates[-1])*dt + \
            sigma*rates[-1]*np.random.normal()
        rates.append(rates[-1] + dr)
    return range(N+1), rates