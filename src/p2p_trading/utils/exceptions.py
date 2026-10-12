"""Domain-specific exceptions for P2P trading routines.

Interactions:

1. Raised across execution, connectors, and data when invariant rules fail."""

class P2PTradeError(Exception):
    """Base exception for all domain-specific errors."""
    pass

class EscrowTimeoutError(P2PTradeError):
    """Raised when an active counterparty fails to confirm fiat or release within SLA."""
    pass

class InvalidOrderBookDataError(P2PTradeError):
    """Raised when external scraped or queried data fails validation schemas."""
    pass