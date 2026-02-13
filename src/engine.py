import numpy as np
import pandas as pd
from scipy.optimize import minimize

class RiskParityOptimizer:
    """
    實作 Equal Risk Contribution (ERC) 算法
    對應 CFRM 522 作業邏輯並參考 Bhansali (2024) 論文概念
    """
    def __init__(self, cov_matrix):
        """
        初始化優化器
        :param cov_matrix: 資產的共變異數矩陣 (DataFrame 或 ndarray)
        """
        self.cov = np.array(cov_matrix)
        self.n = len(self.cov)

    def _get_risk_contribution(self, weights):
        """計算資產的風險貢獻 (Risk Contribution)"""
        p_vol = np.sqrt(weights.T @ self.cov @ weights)
        marginal_risk_con = (self.cov @ weights) / p_vol
        return weights * marginal_risk_con

    def _objective(self, weights):
        """優化目標函數：最小化各資產風險貢獻之間的差異"""
        risk_con = self._get_risk_contribution(weights)
        # 目標是讓每個資產的風險貢獻趨於一致
        target = np.mean(risk_con)
        return np.sum(np.square(risk_con - target))

    def solve(self):
        """執行優化求解權重"""
        # 約束條件：權重總和為 1
        cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1.0})
        # 邊界條件：不允許放空 (Long-only)
        bounds = tuple((0.0, 1.0) for _ in range(self.n))
        init_w = np.array([1.0 / self.n] * self.n)

        res = minimize(self._objective, init_w, method='SLSQP', 
                       constraints=cons, bounds=bounds, tol=1e-9)
        return res.x
