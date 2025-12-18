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

# 顯示係數和R² - 更緊湊的單行顯示
coefficients = np.concatenate([
    np.atleast_1d(model.intercept_), 
    np.atleast_1d(model.coef_).flatten()[1:]
])

coef_str = ", ".join([f"b{i}={coefficients[i]:.3f}" for i in range(len(coefficients))])
st.write(f"**迴歸係數 b0~b{degree}:** {coef_str}")
st.write(f"**R² = {r2_score(Y, Y_pred):.3f}**")

# 使用兩欄布局顯示圖表
col1, col2 = st.columns(2)

with col1:
    # 散佈圖與擬合曲線 - 縮小尺寸
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(X_flat, Y, color='blue', label='實測值', s=25)
    ax.plot(X_flat, Y_pred, color='red', label=f'{degree}次多項式擬合', linewidth=2)
    ax.set_xlabel("X", fontsize=9)
    ax.set_ylabel("Y", fontsize=9)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.tick_params(labelsize=8)
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    # 殘差圖 - 縮小尺寸
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.scatter(range(len(residuals)), residuals, s=25)
    ax2.axhline(0, color='red', linestyle='--', linewidth=1.5)
    ax2.set_xlabel("樣本編號", fontsize=9)
    ax2.set_ylabel("殘差", fontsize=9)
    ax2.set_title("殘差圖", fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.tick_params(labelsize=8)
    plt.tight_layout()
    st.pyplot(fig2)S
