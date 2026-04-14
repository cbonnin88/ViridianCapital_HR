![Project Status](https://img.shields.io/badge/Status-Completed-success)
![Data Size](https://img.shields.io/badge/Dataset-12,500+_Employees-blue)
![Stack](https://img.shields.io/badge/Stack-Snowflake_|_dbt_cloud_|_Python_|_SQL_|_Polars_&_Pandas_|_Scikit--Learn_|_Streamlit_|_Google_Sheets-red)

# 🌿 Viridian Capital: Predictive Talent & ESG Analytics Platform

An end-to-end Modern Data Stack (MDS) project simulating a global investment firm's human capital management. This platform integrates automated data engineering, dbt transformations, and a machine learning-powered Streamlit application to identify and predict high-performing ESG (Environmental, Social, and Governance) talent.



---

## 🚀 Project Overview

Viridian Capital manages a global workforce of 12,500+ employees. This project was built to solve a specific business problem: **How can we identify and predict which employees will drive our sustainability (ESG) initiatives?**

### Key Features:
* **Synthetic Data Engine:** Python-based generation of 12,500+ records with realistic salary, demographic, and performance correlations.
* **dbt Transformation Layer:** Modular SQL modeling to calculate "Green Bonuses," currency conversions, and performance tiers.
* **Executive Dashboarding:** Live Snowflake Snowsight dashboards for C-suite payroll and equity overviews.
* **ML Talent Predictor:** A Streamlit-native application using **Scikit-Learn** and **Polars** to predict "ESG Leadership Propensity" with 85%+ accuracy.

---

## 🛠️ The Tech Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Data Warehouse** | **Snowflake** | Centralized cloud data storage and compute. |
| **Transformation** | **dbt Cloud** | T-shaped data modeling and documentation. |
| **Languages** | **Python & SQL** | Data generation (Snowpark) and ML modeling. |
| **Data Processing**| **Polars & Pandas** | High-performance dataframe manipulation. |
| **Data Science** | **Scikit-Learn** | Random Forest Classification for predictive analytics. |
| **Visualization** | **Streamlit** | Interactive "Talent Explorer" web application. |
| **Ad-Hoc Analysis** | **Google Sheets** | Ad-hoc analysis and data visualizations. |

---

## 📈 Data Pipeline Architecture

1.  **Extract & Load (EL):** Python scripts generate raw employee data and stage it directly into Snowflake tables.
2.  **Transform (T):** dbt models clean raw data, handle `NULL` values, and join disparate tables into a unified `fct_compensation_summary`.
3.  **Analyze (BI):** SQL-based analytics identify pay gaps and budget variances across global offices (London, Paris, Berlin, Madrid).
4.  **Predict (ML):** A Random Forest model analyzes historical patterns (Age, Department, Band) to predict future ESG leaders.

---

## 🖥️ Streamlit App: "The Talent Explorer"

The final deliverable is an interactive app that allows HR Directors to:
* **Filter** employees by office, department, and ESG score in real-time.
* **Model** "What-if" scenarios for bonus distributions.
* **Predict** the likelihood of a new candidate becoming an ESG Leader.
* **Export** filtered results directly to CSV for localized reporting.



---

## 💡 Key Business Insights

* **Sustainability ROI:** Employees in the "Engineering" department showed a 15% higher correlation between salary incentives and ESG score improvements.
* **Budget Impact:** Implementing a 5% "Green Bonus" for scores > 80 would require a €2.4M increase in the FY2026 payroll budget.
* **Predictive Accuracy:** Age and Departmental Level were the strongest predictors of ESG leadership, outperforming salary as a motivator.

---

## 📂 How to Run
1.  **Snowflake:** Execute the `data_generation.py` script in a Snowflake Python Worksheet.
2.  **dbt:** Run `dbt build` to generate the modeled tables.
3.  **Streamlit:** Create a new Streamlit app in Snowflake and paste the provided `app.py` code.
4.  **Packages:** Ensure `scikit-learn`, `pandas`, and `plotly` are installed in the Snowflake environment.

---
**Author:** [Christopher Bonnin](https://www.linkedin.com/in/christopher-bonnin-a08a95197/)  
**Role:** Analytics Engineer 
