
from pathlib import Path

import pandas as pd
import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Sales Data Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "cleaned_sales_data.csv"

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
@st.cache_data
def load_data(file_path):
    data = pd.read_csv(file_path)
    data["Order Date"] = pd.to_datetime(data["Order Date"])
    data["Ship Date"] = pd.to_datetime(data["Ship Date"])
    return data


st.title("📊 Sales Data Analysis Dashboard")
st.caption("Internship Project | Sales Performance and Business Insights")

if not DATA_FILE.exists():
    st.error(f"Dataset not found: {DATA_FILE}")
    st.stop()

df = load_data(DATA_FILE)

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------
st.sidebar.header("🔎 Dashboard Filters")

categories = sorted(df["Category"].dropna().unique().tolist())
regions = sorted(df["Region"].dropna().unique().tolist())
segments = sorted(df["Segment"].dropna().unique().tolist())

selected_categories = st.sidebar.multiselect(
    "Select Category",
    categories,
    default=categories
)

selected_regions = st.sidebar.multiselect(
    "Select Region",
    regions,
    default=regions
)

selected_segments = st.sidebar.multiselect(
    "Select Customer Segment",
    segments,
    default=segments
)

min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()

selected_dates = st.sidebar.date_input(
    "Select Order Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# --------------------------------------------------
# FILTER DATA
# --------------------------------------------------
filtered_df = df[
    df["Category"].isin(selected_categories)
    & df["Region"].isin(selected_regions)
    & df["Segment"].isin(selected_segments)
].copy()

if isinstance(selected_dates, (tuple, list)) and len(selected_dates) == 2:
    start_date, end_date = selected_dates
    filtered_df = filtered_df[
        filtered_df["Order Date"].dt.date.between(start_date, end_date)
    ]

if filtered_df.empty:
    st.warning("No records match your filters. Please change your selections.")
    st.stop()

# --------------------------------------------------
# KEY PERFORMANCE INDICATORS
# --------------------------------------------------
st.subheader("📌 Key Performance Indicators")

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
total_quantity = filtered_df["Quantity"].sum()

profit_margin = (
    total_profit / total_sales * 100 if total_sales != 0 else 0
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Total Orders", f"{total_orders:,}")
col4.metric("Units Sold", f"{total_quantity:,}")
col5.metric("Profit Margin", f"{profit_margin:.2f}%")

st.divider()

# --------------------------------------------------
# SALES BY CATEGORY
# --------------------------------------------------
st.subheader("📦 Sales by Product Category")

category_data = (
    filtered_df.groupby("Category", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Sales", ascending=False)
)

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.markdown("**Total Sales by Category**")
    st.bar_chart(category_data, x="Category", y="Sales")

with chart_col2:
    st.markdown("**Profit by Category**")
    st.bar_chart(category_data, x="Category", y="Profit")

# --------------------------------------------------
# TOP PRODUCTS
# --------------------------------------------------
st.subheader("🏆 Top-Selling Products")

top_n = st.selectbox(
    "Number of top products to display",
    options=[5, 10, 15],
    index=0
)

top_products = (
    filtered_df.groupby("Product Name", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Total_Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
    .sort_values("Total_Sales", ascending=False)
    .head(top_n)
)

product_col1, product_col2 = st.columns(2)

with product_col1:
    st.markdown("**Products Ranked by Sales**")
    st.bar_chart(
        top_products.sort_values("Total_Sales"),
        x="Product Name",
        y="Total_Sales"
    )

with product_col2:
    st.markdown("**Top Products — Details**")
    st.dataframe(
        top_products.style.format({
            "Total_Sales": "${:,.2f}",
            "Total_Profit": "${:,.2f}",
            "Total_Quantity": "{:,.0f}",
            "Orders": "{:,.0f}"
        }),
        use_container_width=True,
        hide_index=True
    )

# --------------------------------------------------
# REGIONAL PERFORMANCE
# --------------------------------------------------
st.subheader("🌎 Regional Performance")

region_data = (
    filtered_df.groupby("Region", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
    .sort_values("Sales", ascending=False)
)

region_col1, region_col2 = st.columns(2)

with region_col1:
    st.markdown("**Sales by Region**")
    st.bar_chart(region_data, x="Region", y="Sales")

with region_col2:
    st.markdown("**Profit by Region**")
    st.bar_chart(region_data, x="Region", y="Profit")

# --------------------------------------------------
# MONTHLY SALES TREND
# --------------------------------------------------
st.subheader("📈 Monthly Sales Trend")

monthly_data = (
    filtered_df.set_index("Order Date")
    .resample("MS")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .reset_index()
)

st.line_chart(monthly_data, x="Order Date", y="Sales")

# --------------------------------------------------
# SUB-CATEGORY PROFITABILITY
# --------------------------------------------------
st.subheader("🏷️ Sub-Category Profitability")

subcategory_data = (
    filtered_df.groupby("Sub-Category", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Profit", ascending=True)
)

st.bar_chart(subcategory_data, x="Sub-Category", y="Profit")

st.markdown("**Five lowest-profit sub-categories**")

st.dataframe(
    subcategory_data.head(5).style.format({
        "Sales": "${:,.2f}",
        "Profit": "${:,.2f}",
        "Quantity": "{:,.0f}"
    }),
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# BUSINESS INSIGHTS
# --------------------------------------------------
st.subheader("💡 Business Insights")

best_sales_category = category_data.loc[category_data["Sales"].idxmax()]
best_profit_category = category_data.loc[category_data["Profit"].idxmax()]
best_sales_region = region_data.loc[region_data["Sales"].idxmax()]
lowest_profit_region = region_data.loc[region_data["Profit"].idxmin()]
lowest_profit_subcategory = subcategory_data.iloc[0]
top_product = top_products.iloc[0]

st.write(
    f"1. **Sales leader:** {best_sales_category['Category']} "
    f"has the highest category sales (${best_sales_category['Sales']:,.2f})."
)

st.write(
    f"2. **Profit leader:** {best_profit_category['Category']} "
    f"has the highest category profit "
    f"(${best_profit_category['Profit']:,.2f})."
)

st.write(
    f"3. **Leading region:** {best_sales_region['Region']} "
    f"has the highest regional sales (${best_sales_region['Sales']:,.2f})."
)

st.write(
    f"4. **Region to investigate:** {lowest_profit_region['Region']} "
    f"has the lowest regional profit "
    f"(${lowest_profit_region['Profit']:,.2f}). Review its product mix, "
    "discounts and costs."
)

st.write(
    f"5. **Sub-category to review:** {lowest_profit_subcategory['Sub-Category']} "
    f"has the lowest sub-category profit "
    f"(${lowest_profit_subcategory['Profit']:,.2f}). Investigate pricing, "
    "discounts and costs."
)

st.write(
    f"6. **Top product by sales:** {top_product['Product Name']} "
    f"has sales of ${top_product['Total_Sales']:,.2f} "
    "under the current filters."
)

st.caption(
    "Insights change with the selected filters. These are descriptive findings; "
    "they do not prove that discounts or other factors caused a result."
)

# --------------------------------------------------
# DOWNLOAD FILTERED DATA
# --------------------------------------------------
st.subheader("📥 Download Data")

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Sales Data (CSV)",
    data=csv_data,
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

with st.expander("View Filtered Dataset"):
    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

st.caption("Created with Python, Pandas and Streamlit.")
