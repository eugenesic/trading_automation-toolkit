A universal `.gitignore` has been added to exclude heavy, binary, and unnecessary files from version control across all directories. This ensures clean, efficient commits and prevents bloating the repository with large assets like datasets, binaries, logs, and cache files.

[![Stars](https://img.shields.io/github/stars/eugenesic/trading_automation-toolkit?style=social)](https://github.com/eugenesic/trading_automation-toolkit/stargazers)
[![Forks](https://img.shields.io/github/forks/eugenesic/trading_automation-toolkit?style=social)](https://github.com/eugenesic/trading_automation-toolkit/network/members)
[![Watchers](https://img.shields.io/github/watchers/eugenesic/trading_automation-toolkit?style=social)](https://github.com/eugenesic/trading_automation-toolkit/watchers)

# Trading Automation Toolkit

Public logbook of my 3-year grind  
**From complete zero → OpenAI / Anthropic / Jane Street / Citadel engineer**  
100 % through algorithmic trading & open-source

---

## ✅ Day 1 – Completed
Finished chapters 0–6 of “Automate the Boring Stuff with Python”  
Covered: variables → flow control → functions → lists → dicts → strings  
All examples are real trading-related (risk management, watchlists, PnL, signals)

---

## ✅ Day 2 – Completed
One command → entire history of top-20 coins  
→ Saved as fast Parquet files

---

## ✅ Day 3 – Completed
**LightBT: The simplest yet robust backtester (December 2025 edition)**

- Pure `pandas` + `NumPy`, no external dependencies
- Backtests **3+ million rows** (5+ years of 1-minute BTCUSDT data) in **under 1.5 seconds**
- Fully overflow-safe: uses `float64`, bounds checks, and finite value guards
- No warnings, no crashes — even with unrealistic equity growth
- Built-in SMA crossover strategy with equity curve, trades, CAGR, and Sharpe ratio

> ⚠️ **Note:** This version runs **entirely on CPU**.  
> It relies on highly optimized vectorized operations with `pandas` and `NumPy`, but **does not use GPU acceleration**.  
> Future versions may support `cudf`, `cupy`, or `numba` for GPU compute.

### Features:
- ✅ Vectorized signal generation (`SMA crossover`)
- ✅ Memory-efficient `.parquet` data loading
- ✅ Realistic taker fees (0.05%)
- ✅ Leverage support (e.g. 10x, 20x)
- ✅ Trade logging and equity tracking
- ✅ Robust metrics: CAGR, Sharpe, total return

### Performance:
- Tested on 3M+ rows (1-minute data)
- Execution time: ~1.2–1.5 sec on modern CPU
- 100% CPU-based — no GPU required

---

**Star if you’re also building your career in public**  
**Watch the repo to follow daily progress**

Current streak: Day 3