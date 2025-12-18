# W15_RegressionEvaluation.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

st.title("第 15 週｜迴歸診斷與模型評估")
st.caption("📘 教科書第 10 章｜模型可靠性與工程判斷")

np.random.seed(42)
X1 = np.random.uniform(5,15,25)
X2 = np.random.uniform(1,5,25)
Y = 20 + 1.5*X1 + 2.0*X2 + np.random.normal(0,2,25)
X = np.column_stack((X1,X2))

model = LinearRegression()
model.fit(X,Y)
Y_pred = model.predict(X)

# 確保一維
Y = np.ravel(Y)
Y_pred = np.ravel(Y_pred)
residuals = Y - Y_pred

st.write("迴歸係數 b0、b1、b2:", np.round(np.append(model.intercept_, model.coef_),3))
st.write(f"R² = {r2_score(Y,Y_pred):.3f}")

# 殘差圖
fig, ax = plt.subplots()
ax.scatter(range(len(residuals)), residuals)
ax.axhline(0, color='red', linestyle='--')
ax.set_xlabel("樣本編號")
ax.set_ylabel("殘差")
ax.set_title("殘差圖")
st.pyplot(fig)
