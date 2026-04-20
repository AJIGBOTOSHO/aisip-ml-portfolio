readme = """# 🌍 2014-2016 Western Africa Ebola Outbreak — EDA
**Africa AI Hub | AISIP Cohort 1 | Week 5**
**Scholar:** Ajigbotosho | **Pathway:** Pathway 4 — AI Engineering & Development

---

## Dataset
- **Source:** Kaggle — imdevskp/ebola-outbreak-20142016-complete-dataset
- **File Used:** ebola_2014_2016_clean.csv
- **Coverage:** Guinea, Sierra Leone, Liberia | 2014-2016
- **Records:** 2,485 rows | 4 columns

---

## Project Structure 

---

## EDA Steps
| Step | Description |
|------|-------------|
| 1 | Downloaded dataset via Kaggle API |
| 2 | Loaded with Pandas — explored shape, info, describe |
| 3 | Cleaned data types, fixed cumulative drops, added derived columns |
| 4 | Created 6 visualisations |
| 5 | Extracted insights and policy recommendations |

---

## Visualisations & Key Findings

| # | Chart | Key Finding |
|---|-------|-------------|
| 1 | Histogram | Cases were bimodal — outbreak had two distinct phases |
| 2 | Scatter | Strong linear relationship between cases and deaths |
| 3 | Bar Chart | Sierra Leone had most cases. Liberia had most deaths |
| 4 | Box Plot | Sierra Leone data was most inconsistent — reporting gaps |
| 5 | Heatmap | Fatality rate dropped as cases rose — response improved |
| 6 | Time Trend | Critical surge window was Sept-Dec 2014 across all 3 countries |

---

## Key Insight For AI Engineers
The same gap that allowed Ebola to overwhelm West African health
systems — the absence of Africa-trained, Africa-validated health AI
tools — is the same gap that today allows biased diagnostic AI systems
to enter Nigerian hospitals unchallenged. African health data must
drive African health solutions.

---

## Recommendations Summary
- Act at first sign of surge — not after hospitals are full
- Build healthcare capacity before crisis hits
- Standardise digital health reporting across all facilities
- Create regional early warning systems across borders
- Train AI tools on African data for African health contexts

---

*Built on African soil. For African problems.*
*Africa AI Hub AISIP Cohort 1 | Pathway 4 — AI Engineering & Development*
"""

with open("README.md", "w") as f:
    f.write(readme)

print("README.md saved successfully")