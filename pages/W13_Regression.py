# W13_Regression.py
# 線性與單/多變量迴歸互動頁

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

st.set_page_config(layout="wide")
st.title("第 13 週｜線性回歸與單/多迴歸")
st.caption("📘 教科書第 10 章｜重點：迴歸分析與工程預測")

# =================================================
# A. 工程案例
# =================================================
st.subheader("一、工程案例")
case = st.selectbox(
    "選擇工程案例",
    ["坡地位移預測（單變量）", "施工時間預測（多變量）"]
)

np.random.seed(42)

# =================================================
# B. 生成或上傳資料
# =================================================
st.subheader("二、資料來源")
upload = st.file_uploader("可上傳 CSV，X1, X2, Y", type="csv")

if upload is not None:
    df = pd.read_csv(upload)
else:
    if case == "坡地位移預測（單變量）":
        X = np.random.uniform(50, 200, 25).reshape(-1,1)  # 降雨量 mm
        Y = 2 + 0.01*X + np.random.normal(0,0.2,25)        # 坡地位移 mm
    else:
        X1 = np.random.uniform(5,15,25)  # 工人數
        X2 = np.random.uniform(1,5,25)   # 機械數
        Y = 20 + 1.5*X1 + 2.0*X2 + np.random.normal(0,2,25)
        X = np.column_stack((X1,X2))

# =================================================
# C. 建立回歸模型
# =================================================
st.subheader("三、建立迴歸模型")

model = LinearRegression()
model.fit(X, Y)
Y_pred = model.predict(X)

st.write("迴歸係數 b0、b1(、b2)：", np.round(np.append(model.intercept_, model.coef_),3))

# =================================================
# D. 評估模型
# =================================================
st.subheader("四、模型評估")

r2 = r2_score(Y, Y_pred)
st.write(f"R² = {r2:.3f}")

# 殘差
residuals = Y - Y_pred

fig, ax = plt.subplots()
ax.scatter(range(len(residuals)), residuals)
ax.axhline(0, color='red', linestyle='--')
ax.set_xlabel("樣本編號")
ax.set_ylabel("殘差")
ax.set_title("殘差圖")
st.pyplot(fig)

# =================================================
# E. 視覺化回歸線（單變量）
# =================================================
if case == "坡地位移預測（單變量）":
    st.subheader("五、散佈圖與回歸線")
    plt.figure()
    plt.scatter(X, Y, color='blue', label='實測值')
    plt.plot(X, Y_pred, color='red', label='回歸線')
    plt.xlabel("降雨量 (mm)")
    plt.ylabel("坡地位移 (mm)")
    plt.title("單變量回歸")
    plt.legend()
    st.pyplot(plt.gcf())

# =================================================
# F. 工程反思
# =================================================
st.subheader("六、工程反思")
st.markdown("""
1. 迴歸模型的斜率代表什麼工程意義？  
2. R² 越高表示什麼？是否等於工程可靠？  
3. 殘差圖如何幫助檢查模型假設？  
4. 如果增加一個自變數，模型會怎麼變化？
""")
