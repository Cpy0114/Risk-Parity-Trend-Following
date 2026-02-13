# Risk Parity with Trend-Following Filter

This project implements a **Risk Parity (ERC - Equal Risk Contribution)** portfolio optimization strategy in Python. To address the vulnerability of Risk Parity during synchronized asset sell-offs, a **Trend-Following (Momentum)** filter is integrated to enhance drawdown control and risk-adjusted returns.

## Research Context
This project is an empirical exploration based on the paper **"Risk Parity with Trend-Following" (Bhansali et al., 2024)**. 

The research investigates the vulnerability of traditional stock-bond risk-parity strategies during periods of positive correlation and simultaneous drawdowns (as seen in 2022). This implementation replicates and extends the paper's proposal: augmenting or replacing bonds with **Trend-Following** strategies to improve portfolio robustness and risk-adjusted returns, especially when considering carry and inflation-regime shifts.

## Core Methodology

### 1. Risk Parity (Equal Risk Contribution)
The goal is to allocate weights $w$ such that each asset contributes equally to the total portfolio risk. The risk contribution of asset $i$ is defined as:

$$RC_i = w_i \frac{(\Sigma w)_i}{\sqrt{w^T \Sigma w}}$$

We solve for optimal weights by minimizing the variance of risk contributions:
$$f(w) = \sum_{i=1}^n \sum_{j=1}^n (RC_i - RC_j)^2$$

### 2. Trend-Following Integration
To mitigate tail risk, the strategy employs a trend filter (e.g., Simple Moving Average). If an asset's price falls below its trend, its weight is reallocated to cash or diversified across remaining "in-trend" assets, reducing the portfolio's exposure during bear markets.

## Key Features
* **Risk Decomposition**: Analyzing marginal risk contributions across different asset classes (Equities, Bonds, Commodities)
* **Optimization Engine**: Custom implementation using `scipy.optimize` to solve for ERC weights
* **Backtesting Framework**: Robust evaluation of performance metrics including Sharpe Ratio and Maximum Drawdown
* **Dynamic Rebalancing**: Periodic weight adjustments based on rolling covariance matrices

## Project Structure
* `src/`
    * `engine.py`: Core `RiskParityOptimizer` class for Equal Risk Contribution weight calculation.
    * `strategy_overlay.py`: Tactical trend-following signals and portfolio rebalancing logic.
* `notebooks/`
    * `Research_Analysis.ipynb`: Full research pipeline including data ingestion, backtesting against Bhansali (2024) benchmarks, and performance visualization.

## Empirical Results & Conclusions
The implementation validates the core thesis of Bhansali et al. (2024) regarding the limitations of traditional Risk Parity in high-correlation regimes:

* **Drawdown Mitigation**: During the 2022 market downturn, the Trend-Following filter successfully reduced maximum drawdown by tactically de-risking asset classes with negative price momentum
* **Risk Un-clustering**: While traditional Risk Parity experienced "risk clustering" (all assets falling simultaneously), the tactical overlay helped maintain a more stable portfolio volatility profile
* **Bond-Trend Substitution**: The study confirms that when bonds fail as a diversifier due to rising inflation/rates, trend-following signals serve as an effective alternative for downside protection
* **Dynamic Rebalancing**: Regular tactical adjustments (e.g., 200-day SMA) significantly improved the Sharpe Ratio compared to static Equal Risk Contribution (ERC) strategies during volatile periods

## Future Enhancements
* Incorporate GARCH models for improved volatility forecasting
* Apply Black-Litterman model for tactical asset allocation overlays

## References
* Bhansali, J. D., Chang, L., Holdom, J., Johnson, M., & Suvak, C. (2024). *Risk Parity with Trend-Following*. Long Tail Alpha, LLC. [Available at SSRN](https://ssrn.com/abstract=4714859)
