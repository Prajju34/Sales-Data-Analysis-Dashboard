
import pandas as pd

# Load cleaned data
df = pd.read_csv("../data/cleaned_sales_data.csv")

# Summarize performance by sub-category
subcategory_summary = (
    df.groupby("Sub-Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Quantity_Sold=("Quantity", "sum")
    )
    .sort_values("Total_Profit", ascending=True)
)

print("5 LOWEST-PROFIT SUB-CATEGORIES")
print("-" * 60)
print(subcategory_summary.head(5).round(2).to_string())

print("\n5 HIGHEST-PROFIT SUB-CATEGORIES")
print("-" * 60)
print(subcategory_summary.tail(5).sort_values(
    "Total_Profit", ascending=False
).round(2).to_string())

# Save the results
subcategory_summary.to_csv("../data/subcategory_analysis.csv")

print("\nSub-category analysis saved successfully!")
