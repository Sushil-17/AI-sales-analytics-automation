import pandas as pd

# 1. Load raw dataset
df = pd.read_excel("../data/sales_dirty_dataset.xlsx")

# 2. Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 3. Remove duplicate orders using OrderID as business key
df = df.drop_duplicates(subset=["orderid"])

# 4. Remove rows with missing critical fields
df = df.dropna(subset=["orderid", "product", "quantity", "unitprice", "revenue", "region"])

# 5. Fix datatypes
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["unitprice"] = pd.to_numeric(df["unitprice"], errors="coerce")
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")

df = df.dropna(subset=["quantity", "unitprice", "revenue"])

# 6. Remove invalid business values
df = df[(df["quantity"] > 0) & (df["unitprice"] > 0) & (df["revenue"] > 0)]

# 7. Logical business validation
df["calculated_revenue"] = df["quantity"] * df["unitprice"]

# keep only rows where revenue matches calculated revenue
df = df[df["revenue"] == df["calculated_revenue"]]

# drop helper column
df = df.drop(columns=["calculated_revenue"])

# 8. Create KPI summary tables

#  Create advanced KPI summary tables

# Revenue & Orders by product
product_kpi = (
    df.groupby("product")
      .agg(
          Total_Revenue=("revenue", "sum"),
          Total_Quantity=("quantity", "sum"),
          Orders=("orderid", "count"),
          Avg_Order_Value=("revenue", "mean")
      )
      .reset_index()
)

# Revenue & Orders by region
region_kpi = (
    df.groupby("region")
      .agg(
          Total_Revenue=("revenue", "sum"),
          Orders=("orderid", "count"),
          Avg_Order_Value=("revenue", "mean")
      )
      .reset_index()
)

# Monthly revenue trend
df["orderdate"] = pd.to_datetime(df["orderdate"])
df["month"] = df["orderdate"].dt.to_period("M").astype(str)

monthly_kpi = (
    df.groupby("month")
      .agg(
          Total_Revenue=("revenue", "sum"),
          Orders=("orderid", "count"),
          Avg_Order_Value=("revenue", "mean")
      )
      .reset_index()
)


# 9. Export clean dataset & KPIs
df.to_excel("../data/clean_sales_data.xlsx", index=False)

with pd.ExcelWriter("../data/sales_kpi_report.xlsx", engine="openpyxl") as writer:
    product_kpi.to_excel(writer, sheet_name="Revenue_by_Product", index=False)
    region_kpi.to_excel(writer, sheet_name="Revenue_by_Region", index=False)
    monthly_kpi.to_excel(writer, sheet_name="Monthly_Revenue", index=False)

print("✔ Data cleaned and KPI report generated successfully!")
