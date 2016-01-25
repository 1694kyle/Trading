""" Price an American option by the Crank-Nicolson method """
import sys

import numpy as np

from FDCnEu import FDCnEu


class FDCnAm(FDCnEu):
    """
    S(t) is the option price at time t
    SO is the underlying asset price
    K is the option strike price
    r is the risk free rate
    T is the time to maturity
    sigma is the volatility of the underlying asset
    Smax is a suitably large asset price that cannot be reached by T
    M is the number of t nodes from t to T
    N is number of S nodes to for S to Smax
    omega is the over-relaxation parameter (higher = faster convergence, but more possibility of no convergence)
    """

    def __init__(self, S0, K, r, T, sigma, Smax, M, N, omega=1.2, tol=.001, is_call=True):
        super(FDCnAm, self).__init__(S0, K, r, T, sigma, Smax, M, N, is_call)
        self.omega = omega
        self.tol = tol
        self.i_values = np.arange(self.M+1)
        self.j_values = np.arange(self.N+1)

    def _setup_boundary_conditions_(self):
        if self.is_call:
            self.payoffs = np.maximum(
                self.boundary_conds[1:self.M]-self.K, 0)
        else:
            self.payoffs = np.maximum(
                self.K-self.boundary_conds[1:self.M], 0)

        self.past_values = self.payoffs
        self.boundary_values = self.K * \
                               np.exp(-self.r *
                                      self.dt *
                                      (self.N-self.j_values))

    def _traverse_grid_(self):
        """ Solve using linear systems of equations """
        aux = np.zeros(self.M-1)
        new_values = np.zeros(self.M-1)

        for j in reversed(range(self.N)):
            aux[0] = self.alpha[1]*(self.boundary_values[j] +
                                    self.boundary_values[j+1])
            rhs = np.dot(self.M2, self.past_values) + aux
            old_values = np.copy(self.past_values)
            error = sys.float_info.max

            while self.tol < error:
                new_values[0] = \
                    max(self.payoffs[0],
                        old_values[0] +
                        self.omega/(1-self.beta[1]) *
                        (rhs[0] -
                         (1-self.beta[1])*old_values[0] +
                         (self.gamma[1]*old_values[1])))

                for k in range(self.M-2)[1:]:
                    new_values[k] = \
                        max(self.payoffs[k],
                            old_values[k] +
                            self.omega/(1-self.beta[k+1]) *
                            (rhs[k] +
                             self.alpha[k+1]*new_values[k-1] -
                             (1-self.beta[k+1])*old_values[k] +
                             self.gamma[k+1]*old_values[k+1]))

                new_values[-1] = \
                    max(self.payoffs[-1],
                        old_values[-1] +
                        self.omega/(1-self.beta[-2]) *
                        (rhs[-1] +
                         self.alpha[-2]*new_values[-2] -
                         (1-self.beta[-2])*old_values[-1]))

                error = np.linalg.norm(new_values - old_values)
                old_values = np.copy(new_values)

            self.past_values = np.copy(new_values)

        self.values = np.concatenate(([self.boundary_values[0]],
                                      new_values,
                                      [0]))

    def _interpolate_(self):
        # Use linear interpolation on final values as 1D array
        return np.interp(self.S0,
                         self.boundary_conds,
                         self.values)