# Управляющие конструкции - принимаем торговые решения

price_btc = 60842.5
sma_200 = 58200.0
rsi = 72

if price_btc < sma_200 * 0.95:
    decision = "STRONG BUY - цена сильно ниже тренда"
elif price_btc > sma_200 * 1.15:
    decision = "TOO EXPENSIVE - ждем откат"
elif rsi > 70:
    decision = "OVERBOUGHT - возможна коррекция"
elif rsi < 30:
    decision = "OVERSOLD - рассматриваем лонг"
else:
    decision = "HOLD / ждем более четких сигналов"

print(f"Текущая цена BTC: ${price_btc:,.1f}")
print(f"Решение робота: {decision}")