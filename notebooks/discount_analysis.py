
import pandas as pd

# Load cleaned data
df = pd.read_csv("../data/cleaned_sales_data.csv")

# Group records by discount level
discount_summary = (
    df.groupby("Discount")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Record_Count=("Order ID", "size"),
        Average_Profit=("Profit", "mean")
    )
    .sort_index()
)

print("PROFIT BY DISCOUNT LEVEL")
print("-" * 65)
print(discount_summary.round(2).to_string())

# Save results
discount_summary.to_csv("../data/discount_analysis.csv")

print("\nDiscount analysis saved successfully!")
