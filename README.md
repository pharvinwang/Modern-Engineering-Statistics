# 工程統計互動課程（Engineering Statistics Interactive App）

## 專案概述
整合 1–16 週課程內容，學生可以透過互動操作了解統計概念與工程應用。

課程重點：
- 描述統計與資料探索
- 機率與分布
- 抽樣分配與信賴區間
- 假設檢定與單因子 ANOVA
- 多重比較與實驗設計
- 統計製程管制（SPC）
- 線性與非線性迴歸分析
- 期中與期末綜合實作

## 使用方法

1. 建議在虛擬環境安裝依賴：
```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

2. 啟動 Streamlit：
```bash
streamlit run app.py
```

3. 進入課程互動頁：
- 左側選單選擇週次
- 互動操作工程資料、拉動參數、查表計算

## 工程資料範例
- data/sample_rainfall.csv
- data/slope_displacement.csv
- data/construction_quality.csv

## 注意事項
- 查表練習週（第6、7、8、9、10、11週）請學生手動輸入 t/F 臨界值
- 可選查表週（第12–16週）程式可自動計算，但仍可手動練習
- 每週互動頁與教科書章節對應
