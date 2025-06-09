from order_book import OrderBook

ob = OrderBook()
ob.add_order('buy', 100.0, 5)
ob.add_order('buy', 99.8, 10)
ob.add_order('sell', 100.2, 7)
ob.add_order('sell', 100.5, 6)

ob.display_top_levels()
print("Best Bid:", ob.best_bid())
print("Best Ask:", ob.best_ask())