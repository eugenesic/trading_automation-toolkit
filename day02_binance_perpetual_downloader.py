"""
Binance Perpetual Futures 1-minute OHLCV Downloader (2019 - сегодня)
"""

import requests
import pandas as pd
from datetime import datetime
import time
import os
from tqdm import tqdm

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36",
}

def download_symbol(symbol: str, start_year: int = 2019):
    base_url = "https://www.binance.com/fapi/v1/klines"
    all_data = []
    start_ts = int(datetime(start_year, 1, 1).timestamp() * 1000)
    limit = 1500

    print(f"[{symbol}] Скачиваем с {start_year} года...")
    pbar = tqdm(desc=symbol, unit="свечей")

    while True:
        params = {
            "symbol": symbol,
            "interval": "1m",
            "startTime": start_ts,
            "limit": limit
        }
        try:
            r = requests.get(base_url, params=params, headers=HEADERS, timeout=10)
            if r.status_code != 200:
                print(f"Ошибка {r.status_code}, ждём...")
                time.sleep(2)
                continue
            data = r.json()
            if not data or len(data) == 0:
                break

            all_data.extend(data)
            start_ts = data[-1][0] + 1  # следующая миллисекунда после последней свечи
            pbar.update(len(data))

            if len(data) < limit:
                break

        except Exception as e:
            print(f"Исключение: {e}")
            time.sleep(5)

    pbar.close()

    if not all_data:
        print(f"[{symbol}] Нет данных")
        return

    # Создаём DataFrame только один раз — после окончания скачивания
    df = pd.DataFrame(all_data, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_volume", "trades", 
        "taker_buy_base", "taker_buy_quote", "ignore"
    ])

    df = df[["open_time", "open", "high", "low", "close", "volume"]]
    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
    df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)

    os.makedirs("data", exist_ok=True)
    path = f"data/{symbol}_1m.parquet"
    df.to_parquet(path, compression="gzip")
    print(f"[{symbol}] Готово → {len(df):,} свечей → {path}")


if __name__ == "__main__":
    symbols = [
        "BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "BNBUSDT",
        "ADAUSDT", "DOGEUSDT", "1000PEPEUSDT", "LINKUSDT", "AVAXUSDT"
    ]

    for sym in symbols:
        try:
            download_symbol(sym)
            time.sleep(1)  # чтобы не получить бан
        except KeyboardInterrupt:
            print("Остановлено пользователем")
            break
        except Exception as e:
            print(f"Ошибка с {sym}: {e}")