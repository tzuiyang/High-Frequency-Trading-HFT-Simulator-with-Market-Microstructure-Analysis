# High-Frequency Trading (HFT) Simulator with Market Microstructure Analysis

## 📌 Project Overview

This project simulates a high-frequency trading environment with a realistic limit order book (LOB) to train and evaluate a reinforcement learning (RL) agent that acts as a market-making bot. The simulator allows for historical tick data ingestion, LOB reconstruction, strategy development, and performance evaluation. This mimics how real-world HFT firms like Citadel, Jump, and Jane Street train and test their trading bots.

---

## 🎯 Objectives

- Recreate a limit order book from real or simulated tick data.
- Implement a rule-based market-making strategy (SimpleMarketMaker).
- Build a custom OpenAI Gym environment (`MarketEnv`) for RL-based trading.
- Train an RL agent (PPO) to place limit orders and profit from the bid-ask spread.
- Track trade logs, simulate fills, and calculate PnL in a simulated environment.
- Visualize order placements vs market mid-price over time.
- Understand core market microstructure concepts (spread, mid-price, liquidity).

---

## ✅ Achievements

- ✅ A modular Python HFT simulator environment.
- ✅ Live replay of market tick data through a simulated LOB.
- ✅ PPO agent learns to place profitable limit orders over time.
- ✅ Realistic trade fill simulation with buy/sell order tracking.
- ✅ Visualization of orders, mid-prices, fills, cash, and position changes.
- ✅ Exportable trade logs for performance analysis.

---

## 🧠 Core Theories Used

### 📘 Limit Order Book (LOB)
- A real-time record of all buy (bid) and sell (ask) orders in the market.
- The agent can only act by placing orders into the book (like a market maker).

### 📘 Spread
- Spread = Ask Price - Bid Price.
- The agent profits when it buys low (bid) and sells high (ask).

### 📘 Mid Price
- Mid = (Bid + Ask) / 2.
- Used to center the agent’s quote placement.

### 📘 Liquidity Provision
- The agent provides liquidity by offering to buy/sell at favorable prices.
- It earns from the spread when both buy and sell orders are filled.

### 📘 Reinforcement Learning
- Agent interacts with environment through `MarketEnv`.
- Actions = where to place limit orders relative to mid-price.
- Rewards = profit (PnL) from filled orders.
- PPO (Proximal Policy Optimization) is used to train the agent to improve over time.

---

## 📈 Evaluation and Visualization

- Trade logs track every order placed and filled.
- Realized PnL is computed at each step.
- Jupyter notebook visualizes:
  - Mid-price trajectory
  - Agent’s placed orders
  - Which orders were filled
  - Cash/Position over time

---

## 🧪 Example Workflow

1. Generate or download tick data → `data/binance_tick_data.csv`
2. Train agent → `python src/train_rl_agent.py`
3. Evaluate agent → `python src/evaluate.py`
4. Visualize trades → Open `visualize_trades.ipynb`

---

## 🚀 Future Improvements

- Add more state features: order book depth, volatility, order flow imbalance
- Use continuous actions for more realistic price/volume quotes
- Model latency and network delays
- Train with live Binance WebSocket API
- Add multiple competing agents to simulate adversarial markets

---
