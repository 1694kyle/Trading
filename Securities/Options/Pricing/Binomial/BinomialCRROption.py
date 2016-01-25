""" Price an option by the binomial CRR model """
import math

import BinomialTreeOption


class BinomialCRROption(BinomialTreeOption.BinomialTreeOption):

    def _setup_parameters_(self):
        self.u = math.exp(self.sigma * math.sqrt(self.dt))
        self.d = 1./self.u
        self.qu = (math.exp((self.r-self.div)*self.dt) - self.d)/(self.u-self.d)  # Risk Neutral Probability of Up
        self.qd = 1-self.qu  # Risk Neutral Probability of Down
