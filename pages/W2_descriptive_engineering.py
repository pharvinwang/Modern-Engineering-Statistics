# W2_descriptive_engineering.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("第 2 週｜工程資料的描述統計與代表值問題")
st.caption("📘 教科書第 2 章（2.1–2.4）")

st.markdown("""
工程統計的核心之一：
> **資料代表什麼？哪些統計量可以支撐工程判斷？**

今天你將觀察：
- 平均值、中位數
- 最大值、95%分位數
- 變異的大小
""")

# -------------------------------------------------
# A. 工程案例選擇
# -------------------------------------------------
st.subheader("一、工程案例選擇")
case = st.selectbox(
    "選擇工程案例",
    ["坡地位移監測", "單場降雨事件", "施工品質檢測"]
)

# B. 資料來源（內建或上傳）
st.subheader("二、資料來源")
source = st.radio(
    "使用內建資料或上傳自己的 CSV",
    ["內建資料", "上傳 CSV"]
)

if source == "上傳 CSV":
    uploaded_file = st.file_uploader("請上傳 CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        st.warning("請先上傳 CSV")
        st.stop()
else:
    # 建立內建資料
    np.random.seed(42)
    if case == "坡地位移監測":
        df = pd.DataFrame({"位移_mm": np.random.normal(2.0, 0.3, 50)})
    elif case == "單場降雨事件":
        df = pd.DataFrame({"降雨_mm": np.random.normal(120, 15, 50)})
    else:
        df = pd.DataFrame({"夯實度_percent": np.random.normal(95, 3, 50)})

st.dataframe(df, use_container_width=True)

# -------------------------------------------------
# C. 選擇分析欄位
# -------------------------------------------------
st.subheader("三、選擇分析欄位")
col = st.selectbox("欄位", df.columns)

# -------------------------------------------------
# D. 可調參數：抽樣大小
# -------------------------------------------------
st.subheader("四、抽樣與可取得資料量")
sample_size = st.slider("可取得樣本數", min_value=3, max_value=len(df), value=10)
sample = df[col].sample(n=sample_size, random_state=42)

# -------------------------------------------------
# E. 計算統計量
# -------------------------------------------------
mean_val = sample.mean()
median_val = sample.median()
max_val = sample.max()
q95_val = sample.quantile(0.95)
std_val = sample.std()

# -------------------------------------------------
# F. 視覺化
# -------------------------------------------------
st.subheader("五、統計量與分布視覺化")
fig, ax = plt.subplots()
ax.hist(sample, bins=10, color='skyblue', edgecolor='black')
ax.axvline(mean_val, color='r', linestyle='--', label=f"平均值 {mean_val:.2f}")
ax.axvline(median_val, color='g', linestyle=':', label=f"中位數 {median_val:.2f}")
ax.axvline(q95_val, color='purple', linestyle='-.', label=f"95%分位數 {q95_val:.2f}")
ax.legend()
st.pyplot(fig, use_container_width=True)

# -------------------------------------------------
# G. 工程決策反思
# -------------------------------------------------
st.subheader("六、工程決策反思")
st.warning(f"""
你現在看到的樣本只有 {sample_size} 筆。
- 平均值 = {mean_val:.2f}
- 中位數 = {median_val:.2f}
- 最大值 = {max_val:.2f}
- 95% 分位數 = {q95_val:.2f}
- 標準差 = {std_val:.2f}

思考：
1. 如果你以平均值作設計依據，是否安全？
2. 若採中位數，會怎樣？
3. 你會選哪個統計量作工程判斷？
4. 如果增加樣本數，結果會變穩嗎？
""")
st.info("""
📌 今天目標：
- 理解統計量與工程判斷的關聯
- 體驗資料有限時的不確定性
- 建立工程決策感覺
""")
