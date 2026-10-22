
import pandas as pd

# Load the original dataset
df = pd.read_excel("../data/sample_-_superstore.xls")

# Record the original row count
original_rows = len(df)

# Set the analysis reference date
reference_date = pd.Timestamp("2026-10-22")

# Exclude future-dated records from the analysis dataset
clean_df = df[df["Order Date"] <= reference_date].copy()

# Check the cleaned data
print("Original rows:", original_rows)
print("Rows excluded:", original_rows - len(clean_df))
print("Cleaned rows:", len(clean_df))
print("Missing values:", clean_df.isnull().sum().sum())
print("Duplicate rows:", clean_df.duplicated().sum())

# Save the cleaned dataset
clean_df.to_csv("../data/cleaned_sales_data.csv", index=False)

print("\nCleaned dataset saved successfully!")
