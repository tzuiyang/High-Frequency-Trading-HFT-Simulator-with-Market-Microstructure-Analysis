from collections import defaultdict
import heapq

class OrderBook:
    def __init__(self):
        # Max-heap for bids, min-heap for asks
        self.bids = defaultdict(list)  # {price: [volumes]}
        self.asks = defaultdict(list)  # {price: [volumes]}
        self.bid_prices = []           # Max-heap (negated prices)
        self.ask_prices = []           # Min-heap (natural prices)

    def add_order(self, side, price, volume):
        if side == 'buy':
            heapq.heappush(self.bid_prices, -price)
            self.bids[price].append(volume)
        elif side == 'sell':
            heapq.heappush(self.ask_prices, price)
            self.asks[price].append(volume)

    def best_bid(self):
        while self.bid_prices:
            price = -self.bid_prices[0]
            if self.bids[price]:
                return price, sum(self.bids[price])
            heapq.heappop(self.bid_prices)
        return None, 0

    def best_ask(self):
        while self.ask_prices:
            price = self.ask_prices[0]
            if self.asks[price]:
                return price, sum(self.asks[price])
            heapq.heappop(self.ask_prices)
        return None, 0

    def display_top_levels(self, levels=5):
        print("Order Book Snapshot:")
        print("  ASK")
        for price in sorted(self.asks.keys())[:levels]:
            print(f"  {price:.2f} x {sum(self.asks[price])}")
        print("------")
        for price in sorted(self.bids.keys(), reverse=True)[:levels]:
            print(f"  {price:.2f} x {sum(self.bids[price])}")
        print("  BID")