# AI-Powered Sales Analytics Automation System

An end-to-end sales analytics automation pipeline that transforms messy enterprise Excel data into analytics-ready datasets, KPI dashboards, and business insights with zero manual effort.

---

## 🚀 Business Problem

Sales teams often receive inconsistent, duplicate and error-prone Excel files that require heavy manual cleaning before analysis.  
This project automates the entire pipeline — eliminating manual work and enabling faster decision-making.

---

## 🛠 Solution Overview

Raw Excel Files  
→ Automated Data Cleaning & Validation  
→ KPI Report Generation  
→ PostgreSQL Database Integration  
→ AI-Powered Business Insights

---

## ⭐ Key Features

- Automated ingestion of raw Excel sales files  
- Data cleaning: duplicate removal, null handling, datatype fixing  
- Business rule validation (Revenue = Quantity × Unit Price)  
- Advanced KPI generation using pandas `.agg()`  
- Multi-sheet Excel KPI report generation  
- PostgreSQL integration for analytics-ready storage  
- Local AI-powered business insight generation using TinyLLaMA  

---

## 🧰 Tech Stack

- Python  
- pandas  
- PostgreSQL  
- SQLAlchemy  
- OpenPyXL  
- Ollama (TinyLLaMA)  

---

## 📁 Folder Structure

```text
ai_data/
├── data/
│ ├── sales_dirty_dataset.xlsx
│ ├── clean_sales_data.xlsx
│ └── sales_kpi_report.xlsx
└── scripts/
	├── excel_automation.py
	├── ai_insights.py
	└── load_to_db.py
```


---

## ▶ How to Run

1. Place raw Excel files inside `data/raw`  
2. Run `excel_automation.py` to clean data & generate KPI reports  
3. Run `load_to_db.py` to load cleaned data into PostgreSQL  
4. Run `ai_insights.py` to generate AI-powered business insights  

---

## 📊 Outcome

- Reduced manual reporting effort by over **90%**
- Created a scalable analytics pipeline usable for any future datasets


