
import pandas as pd

# Load cleaned data
df = pd.read_csv("../data/cleaned_sales_data.csv")

# Analyze sales and profit by region
region_summary = (
    df.groupby("Region")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Orders=("Order ID", "nunique"),
        Quantity_Sold=("Quantity", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("SALES AND PROFIT BY REGION")
print("-" * 60)
print(region_summary.round(2).to_string())

# Save results
region_summary.to_csv("../data/region_analysis.csv")

print("\nRegion analysis saved successfully!")
