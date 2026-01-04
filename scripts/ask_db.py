import ollama
import re
from sqlalchemy import create_engine, text

engine = create_engine("postgresql://postgres:postgres@localhost:5432/salesdb")

question = input("Ask business question: ")

prompt = f"""
You are a PostgreSQL expert.

ONLY generate a valid SQL query for table named "sales".
Do NOT use any other tables.
Do NOT add explanations or labels.

Table schema:
sales(orderid, orderdate, customerid, product, category, quantity, unitprice, revenue, region, paymentmode, returned)

Question: {question}
"""

raw_sql = ollama.chat(
    model="tinyllama",
    messages=[{"role": "user", "content": prompt}]
)["message"]["content"]

# Remove everything except SQL
sql = re.search(r"(SELECT[\s\S]+;)", raw_sql, re.IGNORECASE)
if not sql:
    print("AI failed to generate valid SQL.")
    print(raw_sql)
    exit()

sql = sql.group(1)

print("\nGenerated SQL:\n", sql)

with engine.connect() as conn:
    result = conn.execute(text(sql))
    for row in result.fetchmany(10):
        print(row)
