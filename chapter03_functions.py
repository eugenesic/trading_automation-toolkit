# Функции - переиспользуем расчеты

def risk_amount(balance: float, risk_percent: float = 1.0) -> float:
    """Сколько денег ставить на сделку при риске risk_percent % от баланса"""
    return balance * risk_percent / 100
def position_size_usdt(entry: float, stop_loss: float, balance: float, risk_pct: float = 1.0) -> float:
    """Сколько USDT выделить под позицию, чтобы потерять не больше risk_pct %"""
    risk_per_coin = abs(entry - stop_loss)
    return risk_amount(balance, risk_pct) / risk_per_coin  * entry

# Пример использования
balance = 100000
print(f"Риск 1% = ${risk_amount(balance):.2f}")
print(f"Риск 0.5% = ${risk_amount(balance, 0.5):.2f}")

# Сколько можно открыть в лонг BTC с входом 60k и стопом 57k
size = position_size_usdt(entry = 60000, stop_loss = 57000, balance = balance, risk_pct = 1)
print(f"Размер позиции BTC при риске 1% = ${size:,.0f}")