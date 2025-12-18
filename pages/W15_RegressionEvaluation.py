# W15_RegressionEvaluation.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

st.set_page_config(layout="wide")
st.title("第 15 週｜迴歸診斷與模型評估")
st.caption("📘 教科書第 10 章｜模型可靠性與工程判斷")

# 產生示例資料
np.random.seed(42)
X1 = np.random.uniform(5,15,25)
X2 = np.random.uniform(1,5,25)
Y = 20 + 1.5*X1 + 2.0*X2 + np.random.normal(0,2,25)
X = np.column_stack((X1,X2))

# 建立迴歸模型
model = LinearRegression()
model.fit(X,Y)
Y_pred = model.predict(X)

# 確保一維
Y = np.ravel(Y)
Y_pred = np.ravel(Y_pred)
residuals = Y - Y_pred

# 迴歸係數與 R²
st.write("迴歸係數 b0、b1、b2:", np.round(np.append(model.intercept_, model.coef_),3))
st.write(f"R² = {r2_score(Y,Y_pred):.3f}")

# 殘差圖
fig1, ax1 = plt.subplots()
ax1.scatter(range(len(residuals)), residuals, color='blue')
ax1.axhline(0, color='red', linestyle='--')
ax1.set_xlabel("樣本編號")
ax1.set_ylabel("殘差")
ax1.set_title("殘差圖")
st.pyplot(fig1)

# Y vs Y_pred 散佈圖
fig2, ax2 = plt.subplots()
ax2.scatter(Y, Y_pred, color='green')
ax2.plot([Y.min(), Y.max()], [Y.min(), Y.max()], 'r--', lw=2)  # 45度理想線
ax2.set_xlabel("實測值 Y")
ax2.set_ylabel("預測值 Y_pred")
ax2.set_title("Y vs Y_pred 散佈圖")
st.pyplot(fig2)

# 工程反思
st.subheader("工程反思")
st.markdown("""
1. 殘差圖是否均勻分布？有無偏態或異常值？  
2. Y vs Y_pred 散佈圖是否接近 45 度線？  
3. 迴歸係數與 R² 是否合理？  
4. 模型是否可靠，可用於工程預測？
""")
