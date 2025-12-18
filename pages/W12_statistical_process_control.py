# W12_statistical_process_control.py

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("第 12 週｜統計製程管制（SPC）")
st.caption("📘 教科書第 12 章｜重點：管制圖與工程品質")

st.markdown("""
統計製程管制是把工程品質量化、可視化。  
學生將看到偏差何時超過控制界限，並學會工程判斷。
""")

# =================================================
# A. 工程案例選擇
# =================================================
st.subheader("一、工程案例")
case = st.selectbox(
    "選擇工程案例",
    ["坡地位移", "單場降雨量", "施工品質合格率"]
)

np.random.seed(42)

# =================================================
# B. 生成或上傳資料
# =================================================
st.subheader("二、資料來源")
upload = st.file_uploader("可上傳 CSV，第一欄為測量值（可選）", type="csv")

if upload is not None:
    df = pd.read_csv(upload)
    data = df.iloc[:,0].values
else:
    if case == "坡地位移":
        data = np.random.normal(3.0, 0.5, 25)
        unit = "mm"
    elif case == "單場降雨量":
        data = np.random.normal(120, 25, 25)
        unit = "mm"
    else:
        data = np.random.binomial(1, 0.92, 25)
        unit = "%"

# =================================================
# C. 設定管制圖參數
# =================================================
st.subheader("三、設定管制圖參數")

if case != "施工品質合格率":
    center = np.mean(data)
    sigma = np.std(data, ddof=1)
    LCL = st.number_input("下控制界限 LCL", value=center-3*sigma)
    UCL = st.number_input("上控制界限 UCL", value=center+3*sigma)
else:
    center = np.mean(data)
    p = center
    n = len(data)
    LCL = st.number_input("下控制界限 LCL", value=max(0,p-3*np.sqrt(p*(1-p)/n)))
    UCL = st.number_input("上控制界限 UCL", value=min(1,p+3*np.sqrt(p*(1-p)/n)))

st.write(f"中心線 CL = {center:.3f}, LCL = {LCL:.3f}, UCL = {UCL:.3f}")

# =================================================
# D. 繪製管制圖
# =================================================
st.subheader("四、管制圖視覺化")

fig, ax = plt.subplots()
ax.plot(data, marker='o', linestyle='-', color='blue')
ax.axhline(center, color='green', linestyle='--', label="CL")
ax.axhline(UCL, color='red', linestyle='--', label="UCL")
ax.axhline(LCL, color='red', linestyle='--', label="LCL")

ax.set_ylabel(f"{unit}")
ax.set_xlabel("樣本編號")
ax.set_title(f"{case} 管制圖")
ax.legend()
st.pyplot(fig)

# =================================================
# E. 判斷偏差
# =================================================
st.subheader("五、工程判斷")

out_of_control = np.where((data > UCL) | (data < LCL))[0]

if len(out_of_control) > 0:
    st.warning(f"⚠️ 有 {len(out_of_control)} 個樣本超出控制界限: {out_of_control}")
else:
    st.success("✅ 所有樣本在控制界限內，工程過程穩定")

# =================================================
# F. 工程反思
# =================================================
st.subheader("六、工程反思")

st.markdown("""
1. 如果某些點超過控制界限，你會怎麼調整工程？  
2. 管制圖如何幫助工程持續改進？  
3. 計量資料 vs 計數資料，控制界限計算有什麼差異？
""")

st.info("""
📌 本週重點：管制圖 → 判斷 → 工程調整  
📌 前 1–11 週概念累積，統計轉化為工程決策
""")
