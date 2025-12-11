import streamlit as st

# ----------------------------
# APP METADATA
# ----------------------------
st.set_page_config(page_title="Frugal PCOS Risk Score", page_icon="💠", layout="centered")

st.title("💠 Frugal PCOS Risk Score")
st.caption("Developed using validated clinical predictors of PCOS in South Asian women")

st.markdown("""
This tool uses **three simple clinical questions** to estimate the probability of PCOS,
based on your validated logistic regression model (AUC = 0.78).

> ⚠️ *This tool is for screening and educational use only.  
> It does not replace professional diagnosis.*
""")

# ----------------------------
# USER INPUTS
# ----------------------------
st.subheader("Answer these quick questions:")

age = st.radio("1️⃣ Age below 25 years?", ["No", "Yes"])
fgs = st.radio("2️⃣ Hirsutism present (Ferriman–Gallwey ≥ 8)?", ["No", "Yes"])
acne = st.radio("3️⃣ Acne severity moderate/severe?", ["No", "Yes"])

# ----------------------------
# COMPUTE SCORE
# ----------------------------
score = 0
if age == "Yes":
    score += 1
if fgs == "Yes":
    score += 1
if acne == "Yes":
    score += 2

st.divider()
st.metric(label="FrugalScore II", value=score)

# ----------------------------
# INTERPRETATION
# ----------------------------
if score < 2:
    st.success("🟢 **Low risk** of PCOS — maintain healthy habits and regular follow-up.")
elif score < 4:
    st.warning("🟠 **Moderate risk** — consider screening by clinician.")
else:
    st.error("🔴 **High risk** — consult an endocrinologist for detailed evaluation.")

# ----------------------------
# OPTIONAL OUTPUT DETAILS
# ----------------------------
st.markdown("---")
st.markdown("""
### How it works
| Variable | Points |
|-----------|---------|
| Age < 25 y | +1 |
| Hirsutism (FG ≥ 8) | +1 |
| Moderate/Severe Acne | +2 |

**Total Score Range:** 0–4  
**Optimal Cut-off:** ≥ 1.5 (Sensitivity = 0.73, Specificity = 0.45)

Developed using logistic regression and validated with Kaggle PCOS dataset  
(AUC = 0.784, 95% CI 0.69–0.87).
""")

st.info("© 2025 Dr. Suman Kotwal et al. | Frugal AI Lab, India")

# ----------------------------
# FOOTER
# ----------------------------
st.markdown(
    "<small>Built with ❤️ using Streamlit. "
    "For academic use only — do not store patient identifiers.</small>",
    unsafe_allow_html=True
)
