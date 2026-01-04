import pandas as pd
import ollama

df = pd.read_excel("../data/sales_summary.xlsx")
text = df.to_string()

prompt = f"""
You are a business data analyst.
Analyze this sales summary and give 3 key business insights:

{text}
"""

response = ollama.chat(
    model="tinyllama",
    messages=[{"role": "user", "content": prompt}]
)

print("\nAI BUSINESS INSIGHTS:\n")
print(response['message']['content'])
