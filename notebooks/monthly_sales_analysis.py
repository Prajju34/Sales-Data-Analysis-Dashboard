
import pandas as pd

# Load cleaned data
df = pd.read_csv("../data/cleaned_sales_data.csv")

# Convert order dates to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create a monthly sales summary
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

monthly_sales = (
    df.groupby("Month")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Orders=("Order ID", "nunique")
    )
    .sort_index()
)

print("FIRST 12 MONTHS OF SALES")
print("-" * 60)
print(monthly_sales.head(12).round(2).to_string())

print("\nTOP 5 MONTHS BY SALES")
print(
    monthly_sales.sort_values(
        "Total_Sales", ascending=False
    ).head(5).round(2).to_string()
)

# Save the monthly analysis
monthly_sales.to_csv("../data/monthly_sales_analysis.csv")

print("\nMonthly sales analysis saved successfully!")
