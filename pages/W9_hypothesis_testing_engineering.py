# W9_hypothesis_testing_engineering.py
# 查表導向版

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

st.set_page_config(layout="wide")
st.title("第 9 週｜假設檢定（查表導向版）")
st.caption("📘 教科書第 8 章｜重點：查表判斷拒絕域")

st.markdown("""
工程師經常要比較兩個方案：  
- 坡地改善前後  
- 新舊施工工法  
- 施工品質合格率  

今天我們不算 p-value，**自己查表決定拒絕域**。
""")

# =================================================
# A. 學習模式
# =================================================
st.sidebar.header("學習模式")
mode = st.sidebar.radio(
    "模式",
    ["🔍 查表練習模式（課堂）", "⚡ 自動驗證模式（課後）"]
)

# =================================================
# B. 工程案例
# =================================================
st.subheader("一、工程比較情境")
case = st.selectbox(
    "選擇工程案例",
    ["坡地改善前後", "新舊施工工法", "施工品質合格率"]
)

np.random.seed(42)

if case == "坡地改善前後":
    before = np.random.normal(3.2, 0.6, 40)
    after = np.random.normal(2.7, 0.6, 40)
    unit = "mm"
    H0 = "改善前後平均位移相同"
    H1 = "改善後平均位移較小"
elif case == "新舊施工工法":
    before = np.random.normal(28, 4, 35)
    after = np.random.normal(25, 4, 35)
    unit = "分鐘"
    H0 = "新舊工法平均施工時間相同"
    H1 = "新工法施工時間較短"
else:
    before = np.random.binomial(1, 0.88, 60)
    after = np.random.binomial(1, 0.94, 60)
    unit = "%"
    H0 = "兩工法合格率相同"
    H1 = "新工法合格率較高"

# =================================================
# C. 顯著水準
# =================================================
st.subheader("二、顯著水準")
alpha = st.selectbox("顯著水準 α", [0.10, 0.05, 0.01], index=1)

# =================================================
# D. 顯示自由度
# =================================================
df = len(before) + len(after) - 2
st.write(f"自由度 df = {df}")

# =================================================
# E. 查表輸入
# =================================================
st.subheader("三、查表判斷")

st.markdown("""
📘 依據自由度 df 和 α/2，  
請查 t 表得到臨界值 tα/2
""")

t_input = st.number_input("請輸入查到的 t 臨界值", value=2.0, step=0.01)

# =================================================
# F. 計算 t 統計量
# =================================================
if case != "施工品質合格率":
    mean_diff = np.mean(after) - np.mean(before)
    pooled_se = np.sqrt(np.var(before, ddof=1)/len(before) +
                        np.var(after, ddof=1)/len(after))
    t_stat = mean_diff / pooled_se
else:
    p1, p2 = np.mean(before), np.mean(after)
    p_pool = (sum(before)+sum(after))/(len(before)+len(after))
    t_stat = (p2-p1)/np.sqrt(p_pool*(1-p_pool)*(1/len(before)+1/len(after)))

st.write(f"t 統計量 = {t_stat:.3f}")

# =================================================
# G. 判斷拒絕域
# =================================================
st.subheader("四、工程判斷")

if t_stat > t_input:
    st.success("✅ t 值超過查表臨界值 → 拒絕 H₀\n工程差異是真的")
else:
    st.warning("⚠️ t 值未超過臨界值 → 無法拒絕 H₀\n差異可能只是誤差")

# =================================================
# H. 視覺化（平均差 + 拒絕域）
# =================================================
st.subheader("五、視覺化")

fig, ax = plt.subplots()
ax.bar(["改善前", "改善後"], [np.mean(before), np.mean(after)], color=["skyblue","orange"])
ax.axhline(np.mean(before)+t_input*np.std(before)/np.sqrt(len(before)), color="red", linestyle="--", label="拒絕域")
ax.set_ylabel(unit)
ax.set_title("平均差異與拒絕域示意")
ax.legend()
st.pyplot(fig)

# =================================================
# I. 工程反思
# =================================================
st.subheader("六、工程反思")

st.markdown("""
1. t 值 > 查表值，代表什麼？
2. 样本数增加，拒绝域會怎樣？
3. 為什麼統計告訴我們要保守，而不是算出絕對答案？
""")
st.info("📌 本週重點：查表→判斷→工程決策，p-value只是驗證，不是答案。")
