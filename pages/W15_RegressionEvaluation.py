# W15_RegressionEvaluation.py
# 迴歸診斷與模型評估互動頁

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import r2_score

st.set_page_config(layout="wide")
st.title("第 15 週｜迴歸診斷與模型評估")
st.caption("📘 教科書第 10 章｜重點：模型可靠性與工程判斷")

# =================================================
# A. 工程案例選擇
# =================================================
st.subheader("一、工程案例")
case = st.selectbox(
    "選擇工程案例",
    ["施工進度預測（多變量）", "坡地沉降含工法指標變數"]
)

np.random.seed(42)

# =================================================
# B. 生成或上傳資料
# =================================================
st.subheader("二、資料來源")
upload = st.file_uploader("可上傳 CSV，X1,X2,(X3) Y", type="csv")

if upload is not None:
    df = pd.read_csv(upload)
    Y = df.iloc[:,-1].values
    X = df.iloc[:,:-1].values
else:
    if case == "施工進度預測（多變量）":
        X1 = np.random.uniform(5,15,25)  # 工人數
        X2 = np.random.uniform(1,5,25)   # 機械數
        Y = 20 + 1.5*X1 + 2.0*X2 + np.random.normal(0,2,25)
        X = np.column_stack((X1,X2))
    else:
        # 工法指標變數
        X1 = np.random.uniform(50,200,25).reshape(-1,1)  # 降雨量
        X2 = np.random.choice([0,1], size=(25,1))         # 工法 A/B
        Y = 0.01*X1**2 -0.5*X1 + 2*X2 + 10 + np.random.normal(0,2,25)
        X = np.hstack((X1,X2))

# =================================================
# C. 建立迴歸模型
# =================================================
st.subheader("三、建立迴歸模型")

model = LinearRegression()
model.fit(X,Y)
Y_pred = model.predict(X)
st.write("迴歸係數 b0、b1(、b2,…)：", np.round(np.append(model.intercept_, model.coef_),3))

# =================================================
# D. 模型評估
# =================================================
st.subheader("四、模型評估")
r2 = r2_score(Y,Y_pred)
st.write(f"R² = {r2:.3f}")

# 殘差
residuals = Y - Y_pred
fig, ax = plt.subplots()
ax.scatter(range(len(residuals)), residuals)
ax.axhline(0, color='red', linestyle='--')
ax.set_xlabel("樣本編號")
ax.set_ylabel("殘差")
ax.set_title("殘差圖檢查模型假設")
st.pyplot(fig)

# =================================================
# E. 視覺化回歸擬合
# =================================================
st.subheader("五、擬合與指標變數效果")

if X.shape[1]==1:
    plt.figure()
    plt.scatter(X,Y,color='blue',label='實測值')
    plt.plot(X,Y_pred,color='red',label='回歸線')
    plt.xlabel("自變數 X")
    plt.ylabel("因變數 Y")
    plt.title("單變量回歸")
    plt.legend()
    st.pyplot(plt.gcf())
else:
    st.write("多變量或含指標變數，請參考迴歸係數與預測值判斷影響")

# =================================================
# F. 工程反思
# =================================================
st.subheader("六、工程反思")
st.markdown("""
1. 殘差圖是否顯示線性假設合理？  
2. R² 與工程可靠性有什麼關係？  
3. 指標變數係數如何影響工程判斷？  
4. 模型是否過擬合？如何檢查？  
""")
