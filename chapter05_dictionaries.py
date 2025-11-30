# Словари - храним открытые позиции

positions = {
    "BTCUSDT": {"size": 0.842, "entry": 59200.0, "current": 60842.5},
    "ETHUSDT": {"size": 8.5, "entry": 3350.0, "current": 3421.0},
    "SOLUSDT": {"size": 42.0, "entry": 142.0, "current": 148.9}
}

total_pnl = 0.0
print("Открытые позиции:")
for symbol, data in positions.items():
    pnl = (data["current"] - data["entry"]) * data["size"]
    total_pnl += pnl
    print(f"{symbol:>8} -> ${pnl:+8.2f}")

print(f"Общий, нереализованный PnL: ${total_pnl:+.2f}")