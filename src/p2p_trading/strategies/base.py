"""Abstract base class defining strategy behavior.

Interactions:

1. Defines abstract methods for evaluate_market.
2. Consumed by both backtest.engine.BacktestEngine (for historical evaluation)
   and execution.order_manager.OrderManager (for production signaling)."""

from abc import ABC, abstractmethod
from typing import Any
from p2p_trading.data.orderbook import P2PListing

class BaseStrategy(ABC):
   """Interface required for all P2P market-making and arbitrage strategies."""
   @abstractmethod
   def evaluate_market(
      self,
      bids: list[P2PListing],
      asks: list[P2PListing],
      reference_price: float,
   ) -> list[dict[str, Any]]:
      """Evaluate order book states and return a list of actionable order instructions."""
      pass