import matplotlib.pyplot as plt


iterations = list(range(1, 16))
ep_rew_mean = [
    6.35, 7.65, 12.3, 18.4, 24.7, 
    33.4, 41.5, 50.3, 57.5, 66.2, 
    75.1, 86.2, 98.9, 115.0, 131.0
]

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False


plt.figure(figsize=(10, 6))

plt.plot(iterations, ep_rew_mean, marker='o', linestyle='-', color='#1f77b4', linewidth=2, markersize=6)

#設定標題與XY軸標籤
plt.title('PPO演算法Learning Curve', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('訓練階段 (Iterations)', fontsize=14)
plt.ylabel('平均回合獎勵 (ep_rew_mean)', fontsize=14)

#顯示網格
plt.grid(True, linestyle='--', alpha=0.7)

#將X軸刻度設定為整數
plt.xticks(iterations)

plt.tight_layout()
plt.show()