# W11_multiple_comparison_design.py
# 多重比較與實驗設計查表版

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f, t

st.set_page_config(layout="wide")
st.title("第 11 週｜多重比較與工程實驗設計（查表版）")
st.caption("📘 教科書第 11 章｜重點：查表判斷組間差異")

# =================================================
# A. 學習模式
# =================================================
st.sidebar.header("學習模式")
mode = st.sidebar.radio(
    "模式",
    ["🔍 查表練習模式（課堂）", "⚡ 自動驗證模式（課後）"]
)

st.markdown("""
ANOVA 告訴你至少有一個方案不同，  
但你不知道是誰。  
多重比較告訴你「哪個方案差異顯著」。
""")

# =================================================
# B. 工程案例
# =================================================
st.subheader("一、工程案例")

case = st.selectbox(
    "選擇工程情境",
    ["坡地排水方案比較", "不同施工工法", "材料來源品質差異"]
)

np.random.seed(42)

if case == "坡地排水方案比較":
    unit = "mm"
    group_A = np.random.normal(3.2, 0.4, 20)
    group_B = np.random.normal(2.9, 0.4, 20)
    group_C = np.random.normal(2.5, 0.4, 20)
    ylabel = "坡面位移"
elif case == "不同施工工法":
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

groups = [group_A, group_B, group_C]
group_names = ["A","B","C"]

# =================================================
# C. 顯著水準
# =================================================
st.subheader("二、顯著水準")
alpha = st.selectbox("顯著水準 α", [0.10,0.05,0.01], index=1)

# =================================================
# D. 計算 df1, df2
# =================================================
k = len(groups)
n_list = [len(g) for g in groups]
N = sum(n_list)
df1 = k-1
df2 = N-k
st.write(f"自由度 df1 = {df1}, df2 = {df2}")

# =================================================
# E. 查表輸入（多重比較） 
# =================================================
st.subheader("三、查表判斷")
st.markdown("""
請查 Tukey HSD 或 Bonferroni 臨界值表，輸入 q 或臨界差距
""")
critical_diff = st.number_input("請輸入查表得到的臨界差距", value=0.3, step=0.01)

# =================================================
# F. 計算組間平均差
# =================================================
st.subheader("四、組間差異")

means = [np.mean(g) for g in groups]
diff_matrix = np.zeros((k,k))
for i in range(k):
    for j in range(i+1, k):
        diff = abs(means[i]-means[j])
        diff_matrix[i,j] = diff
        diff_matrix[j,i] = diff

st.write("組間平均差矩陣")
st.write(diff_matrix)

# =================================================
# G. 判斷哪些組差異顯著
# =================================================
st.subheader("五、工程判斷")

significant_pairs = []
for i in range(k):
    for j in range(i+1, k):
        if diff_matrix[i,j] > critical_diff:
            significant_pairs.append(f"{group_names[i]} vs {group_names[j]}")

if significant_pairs:
    st.success("✅ 以下組差異顯著")
    for pair in significant_pairs:
        st.write(pair)
else:
    st.warning("⚠️ 無顯著差異組")

# =================================================
# H. 視覺化
# =================================================
st.subheader("六、視覺化")

fig, ax = plt.subplots()
ax.boxplot(groups, labels=group_names)
ax.set_ylabel(f"{ylabel} ({unit})")
ax.set_title("各方案資料分布")
st.pyplot(fig)

# =================================================
# I. 工程反思
# =================================================
st.subheader("七、工程反思")

st.markdown("""
1. 哪些組之間差異明顯？  
2. 統計顯著 ≠ 工程重要，如何判斷？  
3. 查表的過程為什麼很重要？  
""")

st.info("""
📌 本週重點：查表→判斷→決策  
📌 ANOVA 只是告訴你「至少有一組不同」  
📌 多重比較告訴你「差在哪裡」  
""")
