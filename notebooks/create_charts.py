
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Find the main project folder automatically
BASE_DIR = Path(__file__).resolve().parent.parent

# Load the cleaned sales dataset
data_file = BASE_DIR / "data" / "cleaned_sales_data.csv"
df = pd.read_csv(data_file)

# Make sure the dashboard folder exists
dashboard_dir = BASE_DIR / "dashboard"
dashboard_dir.mkdir(parents=True, exist_ok=True)

# Chart 1: Sales by product category
category_sales = df.groupby("Category")["Sales"].sum().sort_values()

plt.figure(figsize=(9, 5))
category_sales.plot(kind="barh")
plt.title("Total Sales by Product Category")
plt.xlabel("Sales ($)")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig(dashboard_dir / "sales_by_category.png", dpi=150)
plt.close()

# Chart 2: Profit by region
region_profit = df.groupby("Region")["Profit"].sum().sort_values()

plt.figure(figsize=(9, 5))
region_profit.plot(kind="barh")
plt.title("Total Profit by Region")
plt.xlabel("Profit ($)")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig(dashboard_dir / "profit_by_region.png", dpi=150)
plt.close()

# Chart 3: Monthly sales trend
df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum()

monthly_sales.index = monthly_sales.index.to_timestamp()

plt.figure(figsize=(12, 5))
monthly_sales.plot(kind="line", marker="o", markersize=3)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig(dashboard_dir / "monthly_sales_trend.png", dpi=150)
plt.close()

print("All 3 charts created successfully!")
print(f"Charts saved in: {dashboard_dir}")
