# W14_NonlinearRegression.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.font_manager as fm

# 設定中文字型 - 使用系統可用字型
try:
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Microsoft JhengHei', 'SimHei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False
except:
    pass

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
Y_pred = Y_pred.flatten()

X_flat = X.flatten()

residuals = Y - Y_pred

# 顯示係數和R²
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
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(X_flat, Y, color='blue', label='data points', s=25)
    ax.plot(X_flat, Y_pred, color='red', label=f'polynomial fit (degree {degree})', linewidth=2)
    ax.set_xlabel("X", fontsize=10)
    ax.set_ylabel("Y", fontsize=10)
    ax.legend(fontsize=8, loc='upper left')
    ax.grid(True, alpha=0.3)
    ax.tick_params(labelsize=9)
    plt.tight_layout()
    st.pyplot(fig)
    st.markdown("<div style='text-align: center'>📊 散佈圖與多項式擬合曲線</div>", unsafe_allow_html=True)

with col2:
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.scatter(range(len(residuals)), residuals, s=25, color='steelblue')
    ax2.axhline(0, color='red', linestyle='--', linewidth=1.5)
    ax2.set_xlabel("Sample Index", fontsize=10)
    ax2.set_ylabel("Residuals", fontsize=10)
    ax2.set_title("Residual Plot", fontsize=11)
    ax2.grid(True, alpha=0.3)
    ax2.tick_params(labelsize=9)
    plt.tight_layout()
    st.pyplot(fig2)
    st.markdown("<div style='text-align: center'>📉 殘差分布圖（用於檢驗模型適配性）</div>", unsafe_allow_html=True)
