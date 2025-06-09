# src/market_env.py
import numpy as np
import gym
from gym import spaces
from order_book import OrderBook

class MarketEnv(gym.Env):
    def __init__(self, df, max_spread=0.1):
        super().__init__()
        self.trade_log = []
        self.df = df
        self.idx = 0
        self.cash = 0
        self.position = 0
        self.ob = OrderBook()

        # Observations: [bid, ask, spread]
        self.observation_space = spaces.Box(low=0, high=100000, shape=(3,))
        # Actions: [-1, 0, 1] for spread adjustment
        self.action_space = spaces.Discrete(3)

    def reset(self):
        self.idx = 0
        self.ob = OrderBook()
        self.cash = 0
        self.position = 0
        self.trade_log = []  # reset log
        return self._get_state()


    def step(self, action):
        row = self.df.iloc[self.idx]
        bid, ask, vol = row['bid'], row['ask'], row['volume']
        mid = (bid + ask) / 2

        # Update LOB
        self.ob.add_order('buy', bid, vol)
        self.ob.add_order('sell', ask, vol)

        # Convert action
        spread_adj = {0: -0.01, 1: 0.0, 2: 0.01}[int(action)]
        buy_price = round(mid - 0.025 + spread_adj, 2)
        sell_price = round(mid + 0.025 + spread_adj, 2)

        # Simulate fills (you can improve this later!)
        fill_buy = np.random.rand() < 0.4  # 40% fill chance
        fill_sell = np.random.rand() < 0.4

        pnl = 0
        filled = []

        if fill_buy:
            self.position += 1
            self.cash -= buy_price
            filled.append(('buy', buy_price))

        if fill_sell and self.position > 0:
            self.position -= 1
            self.cash += sell_price
            pnl = sell_price - buy_price
            filled.append(('sell', sell_price))

        # Log trade step
        self.trade_log.append({
            'step': self.idx,
            'action': int(action),
            'buy_price': buy_price,
            'sell_price': sell_price,
            'filled': filled,
            'position': self.position,
            'cash': self.cash,
            'reward': pnl
        })

        # Still place the orders in the book
        self.ob.add_order('buy', buy_price, 1)
        self.ob.add_order('sell', sell_price, 1)

        self.idx += 1
        done = self.idx >= len(self.df)
        return self._get_state(), pnl, done, {}



    def _get_state(self):
        if self.idx >= len(self.df):
            return np.zeros(3)
        row = self.df.iloc[self.idx]
        spread = row['ask'] - row['bid']
        return np.array([row['bid'], row['ask'], spread])
