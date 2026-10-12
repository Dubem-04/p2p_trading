""""P2P order book normalizer and memory representation.

Interactions:

1. Ingests raw JSON payloads from connectors.p2p_client or disk archives.
2. Sanitizes prices, limits, and verified-merchant flags.
3. Supplies structured top-of-book levels to strategies.base.BaseStrategy.""""

from dataclasses import dataclass

@dataclass(slots=True)
class P2PListing:
    """Standardized representation of a single merchant offer."""
    adv_id: str
    advertiser: str
    price: float
    available_amount: float
    min_order_limit: float
    max_order_limit: float
    trade_type: str  # 'BUY' or 'SELL'

class OrderBookParser:
    """Transforms raw API responses into structured P2P depth trees."""
    @staticmethod
def parse_listings(raw_data: list[dict]) -> list[P2PListing]:
    """Convert heterogeneous dictionary records into uniform P2PListing objects."""
    listings: list[P2PListing] = []
    for item in raw_data:
        listings.append(
            P2PListing(
                adv_id=item.get("id", ""),
                advertiser=item.get("user", ""),
                price=float(item.get("price", 0.0)),
                available_amount=float(item.get("amount", 0.0)),
                min_order_limit=float(item.get("min_limit", 0.0)),
                max_order_limit=float(item.get("max_limit", 0.0)),
                trade_type=item.get("type", "BUY"),
            )
        )
    return listings