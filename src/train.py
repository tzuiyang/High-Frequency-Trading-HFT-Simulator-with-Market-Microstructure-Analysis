# src/train_rl_agent.py

from stable_baselines3 import PPO
from market_env import MarketEnv
import pandas as pd
import os

def train():
    df = pd.read_csv("data/binance_tick_data.csv")
    env = MarketEnv(df)

    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=20000)

    os.makedirs("models", exist_ok=True)
    model.save("models/ppo_market_maker")
    print("✅ RL model saved to models/ppo_market_maker")

if __name__ == "__main__":
    train()
