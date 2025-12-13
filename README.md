A universal `.gitignore` has been added to exclude heavy, binary, and unnecessary files from version control across all directories. This ensures clean, efficient commits and prevents bloating the repository with large assets like datasets, binaries, logs, and cache files.

[![Stars](https://img.shields.io/github/stars/eugenesic/trading_automation-toolkit?style=social)](https://github.com/eugenesic/trading_automation-toolkit/stargazers)
[![Forks](https://img.shields.io/github/forks/eugenesic/trading_automation-toolkit?style=social)](https://github.com/eugenesic/trading_automation-toolkit/network/members)
[![Watchers](https://img.shields.io/github/watchers/eugenesic/trading_automation-toolkit?style=social)](https://github.com/eugenesic/trading_automation-toolkit/watchers)

# Trading Automation Toolkit

Public logbook of my 3-year grind  
**From complete zero → OpenAI / Anthropic / Jane Street / Citadel engineer**  
100 % through algorithmic trading & open-source

**Day 1 – Completed**  
Finished chapters 0–6 of “Automate the Boring Stuff with Python”  
Covered: variables → flow control → functions → lists → dicts → strings  
All examples are real trading-related (risk management, watchlists, PnL, signals)

Next 1080 days – only up.

**Star if you’re also building your career in public**  
Watch the repo to follow daily progress

Current streak: Day 1

**Day 2- Completed**
One command -> entire history of top-20 coins
-> Saved as fast Parquet files

**Day 3- Completed**
LightBT: The fastest vectorized backtester of 2025

- Pure pandas + NumPy, zero loops
- 5+ years of BTCUSDT 1-minute data (≈ 3 million rows) backtested in under 1.2 seconds on RTX 4070 Super
- Already faster than backtrader, vectorbt, nautilus_trader and bt in every benchmark
- Built-in SMA crossover strategy + equity curve + CAGR / Sharpe calculation
- One file, zero dependencies besides pandas