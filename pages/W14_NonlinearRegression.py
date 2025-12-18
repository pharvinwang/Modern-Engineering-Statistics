# W14_NonlinearRegression.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

st.set_page_config(layout="wide")
st.title("第 14 週｜非線性迴歸與多項式回歸")
st.caption("📘 教科書第 10 章｜非線性擬合與工程預測")

np.random.seed(42)
X = np.linspace(50, 200, 25).reshape(-1, 1)
noise = np.random.normal(0, 2, 25)
Y = (0.01*X**2 - 0.5*X + 10).flatten() + noise

degree = st.slider("多項式階數", 1, 5, 2)

poly = PolynomialFeatures(degree=degree)
X_poly = poly.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, Y)

Y_pred = model.predict(X_poly)
Y_pred = Y_pred.flatten()  # 確保預測值是一維陣列

X_flat = X.flatten()  # 確保 X 是一維陣列

residuals = Y - Y_pred

# 顯示係數
# PolynomialFeatures 產生 [1, x, x^2, ..., x^degree]
# LinearRegression 的 intercept_ 對應截距，coef_ 對應所有特徵(包括常數項1)
# 所以 coef_[0] 對應常數項1的係數(通常接近0)，coef_[1:] 對應 x, x^2, ..., x^degree
coefficients = np.concatenate([
    np.atleast_1d(model.intercept_), 
    np.atleast_1d(model.coef_).flatten()[1:]
])
st.write(f"迴歸係數 b0~b{degree}:", np.round(coefficients, 3))
st.write(f"R² = {r2_score(Y, Y_pred):.3f}")

# 散佈圖與擬合曲線
fig, ax = plt.subplots()
ax.scatter(X_flat, Y, color='blue', label='實測值')
ax.plot(X_flat, Y_pred, color='red', label=f'{degree}次多項式擬合')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()
st.pyplot(fig)

# 殘差圖
fig2, ax2 = plt.subplots()
ax2.scatter(range(len(residuals)), residuals)
ax2.axhline(0, color='red', linestyle='--')
ax2.set_xlabel("樣本編號")
ax2.set_ylabel("殘差")
ax2.set_title("殘差圖")
st.pyplot(fig2)
