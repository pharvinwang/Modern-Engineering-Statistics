# W10_anova_engineering.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

st.set_page_config(layout="wide")
st.title("第 10 週｜變異數分析：多方案工程比較")
st.caption("📘 教科書第 9 章（9.1–9.4）")

st.markdown("""
工程現場很少只有兩個方案。

👉 排水配置 A、B、C  
👉 材料來源 1、2、3  
👉 施工工法甲、乙、丙  

這時候，一個一個做 t 檢定是不對的。
""")

# =================================================
# A. 工程情境
# =================================================
st.subheader("一、工程比較情境")

case = st.selectbox(
    "選擇工程案例",
    ["坡地排水配置比較", "不同工法施工時間", "材料來源品質差異"]
)

np.random.seed(42)

# =================================================
# B. 模擬工程資料
# =================================================
if case == "坡地排水配置比較":
    unit = "mm"
    group_A = np.random.normal(3.2, 0.4, 20)
    group_B = np.random.normal(2.9, 0.4, 20)
    group_C = np.random.normal(2.5, 0.4, 20)
    ylabel = "坡面位移"

elif case == "不同工法施工時間":
    unit = "分鐘"
    group_A = np.random.normal(30, 3, 25)
    group_B = np.random.normal(27, 3, 25)
    group_C = np.random.normal(26, 3, 25)
    ylabel = "施工時間"

else:
    unit = "合格率"
    group_A = np.random.normal(0.88, 0.03, 30)
    group_B = np.random.normal(0.91, 0.03, 30)
    group_C = np.random.normal(0.93, 0.03, 30)
    ylabel = "品質指標"

# =========================================
