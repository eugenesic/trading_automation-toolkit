# Строковые методы - красивый вывод в терминал и в телегу

signal = "strong buy on btc"
print(signal.title())       # Strong Buy On Btc
print(signal.upper())       # STRONG BUY ON BTC

symbol = "BTCUSDT"
price = 60842.5

# Выравнивание - важно для таблиц
print(f"{symbol:>10} | ${price:>10,.2f}")

# Форматирование для алертов
alert = f"BUY {symbol} at ${price:,.0f} - target 65k"
print(alert)