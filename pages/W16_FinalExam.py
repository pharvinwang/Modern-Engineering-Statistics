# W16_FinalExam.py
# 期末考互動頁（整合 1–15 週）

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import t, f
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

st.set_page_config(layout="wide")
st.title("第 16 週｜期末考互動頁（整合前 1–15 週）")
st.caption("📘 目標：綜合運用統計工具做工程判斷")

st.markdown("""
本週為期末考週，學生將運用：
- 抽樣與信賴區間
- 假設檢定
- 單因子 ANOVA、多重比較
- 線性與多項式迴歸
- 工程判斷與決策

🔹 課堂可用實際案例資料操作
""")

# =================================================
# A. 選擇考題類型
# =================================================
st.subheader("一、選擇考題類型")
task = st.selectbox(
    "考題類型",
    ["信賴區間 / 假設檢定", "ANOVA / 多重比較", "迴歸分析", "工程判斷綜合"]
)

# =================================================
# B. 信賴區間 / 假設檢定
# =================================================
if task == "信賴區間 / 假設檢定":
    st.markdown("### 信賴區間 / t 檢定題")
    n = st.number_input("樣本數 n", min_value=5, max_value=50, value=12)
    df = n-1
    xbar = st.number_input("樣本平均 x̄", value=2.5)
    s = st.number_input("樣本標準差 s", value=0.5)
    alpha = st.selectbox("顯著水準 α", [0.10,0.05,0.01], index=1)
    t_input = st.number_input("請輸入 t 查表值 tα/2, df", value=2.0, step=0.01)
    lower = xbar - t_input*s/np.sqrt(n)
    upper = xbar + t_input*s/np.sqrt(n)
    st.write(f"信賴區間為 [{lower:.3f}, {upper:.3f}]")

# =================================================
# C. ANOVA / 多重比較
# =================================================
elif task == "ANOVA / 多重比較":
    st.markdown("### 多方案比較")
    group_A = np.random.normal(3.2,0.4,20)
    group_B = np.random.normal(2.9,0.4,20)
    group_C = np.random.normal(2.5,0.4,20)
    groups = [group_A, group_B, group_C]
    st.write("各方案樣本平均：", [np.mean(g) for g in groups])
    F_stat = np.var([np.mean(g) for g in groups], ddof=1)/np.mean([np.var(g, ddof=1) for g in groups])
    F_input = st.number_input("請輸入 F 臨界值 Fα(df1, df2)", value=3.10, step=0.01)
    if F_stat > F_input:
        st.success("拒絕 H0，至少一方案不同")
    else:
        st.warning("無法拒絕 H0")

# =================================================
# D. 迴歸分析
# =================================================
elif task == "迴歸分析":
    st.markdown("### 迴歸分析題")
    X = np.linspace(50,200,25).reshape(-1,1)
    Y = 0.01*X**2 -0.5*X + 10 + np.random.normal(0,2,25)
    degree = st.slider("多項式階數", 1, 3, 2)
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly,Y)
    Y_pred = model.predict(X_poly)
    r2 = r2_score(Y,Y_pred)
    st.write(f"迴歸係數 b0~b{degree}:", np.round(np.append(model.intercept_, model.coef_),3))
    st.write(f"R² = {r2:.3f}")
    fig, ax = plt.subplots()
    ax.scatter(X,Y,color='blue',label='實測值')
    ax.plot(X,Y_pred,color='red',label=f'{degree}次多項式擬合')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()
    st.pyplot(fig)

# =================================================
# E. 工程判斷綜合
# =================================================
else:
    st.markdown("### 綜合工程判斷題")
    st.markdown("""
1. 使用抽樣分配與信賴區間評估坡地沉降是否安全  
2. 使用 ANOVA / 多重比較選擇最佳施工方案  
3. 使用迴歸分析預測降雨對坡地沉降的影響  
4. 撰寫工程判斷建議  
""")
    st.info("🔹 本週重點：整合前 1–15 週所有統計工具 → 做工程決策")

