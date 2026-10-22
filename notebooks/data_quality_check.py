
import pandas as pd

# Load the original dataset
file_path = "../data/sample_-_superstore.xls"
df = pd.read_excel(file_path)

# Display basic dataset information
print("Dataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

print("\nExact duplicate rows:", df.duplicated().sum())

# Flag future-dated orders for investigation
reference_date = pd.Timestamp("2026-10-22")
future_orders = df[df["Order Date"] > reference_date]

print("\nFuture-dated rows:", len(future_orders))
print("\nFuture-dated orders by year:")
print(future_orders["Order Date"].dt.year.value_counts().sort_index())

# Save the inspection results, not a modified dataset
future_orders.to_csv("../data/future_dated_records_review.csv", index=False)

print("\nReview file saved successfully.")
