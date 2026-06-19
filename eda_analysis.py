import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------------------------
# Create output folder
# ---------------------------
os.makedirs("output", exist_ok=True)

# ---------------------------
# Load Data
# ---------------------------
orders = pd.read_csv("dataset/List of Orders.csv")
details = pd.read_csv("dataset/Order Details.csv")

df = pd.merge(orders, details, on="Order ID")

# ---------------------------
# Data Cleaning
# ---------------------------
df.drop_duplicates(inplace=True)
df.ffill(inplace=True)

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Month"] = df["Order Date"].dt.month_name()

df.to_csv("dataset/Cleaned_Ecommerce_Data.csv", index=False)

print("Data cleaned successfully!")

# ---------------------------
# BASIC EDA
# ---------------------------
print("\nTotal Sales:", df["Amount"].sum())
print("Total Profit:", df["Profit"].sum())

print("\nCategory Sales:")
print(df.groupby("Category")["Amount"].sum())

print("\nState Sales Top 10:")
print(df.groupby("State")["Amount"].sum().sort_values(ascending=False).head(10))

# ---------------------------
# MONTHLY SALES
# ---------------------------
monthly = df.groupby("Month")["Amount"].sum()

plt.figure(figsize=(10,5))
plt.plot(monthly.index, monthly.values, marker="o")
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/monthly_sales.png")
plt.show()

# ---------------------------
# CATEGORY SALES
# ---------------------------
plt.figure(figsize=(7,5))
df.groupby("Category")["Amount"].sum().plot(kind="bar", color="skyblue")
plt.title("Category Sales")
plt.tight_layout()
plt.savefig("output/category_sales.png")
plt.show()

# ---------------------------
# STATE SALES
# ---------------------------
plt.figure(figsize=(8,5))
df.groupby("State")["Amount"].sum().sort_values(ascending=False).head(10).plot(kind="bar")
plt.title("Top States")
plt.tight_layout()
plt.savefig("output/state_sales.png")
plt.show()

# ---------------------------
# PROFIT BY CATEGORY
# ---------------------------
plt.figure(figsize=(6,5))
df.groupby("Category")["Profit"].sum().plot(kind="bar", color="orange")
plt.title("Profit by Category")
plt.tight_layout()
plt.savefig("output/profit_category.png")
plt.show()

# ---------------------------
# TOP CUSTOMERS
# ---------------------------
plt.figure(figsize=(8,5))
df.groupby("CustomerName")["Amount"].sum().sort_values(ascending=False).head(10).plot(kind="bar", color="purple")
plt.title("Top Customers")
plt.tight_layout()
plt.savefig("output/top_customers.png")
plt.show()

# ---------------------------
# HISTOGRAM
# ---------------------------
plt.figure(figsize=(6,5))
plt.hist(df["Amount"], bins=25, color="orange")
plt.title("Sales Distribution")
plt.tight_layout()
plt.savefig("output/histogram.png")
plt.show()

# ---------------------------
# SCATTER PLOT
# ---------------------------
plt.figure(figsize=(6,5))
plt.scatter(df["Amount"], df["Profit"], alpha=0.5, color="red")
plt.title("Sales vs Profit")
plt.tight_layout()
plt.savefig("output/scatter.png")
plt.show()

# ---------------------------
# BOX PLOT
# ---------------------------
plt.figure(figsize=(5,5))
plt.boxplot(df["Amount"])
plt.title("Boxplot - Sales")
plt.tight_layout()
plt.savefig("output/boxplot.png")
plt.show()

# ---------------------------
# HEATMAP
# ---------------------------
plt.figure(figsize=(6,5))
sns.heatmap(df[["Amount","Profit","Quantity"]].corr(), annot=True, cmap="Blues")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("output/heatmap.png")
plt.show()

print("All graphs saved in output folder!")