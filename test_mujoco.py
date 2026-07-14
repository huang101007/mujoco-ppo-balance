import gymnasium as gym
import time

# 建立一個MuJoCo 內建的倒立擺環境
# render_mode="human" 表示我們要開啟視覺化視窗觀看結果
env = gym.make("InvertedPendulum-v5", render_mode="human")

# 初始化環境，準備開始模擬
observation, info = env.reset()

print("環境啟動成功！開始執行隨機動作測試")

# 讓環境執行1000個步驟
for _ in range(1000):
    # env.action_space.sample() 對倒立擺施加推力
    action = env.action_space.sample()
    
    # 執行動作，並取得環境回傳的各種資訊
    observation, reward, terminated, truncated, info = env.step(action)
    
    # 如果倒立擺倒下 (terminated) 或達到最大步數 (truncated)，就重新啟動環境
    if terminated or truncated:
        observation, info = env.reset()
        
    # 短暫暫停
    time.sleep(0.016)

# 結束模擬並關閉視窗
env.close()