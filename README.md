🎓 U.S. Higher Education Dashboard
Analyzing 2,700+ Institutions to Surface ROI, Equity Gaps, and State-Level Disparities

📌 Project Overview
An end-to-end Business Intelligence solution built on real U.S. Department of Education data. This dashboard helps university administrators, policy makers, and prospective students answer three fundamental questions:

Is college worth the investment? (ROI analysis across institution types)
Which states and schools deliver the best outcomes? (Geographic performance analysis)
Who gets left behind? (Equity and affordability analysis for low-income and first-generation students)

The project covers the full data pipeline — raw government data → Python cleaning → star schema modeling → 5-page interactive Power BI dashboard.

🔑 Key Findings

📊 Public universities deliver 6.5x ROI vs. 2.5x for Private For-Profit and 1.5x for Private Nonprofit schools
💸 Average median debt is $18.5K while average 10-year earnings reach $49.8K — suggesting college pays off on average, but outcomes vary widely by institution
🗺️ Rhode Island, Connecticut, and Massachusetts lead the nation in graduation rates (60%+), while the national average sits at just 49.7%
🏫 1,150 schools (42%) offer in-state tuition below $10,000/year — affordable options exist but are geographically concentrated
⚖️ Puerto Rico serves the highest share of low-income students (81% Pell Grant recipients), highlighting significant geographic equity gaps
🎓 Private For-Profit schools serve the most first-generation students (50%) yet deliver the lowest graduation rates — a critical policy concern


📸 Dashboard Pages
Page 1 — Executive Summary
"What is the overall state of American higher education?"
High-level national snapshot: 2,745 institutions, 13M total enrolled students, average graduation rate, tuition, debt, and earnings. Includes institution type breakdown and state-level institution counts.
<img width="2064" height="1195" alt="image" src="https://github.com/user-attachments/assets/47303bcb-d764-464d-8cd4-f06d163deffd" />
Page 2 — Institution Analysis
"Which individual schools offer the best value?"
Searchable, sortable table of all institutions with graduation rate, tuition, debt, and earnings. Scatter plot of tuition vs. earnings reveals value outliers. Top 15 schools by median earnings ranked.
<img width="2065" height="1191" alt="image" src="https://github.com/user-attachments/assets/4b5f420a-6897-4a67-afed-e1b99158600d" />
Page 3 — State Level Analysis
"How does geography shape educational outcomes?"
Choropleth map colored by graduation rate. State rankings by graduation rate, earnings, and in-state tuition — revealing that the highest-performing states are not always the most affordable.
<img width="2073" height="1203" alt="image" src="https://github.com/user-attachments/assets/84325d9e-23b2-42db-8752-e9ab7806fbb5" />
Page 4 — Student Outcomes
"Is college actually worth it financially?"
ROI comparison across institution types. Debt vs. earnings scatter plot. 10-year earnings progression. Public schools dominate ROI despite lower tuition — a counterintuitive finding with major policy implications.
<img width="2064" height="1204" alt="image" src="https://github.com/user-attachments/assets/ec6afbf9-ec9f-47ad-a55d-c859ef4e077d" />
Page 5 — Affordability & Access
"Who gets left behind in American higher education?"
Pell Grant and first-generation student representation by institution type and state. Poverty rate vs. graduation rate relationship. Reveals systemic equity gaps between institution types and geographic regions.
<img width="2070" height="1201" alt="image" src="https://github.com/user-attachments/assets/2acb17cb-e772-4a4a-9efe-08c5fbb3e71a" />
🛠️ Tech Stack
LayerTools UsedData Cleaning & TransformationPython, PandasData ModelingStar Schema (Power BI Model View)Metrics & KPIsDAX (20 custom measures)VisualizationPower BI DesktopVersion ControlGit, GitHub

📂 Project Structure

us-higher-education-dashboard/
├── raw_data/
│   └── Most-Recent-Cohorts-Institution.csv    # Source: U.S. Dept. of Education
├── cleaned_data/
│   ├── cleaned_institutions.csv               # Cleaned master dataset
│   ├── dim_institution.csv                    # Dimension: school attributes
│   ├── dim_location.csv                       # Dimension: state-level info
│   └── fact_institutions.csv                  # Fact: all metrics and KPIs
├── scripts/
│   ├── 01_explore_data.py                     # Initial data exploration
│   ├── 02_clean_transform.py                  # Cleaning, filtering, ROI calc
│   └── 03_build_star_schema.py                # Star schema table creation
├── screenshots/
│   ├── page1_executive_summary.png
│   ├── page2_institution_analysis.png
│   ├── page3_state_analysis.png
│   ├── page4_student_outcomes.png
│   └── page5_affordability_access.png
├── Higher_Education_Dashboard.pbix            # Power BI file
└── README.md

⚙️ Data Pipeline
Step 1 — Data Acquisition
Downloaded the Most Recent Cohorts Institution dataset from the U.S. Department of Education College Scorecard. Raw file contains 6,000+ institutions and 3,000+ columns.
Step 2 — Data Cleaning (Python / Pandas)

Selected 27 relevant columns from 3,000+
Converted all numeric fields from object type using pd.to_numeric(errors='coerce')
Created human-readable labels for institution control type and degree type
Combined 4-year and sub-4-year graduation rate columns using combine_first()
Filtered out unclassified institutions (PREDDEG == 0) and schools with zero enrollment
Dropped rows missing critical metrics: graduation rate, tuition, earnings, and debt — preserving only institutions with complete, analyzable records
Calculated custom ROI metric: median_earnings_10yr / tuition_in_state

Step 3 — Star Schema Modeling
Built three normalized tables for Power BI:

dim_institution: school identity and classification attributes
dim_location: state-level lookup table with surrogate location_id key
fact_institutions: all numeric metrics joined to both dimensions

Relationships built in Power BI Model View on institution_id and location_id.
Step 4 — DAX Measures (20 total)
Custom measures across 7 categories:
CategoryMeasuresSummaryTotal Institutions, Total EnrollmentPerformanceAvg Graduation Rate, Avg Retention Rate, Avg Admission RateFinancialAvg Tuition In-State, Avg Tuition Out-of-State, Avg Median Debt, Avg Grad DebtEarningsAvg Earnings 6yr, Avg Earnings 10yr, Avg ROIDemographicsAvg Pell Grant %, Avg First Gen %, Avg Female %ContextualAvg Poverty Rate, Avg Unemployment Rate, Avg Federal Loan %RankingsHigh ROI Schools (ROI > 2), Affordable Schools (Tuition < $10K)

📊 Data Source
U.S. Department of Education — College Scorecard

URL: https://collegescorecard.ed.gov/data/
Dataset: Most Recent Cohorts — Institution Level
Coverage: All Title IV participating institutions in the United States
Includes: enrollment, tuition, graduation rates, post-graduation earnings, debt, and student demographics

This is real government data, not a synthetic or Kaggle dataset.

🚀 How to Run This Project

Download the College Scorecard dataset from the link above
Place the CSV in the raw_data/ folder
Run the Python scripts in order: 01 → 02 → 03
Open Higher_Education_Dashboard.pbix in Power BI Desktop
Update the data source path to point to your local cleaned_data/ folder
Refresh the data — all visuals will populate automatically

Requirements: Python 3.8+, Pandas, Power BI Desktop (free)

👤 Author
Naga Vamsi Chaitanya Pammi

LinkedIn: www.linkedin.com/in/nagapammi
Email: naga.pammi@outlook.com


Built as a portfolio project demonstrating end-to-end BI development using real U.S. government data.
