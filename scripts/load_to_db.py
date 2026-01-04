import pandas as pd
from sqlalchemy import create_engine

# Read clean dataset
df = pd.read_excel("../data/clean_sales_data.xlsx")

# Connect to PostgreSQL
engine = create_engine("postgresql://postgres:postgres@localhost:5432/salesdb")

# Load data into table 'sales'
df.to_sql("sales", engine, if_exists="replace", index=False)

print("✔ Clean data loaded into PostgreSQL database")
