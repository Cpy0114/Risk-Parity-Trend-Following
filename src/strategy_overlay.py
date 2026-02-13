import numpy as np
import pandas as pd

class TrendFilter:
    """
    Implementation of tactical trend-following overlays.
    Ref: Bhansali et al. (2024) "Risk Parity with Trend-Following".
    """
    def __init__(self, prices):
        """
        :param prices: DataFrame of historical asset prices.
        """
        self.prices = prices

    def get_sma_signal(self, window=200):
        """
        Generate binary trend signals based on Simple Moving Average.
        Returns 1 if price > SMA (Bullish), 0 otherwise (Bearish).
        """
        sma = self.prices.rolling(window=window).mean()
        # Get the most recent signal
        signal = (self.prices > sma).astype(int).iloc[-1]
        return signal

    def apply_overlay(self, weights, signals):
        """
        Apply trend signals to Risk Parity weights.
        Reduces exposure to assets with bearish signals.
        """
        # A simple overlay: zero out weights for assets in a downtrend
        overlay_weights = weights * signals
        
        # Re-normalize to ensure weights sum to 1, or allocate to cash if needed
        if np.sum(overlay_weights) > 0:
            return overlay_weights / np.sum(overlay_weights)
        else:
            # If all assets are in a downtrend, stay in cash (represented by zeros)
            return overlay_weights
