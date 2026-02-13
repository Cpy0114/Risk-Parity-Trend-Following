import numpy as np
import pandas as pd
from scipy.optimize import minimize

class RiskParityOptimizer:
    """
    Implementation of the Equal Risk Contribution (ERC) portfolio optimization.
    
    This module provides tools to solve for asset weights where each component 
    contributes equally to the total portfolio risk, as discussed in 
    Bhansali et al. (2024).
    """
    def __init__(self, cov_matrix):
        """
        Initialize the optimizer with a covariance matrix.
        :param cov_matrix: Covariance matrix of asset returns (ndarray or DataFrame)
        """
        self.cov = np.array(cov_matrix)
        self.n = len(self.cov)

    def _get_risk_contribution(self, weights):
        """Calculate the absolute Risk Contribution of each asset."""
        p_vol = np.sqrt(weights.T @ self.cov @ weights)
        marginal_risk_con = (self.cov @ weights) / p_vol
        return weights * marginal_risk_con

    def _objective(self, weights):
        """Objective function: minimize the variance of risk contributions."""
        risk_con = self._get_risk_contribution(weights)
        target = np.mean(risk_con)
        return np.sum(np.square(risk_con - target))

    def solve(self):
        """Solve for optimal ERC weights using SLSQP optimizer."""
        cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1.0})
        bounds = tuple((0.0, 1.0) for _ in range(self.n))
        init_w = np.array([1.0 / self.n] * self.n)

        res = minimize(self._objective, init_w, method='SLSQP', 
                       constraints=cons, bounds=bounds, tol=1e-9)
        return res.x
