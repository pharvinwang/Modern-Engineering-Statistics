# W14_NonlinearRegression.py
# 非線性與多項式迴歸互動頁

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

st.set_page_config(layout="wide")
st.title("第 14 週｜非線性迴歸與多項式回歸")
st.caption("📘 教科書第 10 章｜重點：非線性擬合與工程預測")

# =================================================
# A. 工程案例
# =================================================
st.subheader("一、工程案例")
case = st.selectbox(
    "選擇工程案例",
    ["坡地沉降預測", "施工進度曲線"]
)

np.random.seed(42)

# =================================================
# B. 生成或上傳資料
# =================================================
st.subheader("二、資料來源")
upload = st.file_uploader("可上傳 CSV，X, Y", type="csv")

if upload is not None:
    df = pd.read_csv(upload)
    X = df.iloc[:,0].values.reshape(-1,1)
    Y = df.iloc[:,1].values
else:
    if case == "坡地沉降預測":
        X = np.linspace(50,200,25).reshape(-1,1)
        Y = 0.01*X**2 - 0.5*X + 10 + np.random.normal(0,2,25)
    else:
        X = np.linspace(1,12,25).reshape(-1,1)
        Y = 0.2*X**3 - 1.5*X**2 + 3*X + np.random.normal(0,1,25)

# =================================================
# C. 選擇多項式階數
# =================================================
st.subheader("三、選擇多項式階數")
degree = st.slider("多項式階數", 1, 5, 2)

poly = PolynomialFeatures(degree=degree)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, Y)
Y_pred = model.predict(X_poly)

# =================================================
# D. 評估模型
# =================================================
st.subheader("四、模型評估")
r2 = r2_score(Y, Y_pred)
st.write(f"R² = {r2:.3f}")

residuals = Y - Y_pred
fig, ax = plt.subplots()
ax.scatter(range(len(residuals)), residuals)
ax.axhline(0, color='red', linestyle='--')
ax.set_xlabel("樣本編號")
ax.set_ylabel("殘差")
ax.set_title("殘差圖")
st.pyplot(fig)

# =================================================
# E. 視覺化擬合曲線
# =================================================
st.subheader("五、擬合曲線視覺化")
fig2, ax2 = plt.subplots()
ax2.scatter(X, Y, color='blue', label='實測值')
ax2.plot(X, Y_pred, color='red', label=f'{degree}次多項式擬合')
ax2.set_xlabel("自變數 X")
ax2.set_ylabel("因變數 Y")
ax2.set_title("非線性回歸擬合曲線")
ax2.legend()
st.pyplot(fig2)

# =================================================
# F. 工程反思
# =================================================
st.subheader("六、工程反思")
st.markdown("""
1. 多項式階數越高，R² 會增加，但是否總是工程上可靠？  
2. 殘差圖如何幫助檢查模型假設？  
3. 如果增加更多自變數，模型會如何改變？  
4. 如何將擬合曲線應用到坡地沉降或施工進度預測？
""")
