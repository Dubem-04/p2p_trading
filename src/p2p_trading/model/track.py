"""Keeps track of base currency prices and reference market rates.

Interactions:

1. Maintains running averages and historical moving windows for base pairs (e.g., USDT/USD, USD/NGN).
2. Supplies fair-market reference rates to strategies.spread_arbitrage to prevent
   trading on stale or off-market merchant quotes."""

class ReferencePriceTracker:
    """Tracks spot exchange rates to establish baseline market valuations."""
    def __init__(self, window_size: int = 50) -> None:
        self.window_size = window_size
        self._history: list[float] = []

    def update_price(self, price: float) -> None:
        """Register the latest tick and retain window bounds."""
        self._history.append(price)
        if len(self._history) > self.window_size:
            self._history.pop(0)

    @property
    def rolling_mean(self) -> float:
        """Compute the simple arithmetic moving average over the tracked window."""
        if not self._history:
            return 0.0
        return sum(self._history) / len(self._history)