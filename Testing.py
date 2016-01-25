from Securities.Options.ImpliedVolatility.ImpliedVolatilityModel import ImpliedVolatilityModel
from Securities.Options.Pricing.FiniteDifferenceMethod.FDCnAm import FDCnAm
from Securities.Bonds.BootstrapYieldCurve import BootstrapYieldCurve
from Securities.Bonds.bond_ytm import bond_ytm
from Securities.Bonds.bond_price import bond_price
import matplotlib.pyplot as plt


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
    option = FDCnAm(S0=127.17, K=90, r=.01, T=.005468, sigma=.0979, Smax=150, M=100, N=100)

    print option.price()

def bootstrap():

    yield_curve = BootstrapYieldCurve()
    yield_curve.add_instrument(100, 0.25, 0., 97.5)
    yield_curve.add_instrument(100, 0.5, 0., 94.9)
    yield_curve.add_instrument(100, 1.0, 0., 90.)
    yield_curve.add_instrument(100, 1.5, 8, 96., 2)
    yield_curve.add_instrument(100, 2., 12, 101.6, 2)
    y = yield_curve.get_zero_rates()
    x = yield_curve.get_maturities()
    plt.plot(x, y)
    plt.title("Zero Curve")
    plt.ylabel("Zero Rate (%)")
    plt.xlabel("Maturity in Years")
    plt.show()

def ytm():
    ytm = bond_ytm(95.0428, 100, 1.5, 5.75, 2)
    print ytm
    return ytm

def bond_p():
    price = bond_price(100, 1.5, ytm(), 5.75, 2)
    print price

