import pandas as pd
from order_book import OrderBook

def simulate_from_csv(csv_path, step_print=10):
    df = pd.read_csv(csv_path)
    ob = OrderBook()

    for i, row in enumerate(df.itertuples()):
        timestamp = row.timestamp
        bid = row.bid
        ask = row.ask
        volume = row.volume

        # Feed orders into the book
        ob.add_order('buy', bid, volume)
        ob.add_order('sell', ask, volume)

        if i % step_print == 0:
            print(f"\n[Time: {timestamp}]")
            ob.display_top_levels()

if __name__ == "__main__":
    simulate_from_csv("data/binance_tick_data.csv") 
