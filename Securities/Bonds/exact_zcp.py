import numpy as np

""" Get zero coupon bond price by Vasicek model """
def exact_zcb(theta, kappa, sigma, tau, r0=0.):
    B = (1 - np.exp(-kappa*tau)) / kappa
    A = np.exp((theta-(sigma**2)/(2*(kappa**2))) * (B-tau) - (sigma**2)/(4*kappa)*(B**2))
    return A * np.exp(-r0*B)