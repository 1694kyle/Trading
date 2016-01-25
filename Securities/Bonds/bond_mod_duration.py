""" Calculate modified duration of a bond """
from bond_ytm import bond_ytm
from bond_price import bond_price


def bond_mod_duration(price, par, T, coup, freq, dy=0.01):
    ytm = bond_ytm(price, par, T, coup, freq)

    ytm_minus = ytm - dy
    price_minus = bond_price(par, T, ytm_minus, coup, freq)

    ytm_plus = ytm + dy
    price_plus = bond_price(par, T, ytm_plus, coup, freq)

    mduration = (price_minus-price_plus)/(2*price*dy)
    return mduration

