📦 LOW MOVEMENT PRODUCT IDENTIFIER PROJECT

This project identifies low-selling or slow-moving products from electronic sales data.
It helps businesses understand which items have poor sales performance, so they can plan discounts, promotions, or stock reductions.
The analysis is performed using Python (Pandas) and the results are exported to Excel.
An optional Power BI dashboard can visualize low vs high movement items.

📌 Project Overview

Collected electronic sales data (20 products)

Performed monthly grouping and average sales analysis using Python

Defined threshold to identify low movement (<10 units/month) products

Saved final reports into Excel

(Optional) Built a Power BI dashboard to visualize product performance

🛠 Tools & Technologies Used
Tool	Purpose
Python (Pandas)	Data analysis & grouping
Excel	Input and output data
Power BI (optional)	Data visualization
Git & GitHub	Version control and hosting
🗂 Folder Structure
LowMovementProductIdentifier/
├── data/
│   ├── electronics_sales.xlsx          # Input data
│   └── low_movement_results.xlsx       # Output results
│
├── src/
│   └── analysis.py                     # Python script
│
├── dashboard/
│   └── low_movement_dashboard.pbix     # Optional Power BI file
│
├── README.md                           # Project documentation
├── requirements.txt                    # Python libraries
└── .gitignore

📊 Sample Data
product_id	product_name	date	quantity_sold
E001	Laptop Dell	05-01-2025	12
E002	Laptop HP	06-01-2025	18
E003	Mobile Samsung	07-01-2025	15
E004	Mobile iPhone	08-01-2025	25
E005	Headphones Sony	09-01-2025	5
E006	Headphones JBL	10-01-2025	7
E007	Smartwatch Mi	11-01-2025	18
E008	Smartwatch Apple	12-01-2025	10
E009	TV Samsung	13-01-2025	20
E010	TV LG	14-01-2025	22
E011	Keyboard Logitech	03-02-2025	6
E012	Mouse Dell	04-02-2025	9
E013	Tablet Lenovo	05-02-2025	11
E014	Tablet Apple	06-02-2025	13
E015	Printer HP	07-02-2025	4
E016	Printer Canon	08-02-2025	3
E017	Camera Nikon	01-03-2025	8
E018	Camera Sony	02-03-2025	6
E019	Speaker Bose	03-03-2025	5
E020	Speaker JBL	04-03-2025	7
🧮 Python Code (analysis.py)
import pandas as pd

# Step 1: Load Excel file
df = pd.read_excel("electronics_sales.xlsx")

# Step 2: Convert 'date' column to proper datetime
df["date"] = pd.to_datetime(df["date"])

# Step 3: Create month column for grouping
df["month"] = df["date"].dt.to_period("M")

# Step 4: Calculate monthly sales per product
monthly_sales = df.groupby(["product_id", "product_name", "month"])["quantity_sold"].sum().reset_index()

# Step 5: Calculate average monthly sales per product
avg_sales = monthly_sales.groupby(["product_id", "product_name"])["quantity_sold"].mean().reset_index()
avg_sales = avg_sales.rename(columns={"quantity_sold": "avg_monthly_sales"})

# Step 6: Define threshold for low movement (<10 units/month)
low_movement = avg_sales[avg_sales["avg_monthly_sales"] < 10]

# Step 7: Save results to Excel
with pd.ExcelWriter("low_movement_results.xlsx") as writer:
    avg_sales.to_excel(writer, sheet_name="Average_Monthly_Sales", index=False)
    low_movement.to_excel(writer, sheet_name="Low_Movement_Products", index=False)

print("✅ Analysis complete. Results saved in 'low_movement_results.xlsx'")

📈 Analysis Performed

Converted date column to datetime format

Grouped data by product and month

Calculated average monthly sales for each product

Identified low movement products (avg_monthly_sales < 10)

Exported both sheets (average & low movement) into one Excel file

💡 Key Learnings

How to clean and analyze sales data using Python & Pandas

How to calculate sales trends and movement rate

How to export multiple DataFrames to one Excel file using ExcelWriter

How to identify slow-moving products for business optimization

🚀 How to Run This Project

Clone the repo:

git clone https://github.com/yourusername/low-movement-product-identifier


Place your electronics_sales.xlsx file in the project folder.

Install dependencies:

pip install -r requirements.txt


Run the analysis script:

python src/analysis.py


View results in low_movement_results.xlsx.

🧾 requirements.txt
pandas
openpyxl

📊 Optional Power BI Dashboard

If you create a Power BI file (low_movement_dashboard.pbix):

Import low_movement_results.xlsx

Add visuals:

Bar chart → Product vs Avg Monthly Sales

Table → Low movement products

Card → Total low movement count

✅ Project Summary:

Identified low-movement products using Python-based data analysis.
Calculated average monthly sales and exported reports to Excel.
Optional dashboard built in Power BI for visual insights.
