
import pandas as pd

# Load cleaned data
df = pd.read_csv("../data/cleaned_sales_data.csv")

# Summarize sales and profit by category
category_summary = (
    df.groupby("Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Quantity_Sold=("Quantity", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
)

print("SALES AND PROFIT BY CATEGORY")
print("-" * 60)
print(category_summary.round(2).to_string())

# Save the results
category_summary.to_csv("../data/category_analysis.csv")

print("\nCategory analysis saved successfully!")
