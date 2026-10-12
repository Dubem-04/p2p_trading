"""Top-level package CLI entrypoint.
Enables invocation via python -m p2p_trading. Delegates parsing directly to
p2p_trading.cli.commands."""

import sys
from p2p_trading.cli.commands import main

if name == "main":
    sys.exit(main())