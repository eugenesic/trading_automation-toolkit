# Переменные и базовые типы данных - основа любого торгового скрипта

name = "Evgen"                      # str - имя трейдера
account_balance = 52370.80          # float - баланс USDT
position_size = 7                   # int - количество контрактов
is_market_bull = True               # bool - наш взгляд на рынок

# f-строки - главный инструмент трейдер для вывода
print(f"Трейдер: {name}")
print(f"Баланс: {account_balance:,.2f}")
print(f"Открыто контрактов: {position_size}")
print(f"Бычий рынок? -> {is_market_bull}")

# Пример расчета возможной прибыли
entry_price = 60150.0
current_price = 61500.0
profit = (current_price - entry_price) * position_size
print(f"Нереализованный PnL: ${profit:+.2f}")   # + перед числом показывает знак