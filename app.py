import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

st.title("📊 E-Commerce Sales Dashboard")
st.write("Complete interactive dashboard with 10 visual insights")

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("dataset/Cleaned_Ecommerce_Data.csv")

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("Filters")

category = st.sidebar.multiselect(
    "Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

state = st.sidebar.multiselect(
    "State",
    df["State"].unique(),
    default=df["State"].unique()
)

df = df[(df["Category"].isin(category)) & (df["State"].isin(state))]

# -----------------------------
# KPI CARDS
# -----------------------------
st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"{df['Amount'].sum():,.0f}")
col2.metric("Total Profit", f"{df['Profit'].sum():,.0f}")
col3.metric("Average Sales", f"{df['Amount'].mean():,.2f}")
col4.metric("Total Orders", df.shape[0])

st.divider()

# =====================================================
# 1. CATEGORY SALES
# =====================================================
st.subheader("1️⃣ Category-wise Sales")

fig, ax = plt.subplots()
df.groupby("Category")["Amount"].sum().plot(
    kind="bar",
    color=["#FF6B6B", "#4ECDC4", "#FFD93D"]
)
st.pyplot(fig)

# =====================================================
# 2. STATE SALES
# =====================================================
st.subheader("2️⃣ State-wise Sales (Top 10)")

fig, ax = plt.subplots()
df.groupby("State")["Amount"].sum().sort_values(ascending=False).head(10).plot(
    kind="bar",
    color="#4C72B0"
)
st.pyplot(fig)

# =====================================================
# 3. MONTHLY SALES TREND
# =====================================================
st.subheader("3️⃣ Monthly Sales Trend")

monthly = df.groupby("Month")["Amount"].sum()

fig, ax = plt.subplots()
ax.plot(monthly.index, monthly.values, marker="o", color="green")
ax.fill_between(monthly.index, monthly.values, alpha=0.2)
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# =====================================================
# 4. PROFIT BY CATEGORY
# =====================================================
st.subheader("4️⃣ Profit by Category")

fig, ax = plt.subplots()
df.groupby("Category")["Profit"].sum().plot(
    kind="bar",
    color="orange"
)
st.pyplot(fig)

# =====================================================
# 5. TOP CUSTOMERS
# =====================================================
st.subheader("5️⃣ Top Customers")

top = df.groupby("CustomerName")["Amount"].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots()
top.plot(kind="bar", color="purple")
st.pyplot(fig)

# =====================================================
# 6. SALES DISTRIBUTION
# =====================================================
st.subheader("6️⃣ Sales Distribution (Histogram)")

fig, ax = plt.subplots()
ax.hist(df["Amount"], bins=25, color="skyblue", edgecolor="black")
st.pyplot(fig)

# =====================================================
# 7. SALES vs PROFIT
# =====================================================
st.subheader("7️⃣ Sales vs Profit")

fig, ax = plt.subplots()
ax.scatter(df["Amount"], df["Profit"], color="red", alpha=0.5)
st.pyplot(fig)

# =====================================================
# 8. BOX PLOT (OUTLIERS)
# =====================================================
st.subheader("8️⃣ Sales Outliers (Box Plot)")

fig, ax = plt.subplots()
ax.boxplot(df["Amount"])
st.pyplot(fig)

# =====================================================
# 9. CORRELATION HEATMAP
# =====================================================
st.subheader("9️⃣ Correlation Heatmap")

fig, ax = plt.subplots()
sns.heatmap(df[["Amount","Profit","Quantity"]].corr(), annot=True, cmap="Blues", ax=ax)
st.pyplot(fig)

# =====================================================
# 10. CATEGORY + PROFIT COMPARISON
# =====================================================
st.subheader("🔟 Category Performance Overview")

fig, ax = plt.subplots()
df.groupby("Category")[["Amount", "Profit"]].sum().plot(
    kind="bar",
    ax=ax,
    color=["#3498db", "#e74c3c"]
)
st.pyplot(fig)

# -----------------------------
# DATA PREVIEW
# -----------------------------
st.subheader("Dataset Preview")
st.dataframe(df.head(500))