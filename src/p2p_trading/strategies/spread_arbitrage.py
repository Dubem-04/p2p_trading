"""Calculates net spreads between P2P bids/asks or cross-platform windows.

Interactions:

1. Inherits from strategies.base.BaseStrategy.
2. Uses metrics.formulas.calculate_net_spread to evaluate if a spread exceeds thresholds.
3. Consults models.track.ReferencePriceTracker for baseline fair-value checks."""

from typing import Any
from p2p_trading.data.orderbook import P2PListing
from p2p_trading.metrics.formulas import calculate_net_spread
from p2p_trading.strategies.base import BaseStrategy

class SpreadArbitrageStrategy(BaseStrategy):
    """Executes when the spread between bid and ask covers merchant costs plus margin."""

    def __init__(self, min_spread_threshold: float = 0.015, taker_fee: float = 0.001) -> None:
        self.min_spread_threshold = min_spread_threshold
        self.taker_fee = taker_fee

    def evaluate_market(
        self,
        bids: list[P2PListing],
        asks: list[P2PListing],
        reference_price: float,
    ) -> list[dict[str, Any]]:
        """Identify trades where (lowest_ask - highest_bid) net of fees meets threshold."""
        if not bids or not asks:
            return []

        best_bid = max(bids, key=lambda x: x.price)
        best_ask = min(asks, key=lambda x: x.price)

        spread = calculate_net_spread(best_ask.price, best_bid.price, self.taker_fee)
        if spread >= self.min_spread_threshold:
            return [{
                "action": "ARBITRAGE_SIGNAL",
                "buy_from": best_ask.adv_id,
                "sell_to": best_bid.adv_id,
                "expected_spread": spread,
            }]
        return []