# W13_Regression.py
# 第 13 週｜線性回歸與單/多變量回歸互動頁（修正版）

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

st.set_page_config(layout="wide")
st.title("第 13 週｜線性回歸與單/多變量回歸")
st.caption("📘 教科書第 10 章｜重點：迴歸分析與工程預測")

# 一、工程案例選擇
case = st.selectbox("選擇工程案例", ["坡地位移預測（單變量）", "施工時間預測（多變量）"])
np.random.seed(42)

# 二、資料來源（可上傳 CSV）
upload = st.file_uploader("可上傳 CSV，X1,X2,Y", type="csv")
if upload is not None:
    df = pd.read_csv(upload)
    X = df.iloc[:, :-1].values
    Y = df.iloc[:, -1].values
else:
    if case == "坡地位移預測（單變量）":
        X = np.random.uniform(50, 200, 25)
        Y = 2 + 0.01*X + np.random.normal(0,0.2,25)
    else:
        X1 = np.random.uniform(5,15,25)
        X2 = np.random.uniform(1,5,25)
        Y = 20 + 1.5*X1 + 2.0*X2 + np.random.normal(0,2,25)
        X = np.column_stack((X1,X2))

# 保證單變量 X 是二維
if X.ndim == 1:
    X = X.reshape(-1,1)

# 建立迴歸模型
model = LinearRegression()
model.fit(X, Y)
Y_pred = model.predict(X)

# 確保 Y, Y_pred 一維
Y = np.ravel(Y)
Y_pred = np.ravel(Y_pred)
residuals = Y - Y_pred

st.write("迴歸係數 b0、b1(、b2,…):", np.round(np.append(model.intercept_, model.coef_),3))
st.write(f"R² = {r2_score(Y,Y_pred):.3f}")

# 四、殘差圖
fig, ax = plt.subplots()
ax.scatter(range(len(residuals)), residuals)
ax.axhline(0, color='red', linestyle='--')
ax.set_xlabel("樣本編號")
ax.set_ylabel("殘差")
ax.set_title("殘差圖")
st.pyplot(fig)

# 五、單變量散佈圖
if X.shape[1] == 1:
    fig2, ax2 = plt.subplots()
    ax2.scatter(X.ravel(), Y, color='blue', label='實測值')
    ax2.plot(X.ravel(), Y_pred, color='red', label='回歸線')
    ax2.set_xlabel("自變數 X")
    ax2.set_ylabel("因變數 Y")
    ax2.set_title("單變量回歸")
    ax2.legend()
    st.pyplot(fig2)

# 六、工程反思
st.subheader("工程反思")
st.markdown("""
1. 迴歸係數的工程意義為何？
2. R² 越高表示什麼？是否等於工程可靠？
3. 殘差圖如何幫助檢查模型假設？
4. 如果增加第二個自變數，模型會如何改變？
""")
