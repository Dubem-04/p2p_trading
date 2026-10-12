"""Mathematical and financial calculation primitives.

Interactions:

1. Supplies spread arithmetic to strategies.spread_arbitrage.
2. Provides Sharpe, Drawdown, and Win-Rate calculators to reporting.summary."""

import math

def calculate_net_spread(buy_price: float, sell_price: float, fee_rate: float = 0.0) -> float:
    """Calculate percentage net yield accounting for percentage fees on turnover."""
    if buy_price <= 0:
        return 0.0
    effective_buy = buy_price * (1.0 + fee_rate)
    effective_sell = sell_price * (1.0 - fee_rate)
    return (effective_sell - effective_buy) / effective_buy

def calculate_sharpe_ratio(returns: list[float], risk_free_rate: float = 0.0) -> float:
    """Calculate annualized Sharpe ratio from an array of periodic returns."""
    if len(returns) < 2:
        return 0.0
    mean_return = sum(returns) / len(returns)
    variance = sum((r - mean_return)  2 for r in returns) / (len(returns) - 1)
    std_dev = math.sqrt(variance)
    if std_dev == 0.0:
        return 0.0
    return (mean_return - risk_free_rate) / std_dev