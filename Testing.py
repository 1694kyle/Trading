from Classes.Options.ImpliedVolatility.ImpliedVolatilityModel import ImpliedVolatilityModel
import matplotlib.pyplot as plt
from Classes.Options.Pricing.FiniteDifferenceMethod.FDCnAm import FDCnAm

def iv():
    strikes = [75, 80, 85, 90, 92.5, 95, 97.5,100, 105, 110, 115, 120, 125]
    put_prices = [0.16, 0.32, 0.6, 1.22, 1.77, 2.54, 3.55,4.8, 7.75, 11.8, 15.96, 20.75, 25.81]
    model = ImpliedVolatilityModel(99.62, 0.0248, 78/365.,0.0182, 77, is_call=False)
    impvols_put = model.get_implied_volatilities(strikes,put_prices)


    plt.plot(strikes, impvols_put)
    plt.xlabel('Strike Prices')
    plt.ylabel('Implied Volatilities')
    plt.title('AAPL Put Implied Volatilities expiring in 78 days')
    plt.show()

def FD():
    """
    :supply:S0, K, r, T, sigma, Smax, M, N, omega, tol, is_call=True
    """
    option = FDCnAm(127.17, .01, 90, 1.58333, .0979, 150, 10, 10)

    print option.price()

FD()