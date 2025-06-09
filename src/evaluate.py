from stable_baselines3 import PPO
from market_env import MarketEnv
import pandas as pd

def evaluate():
    df = pd.read_csv("data/binance_tick_data.csv")
    env = MarketEnv(df)
    model = PPO.load("models/ppo_market_maker")

    obs = env.reset()
    total_reward = 0
    steps = 0

    while True:
        action, _ = model.predict(obs)
        obs, reward, done, _ = env.step(action)
        total_reward += reward
        steps += 1
        if done:
            break

    print("✅ Evaluation complete")
    print(f"Total reward: {total_reward:.2f}")
    print(f"Steps: {steps}")
    print(f"Average reward per step: {total_reward/steps:.5f}")

    # Save trade log
    log_df = pd.DataFrame(env.trade_log)
    log_df.to_csv("data/trade_log.csv", index=False)
    print("📁 Trade log saved to data/trade_log.csv")


if __name__ == "__main__":
    evaluate()
