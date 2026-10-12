"""Discrete event simulation runner for backtesting P2P strategies.

Interactions:

1. Ingests structured historical tick series from data.orderbook.
2. Passes snapshot slices to strategies.base.BaseStrategy.
3. Simulates fill times, capital lockups, and counterparty release delays.
4. Outputs completed execution logs to metrics.formulas and reporting.summary."""

from typing import Any
from p2p_trading.strategies.base import BaseStrategy

class BacktestEngine:
    """Simulates market interaction over static or replay feeds."""

    def __init__(self, strategy: BaseStrategy, initial_capital: float = 10_000.0) -> None:
        self.strategy = strategy
        self.capital = initial_capital
        self.trades: list[dict[str, Any]] = []

    def run(self, ticks: list[dict[str, Any]]) -> dict[str, Any]:
        """Simulate sequential ticks and record execution outcomes."""
        return {
            "initial_capital": self.capital,
            "final_capital": self.capital,
            "total_trades": len(self.trades),
            "total_pnl": 0.0,
        }