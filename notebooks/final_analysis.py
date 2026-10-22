
from pathlib import Path

import pandas as pd

# --------------------------------------------------
# PROJECT PATHS
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "cleaned_sales_data.csv"
OUTPUT_DIR = BASE_DIR / "data"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# LOAD CLEANED DATA
# --------------------------------------------------
if not DATA_FILE.exists():
    raise FileNotFoundError(
        f"Cleaned dataset not found: {DATA_FILE}"
    )

df = pd.read_csv(DATA_FILE)
df["Order Date"] = pd.to_datetime(df["Order Date"])

print("=" * 60)
print("SALES DATA ANALYSIS - FINAL SUMMARY")
print("=" * 60)

# --------------------------------------------------
# OVERALL KPIs
# --------------------------------------------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_quantity = df["Quantity"].sum()

profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0
    else 0
)

kpi_summary = pd.DataFrame({
    "Metric": [
        "Total Sales",
        "Total Profit",
        "Total Orders",
        "Units Sold",
        "Profit Margin (%)",
        "Dataset Rows"
    ],
    "Value": [
        round(total_sales, 2),
        round(total_profit, 2),
        total_orders,
        total_quantity,
        round(profit_margin, 2),
        len(df)
    ]
})

print("\nOVERALL PERFORMANCE")
print(kpi_summary.to_string(index=False))

# --------------------------------------------------
# CATEGORY ANALYSIS
# --------------------------------------------------
category_summary = (
    df.groupby("Category", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Quantity_Sold=("Quantity", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
)

category_summary.to_csv(
    OUTPUT_DIR / "final_category_analysis.csv",
    index=False
)

print("\nCATEGORY PERFORMANCE")
print(category_summary.to_string(index=False))

# --------------------------------------------------
# REGIONAL ANALYSIS
# --------------------------------------------------
region_summary = (
    df.groupby("Region", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Orders=("Order ID", "nunique"),
        Quantity_Sold=("Quantity", "sum")
    )
    .sort_values("Total_Sales", ascending=False)
)

region_summary.to_csv(
    OUTPUT_DIR / "final_region_analysis.csv",
    index=False
)

print("\nREGIONAL PERFORMANCE")
print(region_summary.to_string(index=False))

# --------------------------------------------------
# MONTHLY SALES ANALYSIS
# --------------------------------------------------
monthly_summary = (
    df.set_index("Order Date")
    .resample("MS")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Orders=("Order ID", "nunique")
    )
    .reset_index()
)

monthly_summary["Order Date"] = (
    monthly_summary["Order Date"].dt.strftime("%Y-%m")
)

monthly_summary.to_csv(
    OUTPUT_DIR / "final_monthly_analysis.csv",
    index=False
)

print("\nTOP 5 MONTHS BY SALES")
print(
    monthly_summary.nlargest(5, "Total_Sales")
    .to_string(index=False)
)

# --------------------------------------------------
# TOP PRODUCTS
# --------------------------------------------------
product_summary = (
    df.groupby("Product Name", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Quantity_Sold=("Quantity", "sum"),
        Total_Orders=("Order ID", "nunique")
    )
    .sort_values("Total_Sales", ascending=False)
)

product_summary.to_csv(
    OUTPUT_DIR / "final_product_analysis.csv",
    index=False
)

print("\nTOP 10 PRODUCTS BY SALES")
print(product_summary.head(10).to_string(index=False))

# --------------------------------------------------
# SUB-CATEGORY PROFITABILITY
# --------------------------------------------------
subcategory_summary = (
    df.groupby("Sub-Category", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Quantity_Sold=("Quantity", "sum")
    )
    .sort_values("Total_Profit")
)

subcategory_summary.to_csv(
    OUTPUT_DIR / "final_subcategory_analysis.csv",
    index=False
)

print("\n5 LOWEST-PROFIT SUB-CATEGORIES")
print(subcategory_summary.head(5).to_string(index=False))

# --------------------------------------------------
# DISCOUNT ANALYSIS
# --------------------------------------------------
discount_summary = (
    df.groupby("Discount", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Record_Count=("Discount", "size")
    )
    .sort_values("Discount")
)

discount_summary.to_csv(
    OUTPUT_DIR / "final_discount_analysis.csv",
    index=False
)

print("\nDISCOUNT PERFORMANCE")
print(discount_summary.to_string(index=False))

# --------------------------------------------------
# BUSINESS INSIGHTS
# --------------------------------------------------
best_sales_category = category_summary.loc[
    category_summary["Total_Sales"].idxmax()
]

best_profit_category = category_summary.loc[
    category_summary["Total_Profit"].idxmax()
]

best_sales_region = region_summary.loc[
    region_summary["Total_Sales"].idxmax()
]

lowest_profit_region = region_summary.loc[
    region_summary["Total_Profit"].idxmin()
]

top_product = product_summary.iloc[0]
lowest_profit_subcategory = subcategory_summary.iloc[0]

insights = [
    (
        f"{best_sales_category['Category']} has the highest category "
        f"sales at ${best_sales_category['Total_Sales']:,.2f}."
    ),
    (
        f"{best_profit_category['Category']} has the highest category "
        f"profit at ${best_profit_category['Total_Profit']:,.2f}."
    ),
    (
        f"{best_sales_region['Region']} has the highest regional sales "
        f"at ${best_sales_region['Total_Sales']:,.2f}."
    ),
    (
        f"{lowest_profit_region['Region']} has the lowest regional profit "
        f"at ${lowest_profit_region['Total_Profit']:,.2f}; its product mix "
        "and costs merit investigation."
    ),
    (
        f"{top_product['Product Name']} is the top product by sales "
        f"at ${top_product['Total_Sales']:,.2f}."
    ),
    (
        f"{lowest_profit_subcategory['Sub-Category']} has the lowest "
        f"sub-category profit at "
        f"${lowest_profit_subcategory['Total_Profit']:,.2f}."
    )
]

insights_file = OUTPUT_DIR / "final_business_insights.txt"

with open(insights_file, "w", encoding="utf-8") as file:
    file.write("SALES DATA ANALYSIS - BUSINESS INSIGHTS\n\n")
    for number, insight in enumerate(insights, start=1):
        file.write(f"{number}. {insight}\n\n")

print("\nBUSINESS INSIGHTS")
for number, insight in enumerate(insights, start=1):
    print(f"{number}. {insight}")

# --------------------------------------------------
# SAVE KPI SUMMARY AND FINISH
# --------------------------------------------------
kpi_summary.to_csv(
    OUTPUT_DIR / "final_kpi_summary.csv",
    index=False
)

print("\n" + "=" * 60)
print("FINAL ANALYSIS COMPLETED SUCCESSFULLY")
print(f"Analysis outputs saved in: {OUTPUT_DIR}")
print("=" * 60)
