# 💠 Frugal PCOS Risk Score (FrugalScore2)

A lightweight, OPD-friendly clinical risk scoring tool for **screening Polycystic Ovary Syndrome (PCOS)** using only three simple predictors.  
Developed for rapid use in low-resource settings and validated using logistic regression (AUC = 0.78).

---

## 📌 Features
- Streamlit-based interactive web app  
- Uses **3 clinical questions** to compute a validated frugal score  
- Provides automated **risk interpretation** (Low / Moderate / High)  
- Includes a transparent scoring table and methodology  
- Fully offline, stores **no patient data**

---

## 🧮 Scoring System
| Variable | Points |
|---------|--------|
| Age < 25 years | +1 |
| Hirsutism (FG ≥ 8) | +1 |
| Moderate/Severe Acne | +2 |

**Score Range:** 0–4  
**Optimal Cut-off:** ≥ 1.5  
- Sensitivity: 0.62  
- Specificity: 0.83  
- AUC: 0.784 (95% CI: 0.69–0.87)




