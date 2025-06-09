import ccxt
import pandas as pd
import time

exchange = ccxt.binance()
symbol = 'BTC/USDT'
data = []

for _ in range(100):
    orderbook = exchange.fetch_order_book(symbol)
    timestamp = pd.Timestamp.now()
    bid = orderbook['bids'][0][0] if orderbook['bids'] else None
    ask = orderbook['asks'][0][0] if orderbook['asks'] else None
    volume = orderbook['bids'][0][1] if orderbook['bids'] else None
    data.append([timestamp, bid, ask, volume])
    time.sleep(0.1)

df = pd.DataFrame(data, columns=["timestamp", "bid", "ask", "volume"])
df.to_csv("data/binance_tick_data.csv", index=False)