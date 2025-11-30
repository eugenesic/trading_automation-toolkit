# Списки - храним вотчлист и цены

watchlist = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT"]
prices = [60842.5, 3421.0, 148.9, 518.0, 0.583]

print("Мой текущий вотчлист:")
print("-" * 30)
for symbol, price in zip(watchlist, prices):
    change_24h = 2.48 if symbol == "BTCUSDT" else 6.2 # просто пример
    print(f"{symbol:>8} | ${price:9,.2f} | 24h: +{change_24h}%")