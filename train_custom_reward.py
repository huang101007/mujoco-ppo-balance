import gymnasium as gym
import numpy as np
from stable_baselines3 import PPO
import os

#運用OOP繼承並改寫環境
class PrecisionPendulumWrapper(gym.Wrapper):
    def __init__(self, env):
        super().__init__(env)

    def step(self, action):
        #先讓原始環境執行一步，取得原始資料
        observation, reward, terminated, truncated, info = self.env.step(action)
        
        #提取狀態矩陣中的數值
        x_pos = observation[0]      #車子在X軸的位置
        theta_angle = observation[1]     #擺錘的傾斜角度
        
        #實作Reward Function
        #設定權重，對角度偏移給予重度懲罰(2.0)，位置偏移給予輕度懲罰(0.5)
        custom_reward = 1.0 - (0.5 * abs(x_pos)) - (2.0 * abs(theta_angle))
        
        #回傳篡改後的reward給AI演算法
        return observation, custom_reward, terminated, truncated, info

#建立儲存資料夾
models_dir = "models_custom"
if not os.path.exists(models_dir):
    os.makedirs(models_dir)

#建立環境並套用我們的Wrapper
base_env = gym.make("InvertedPendulum-v5")
custom_env = PrecisionPendulumWrapper(base_env)

#啟動PPO進行訓練(這次訓練30,000步，讓它有時間適應新規則)
print("開始進行高精度平衡訓練...")
model = PPO("MlpPolicy", custom_env, verbose=1)
model.learn(total_timesteps=30000)

#儲存進階模型
model_path = f"{models_dir}/ppo_precision_pendulum"
model.save(model_path)
print(f"進階訓練完成！模型儲存至：{model_path}.zip")

custom_env.close()