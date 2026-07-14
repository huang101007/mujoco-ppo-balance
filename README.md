# MuJoCo 強化學習與高精度控制策略開發 🤖

本專案探討並實作基於 **MuJoCo** 物理引擎的強化學習 (Reinforcement Learning) 環境。透過 **PPO (Proximal Policy Optimization)** 演算法，結合客製化獎勵函數 (Custom Reward Function)，引導智能體達成高精度的倒立擺平衡控制。

## 專案展示以及學習曲線
https://drive.google.com/drive/folders/1hb6V_dmX2fuay1p0dMm5Bm-v8eSiY1Oa?usp=drive_link

## 專案動機與技術實作
* **專案動機**：結合過往力學與數位孿生專案經驗，決定自主從零建置，將物理動態與軟體演算法結合。
* **技術實作**：採用 `MuJoCo` 物理引擎與 `Gymnasium` 框架，結合 `Stable-Baselines3` 的 PPO 演算法進行動態平衡訓練。
* **問題解決**：針對預設獎勵機制導致的「系統抖動與偏移」問題，運用 OOP 繼承改寫底層 `gym.Wrapper`，自訂數學獎勵函數嚴格懲罰位置與角度偏移。
* **訓練成果**：歷經 3 萬步訓練，成功收斂出平滑的最佳控制策略，將物理限制成功轉化為軟體工程解方。

## 核心檔案說明
* `train_ppo.py`: 預設環境的 PPO 基礎訓練程式碼。
* `train_custom_reward.py`: 繼承 Wrapper 並實作客製化 Reward Function 的進階訓練程式碼。
* `plot_learning_curve.py`: 訓練數據視覺化腳本。
