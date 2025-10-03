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

# Step 6: Define threshold for low movement (< 10 units/month)
low_movement = avg_sales[avg_sales["avg_monthly_sales"] < 10]

# Step 7: Save results to Excel
with pd.ExcelWriter("low_movement_results.xlsx") as writer:
    avg_sales.to_excel(writer, sheet_name="Average_Monthly_Sales", index=False)
    low_movement.to_excel(writer, sheet_name="Low_Movement_Products", index=False)

print("✅ Analysis complete. Results saved in 'low_movement_results.xlsx'")

