"""CLI entrypoints and argument parsing.

Interactions:

1. Parses parameters (fiat, crypto, capital, strategy configuration).
2. Instantiates either p2p_trading.backtest.engine.BacktestEngine or
   p2p_trading.execution.order_manager.OrderManager.
3. Routes results to p2p_trading.reporting.summary."""

import argparse
from p2p_trading.backtest.engine import BacktestEngine
from p2p_trading.reporting.summary import generate_summary_report
from p2p_trading.strategies.spread_arbitrage import SpreadArbitrageStrategy

def main() -> int:

    """Parse user terminal arguments and trigger execution workflows."""
    parser = argparse.ArgumentParser(description="P2P Trading System CLI")
    parser.add_argument("mode", choices=["backtest", "live"], help="Execution mode")
    parser.add_argument("--capital", type=float, default=10000.0, help="Starting balance")
    args = parser.parse_args()

    if args.mode == "backtest":
        strategy = SpreadArbitrageStrategy()
        engine = BacktestEngine(strategy=strategy, initial_capital=args.capital)
        results = engine.run(ticks=[])
        print(generate_summary_report(results))
return 0