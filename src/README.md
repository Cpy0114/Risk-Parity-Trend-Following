# Risk Parity with Trend-Following Filter

This project is an empirical exploration based on the research paper **"Risk Parity with Trend-Following" (Bhansali et al., 2024)**. It investigates the performance of the Equal Risk Contribution (ERC) strategy and its robustness when integrated with Trend-Following filters, particularly during regime shifts like the 2022 market downturn.

## Research Context
Traditional Risk Parity strategies often struggle during periods of positive stock-bond correlation and synchronized asset sell-offs. This project replicates and extends the framework proposed by Bhansali et al. (2024), exploring how adding **Trend-Following** signals (e.g., Moving Average filters) can mitigate drawdowns and enhance risk-adjusted returns by reducing exposure to assets in clear downtrends.

## Core Methodology

### 1. Equal Risk Contribution (ERC)
The objective is to find a weight vector $w$ such that the risk contribution (RC) from each asset is equalized. The RC of asset $i$ is defined as:

$$RC_i = w_i \frac{(\Sigma w)_i}{\sqrt{w^T \Sigma w}}$$

The optimization problem minimizes the variance of risk contributions across all assets.

### 2. Trend-Following Filter (Implementation)
Based on the paper's insights, the strategy applies a trend filter (e.g., SMA 200) to each asset class. If an asset's price falls below its trend, its risk allocation is tactically reduced or reallocated to defensive assets, addressing the "concentration of risk" issue during bear markets.

## Project Structure
* `src/`: Core Python modules including `RiskParityOptimizer` for ERC weight calculation.
* `notebooks/`: Comprehensive analysis, backtesting results, and performance visualizations.
* `data/`: Historical market data processing (Equities, Bonds, etc.).

## Key Features
* **Custom ERC Optimizer**: Built using `scipy.optimize` with long-only constraints
* **Regime-Specific Backtesting**: Comparative analysis of 60/40 vs. Risk Parity vs. RP + Trend
* **Risk Decomposition**: Visualizing marginal risk contributions across different market cycles

## Reference
Bhansali, J. D., et al. (2024). *Risk Parity with Trend-Following*. Long Tail Alpha.
