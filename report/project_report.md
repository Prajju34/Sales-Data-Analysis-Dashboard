
# SALES DATA ANALYSIS DASHBOARD
## Internship Mini Project Report

**Project Title:** Sales Data Analysis Dashboard  
**Project Level:** Beginner  
**Duration:** 2 Weeks  
**Tools Used:** Python, Pandas, NumPy, Matplotlib and Streamlit

**Submitted by:** [Your Name]  
**Internship Organization:** [Organization Name]  
**Mentor Name:** [Mentor Name]  
**Submission Date:** [Submission Date]

---

## 1. Abstract

This project focuses on analyzing sales data to understand business performance through data cleaning, exploratory analysis, visualization and an interactive dashboard. Python and its data analysis libraries were used to process the dataset, calculate performance indicators, compare product categories and regions, and identify business opportunities.

The final dashboard presents key performance indicators, product performance, regional comparisons, monthly sales trends and business insights. Interactive filters allow users to explore results by category, region, customer segment and date range.

## 2. Introduction

Sales data analysis helps organizations understand revenue, profitability, product demand and regional performance. Examining sales records can reveal which products perform well and which areas may need further investigation.

This project demonstrates the complete data analysis workflow, from understanding and cleaning a dataset to creating an interactive dashboard and communicating findings.

## 3. Project Objectives

- Understand the structure and quality of the sales dataset.
- Identify missing values, duplicate records and date-related issues.
- Clean and prepare the data for analysis.
- Calculate total sales, total profit, total orders and profit margin.
- Analyze monthly sales, product categories, individual products and regions.
- Create charts and an interactive dashboard.
- Generate at least five meaningful business insights.
- Document the findings for business decision-making.

## 4. Tools and Technologies

- **Python:** Programming and analysis.
- **Pandas:** Data cleaning, grouping and aggregation.
- **NumPy:** Numerical computing support.
- **Matplotlib:** Static chart creation.
- **Streamlit:** Interactive dashboard development.
- **Visual Studio Code:** Code editing and project development.
- **CSV:** Storage of cleaned data and analysis outputs.
- **PowerShell:** Running Python scripts and the dashboard.

## 5. Dataset Description

The project uses a sales dataset originally provided in Excel format.

The original dataset contains 10,194 rows and 21 columns. It includes information about orders, customers, shipping, regions, product categories, sales, quantities, discounts and profit.

Important columns include:

- Order ID
- Order Date
- Ship Date
- Customer Name
- Segment
- Region
- Category
- Sub-Category
- Product Name
- Sales
- Quantity
- Discount
- Profit

The original dataset is retained separately from the cleaned analysis dataset.

## 6. Data Cleaning and Preparation

The data quality checks identified the following:

- Original dataset size: 10,194 rows and 21 columns.
- Missing values: 0.
- Exact duplicate rows: 0.
- Records with order dates after 22 October 2026: 1,019.

The 1,019 future-dated records were exported separately for review. They were excluded from the analysis dataset to avoid including dates later than the project review date.

After this step, the cleaned analysis dataset contained 9,175 rows.

The original dataset was preserved. The exclusion of future-dated records is documented as a data preparation decision and should be reviewed if the source dataset is intended to include future or planned transactions.

## 7. Methodology

The project followed these stages:

1. Data collection and understanding.
2. Data quality assessment.
3. Data cleaning and preprocessing.
4. KPI calculation and exploratory analysis.
5. Category, regional, monthly and product analysis.
6. Chart creation.
7. Interactive dashboard development.
8. Business insight generation.
9. Documentation and final submission preparation.

## 8. Key Performance Indicators

The analysis of the 9,175-row cleaned dataset produced the following results:

| KPI | Result |
|---|---:|
| Total Sales | $2,111,931.81 |
| Total Profit | $273,111.42 |
| Total Orders | 4,581 |
| Units Sold | 34,712 |
| Profit Margin | 12.93% |
| Cleaned Dataset Rows | 9,175 |

Profit margin is calculated as total profit divided by total sales, multiplied by 100.

## 9. Product Category Analysis

The category analysis produced these results:

| Category | Total Sales | Total Profit |
|---|---:|---:|
| Technology | $764,648.41 | $135,079.78 |
| Furniture | $681,580.73 | $18,170.06 |
| Office Supplies | $665,702.67 | $119,861.58 |

Technology recorded the highest total sales and profit among the three categories. Furniture generated substantial sales but considerably lower profit than the other categories, suggesting that its product mix, discounts and costs deserve further examination.

## 10. Regional Performance

| Region | Total Sales | Total Profit | Total Orders |
|---|---:|---:|---:|
| West | $677,194.05 | $102,491.60 | 1,478 |
| East | $622,585.77 | $82,182.77 | 1,315 |
| Central | $466,388.27 | $42,735.11 | 1,054 |
| South | $345,763.72 | $45,701.93 | 734 |

The West region recorded the highest sales and profit. The South region had the lowest sales and order count. Central generated more sales than South but lower total profit, making its product mix, costs and discount patterns worth investigating.

## 11. Monthly Sales Analysis

Monthly sales were calculated by grouping orders by month.

The five highest-sales months in the analysis dataset were:

| Month | Total Sales |
|---|---:|
| December 2025 | $97,502.28 |
| September 2026 | $88,064.53 |
| September 2023 | $82,670.43 |
| November 2025 | $79,411.97 |
| November 2023 | $78,826.96 |

December 2025 recorded the highest monthly sales in the dataset. Monthly trends can help a business examine seasonality, demand changes and sales planning opportunities.

## 12. Top-Selling Products

The product analysis ranks individual products by total sales.

The highest-sales product was:

**Canon imageCLASS 2200 Advanced Copier**

- Total sales: $51,099.85
- Total profit: approximately $20,159.94
- Quantity sold: 17
- Distinct orders: 4

The interactive dashboard also allows users to view different numbers of top-selling products under the selected filters.

## 13. Sub-Category Profitability

The three lowest-profit sub-categories were:

| Sub-Category | Total Sales | Total Profit |
|---|---:|---:|
| Tables | $183,399.07 | -$15,599.77 |
| Bookcases | $108,827.77 | -$3,115.69 |
| Supplies | $43,645.85 | -$1,235.62 |

Tables recorded the largest loss among the sub-categories shown. These results suggest a need to investigate pricing, discounting, costs and product-level performance before deciding on corrective action.

## 14. Discount Analysis

The discount analysis compared sales and profit at different discount levels.

In this dataset, discount levels of 30% and above had negative aggregate profit. For example, records with a 70% discount showed total profit of approximately -$37,830.61.

This is an association in the available records, not proof that discounts alone caused the losses. Product mix, order characteristics and other costs should be investigated before making business decisions.

## 15. Business Insights

The project produced the following business insights:

1. **Technology leads category performance:** It recorded $764,648.41 in sales and $135,079.78 in profit.
2. **Furniture needs further investigation:** Its sales were $681,580.73, while profit was $18,170.06.
3. **West is the leading region:** It recorded $677,194.05 in sales and $102,491.60 in profit.
4. **Central has a comparatively low profit result:** Its profit was $42,735.11 despite sales of $466,388.27.
5. **The Canon imageCLASS 2200 Advanced Copier leads product sales:** It generated $51,099.85 in sales.
6. **Tables is the lowest-profit sub-category:** It recorded a loss of $15,599.77.
7. **High discount levels merit review:** Discount levels of 30% and above showed negative aggregate profit in this dataset.
8. **December 2025 was the strongest month by sales:** Monthly sales reached $97,502.28.

These insights are descriptive findings from the available dataset. Additional investigation is needed before attributing results to a particular business cause.

## 16. Dashboard Development

The dashboard was developed using Streamlit and includes:

- Total Sales
- Total Profit
- Total Orders
- Units Sold
- Profit Margin
- Sales and profit by product category
- Top-selling products
- Sales and profit by region
- Monthly sales trend
- Sub-category profitability
- Business insights
- Category, region, segment and date filters
- Downloadable filtered data
- A view of the filtered dataset

The dashboard allows users to explore the data interactively instead of relying only on static reports.

## 17. Limitations

- The results depend on the accuracy and scope of the supplied dataset.
- Future-dated records were excluded from the analysis and retained separately for review.
- Aggregate results may hide differences between individual products or orders.
- Observed relationships between discounts and profit do not establish causation.
- The analysis describes historical records and does not constitute a forecast.

## 18. Conclusion

The Sales Data Analysis Dashboard project demonstrates the use of Python, Pandas, Matplotlib and Streamlit in a complete beginner-level data analysis workflow.

The project includes data quality checks, cleaning, KPI calculation, category and regional comparisons, monthly trends, product analysis, visualizations and an interactive dashboard.

The findings highlight strong Technology category performance, the West region's leading sales, and loss-making sub-categories that warrant further review. The dashboard provides an accessible way to explore these results and support data-informed business discussions.

## 19. Deliverables

- Original dataset.
- Cleaned dataset.
- Python analysis scripts.
- Data quality review output.
- Category, regional, monthly, product, sub-category and discount analysis outputs.
- Three static visualization charts.
- Interactive Streamlit dashboard.
- Business insights file.
- Dashboard screenshots.
- This project report.
- GitHub repository and presentation: to be completed.

## 20. Acknowledgement

I would like to thank my internship mentor and organization for providing this project opportunity. This project helped me practise data cleaning, analysis, visualization and dashboard development using Python.

---

**End of Report**
