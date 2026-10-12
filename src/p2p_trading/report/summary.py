"""Formats simulation or live session statistics into tabular summaries.

Interactions:

1. Accepts trade ledgers produced by backtest.engine or execution.order_manager.
2. Invokes metrics.formulas to generate risk and return figures.
3. Emits formatted strings for display by cli.commands."""

from typing import Any

def generate_summary_report(results: dict[str, Any]) -> str:
    """Convert engine execution statistics into a clean text-based report."""
    return (
    "\n"
    "         TRADING RUN SUMMARY            \n"
    "\n"
    f"Initial Capital: {results.get('initial_capital', 0.0):,.2f}\n"
    f"Final Capital:   {results.get('final_capital', 0.0):,.2f}\n"
    f"Total PnL:       {results.get('total_pnl', 0.0):,.2f}\n"
    f"Trades Taken:    {results.get('total_trades', 0)}\n"
    "========================================"
    )