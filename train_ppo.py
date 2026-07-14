import gymnasium as gym
from stable_baselines3 import PPO
import os

#建立一個資料夾，用來儲存訓練好的AI模型參數
models_dir = "models"
if not os.path.exists(models_dir):
    os.makedirs(models_dir)

# 刻意不加上 render_mode="human"，因為渲染 3D 畫面會極大程度佔用運算資源。
# 為了演算法訓練速度，所以在背景默默進行矩陣運算即可。
env = gym.make("InvertedPendulum-v5")

# "MlpPolicy" 代表使用Multi-Layer Perceptron作為神經網路架構
# verbose=1 會讓系統在終端機中印出詳細的訓練日誌與記憶體使用狀況
model = PPO("MlpPolicy", env, verbose=1)

print("開始訓練 PPO 模型...")

# 我們先設定讓它在環境中嘗試20,000 步
model.learn(total_timesteps=20000)

#儲存模型
model_path = f"{models_dir}/ppo_pendulum"
model.save(model_path)
print(f"訓練完成！模型已儲存至：{model_path}.zip")

env.close()