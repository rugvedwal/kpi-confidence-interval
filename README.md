# kpi-confidence-interval
Streamlit calculator that computes ROAS confidence intervals for paid media campaigns

# KPI Confidence Interval – Streamlit App

A statistical calculator that computes the confidence interval for ROAS (Return on Ad Spend) using conversion data from your paid media campaigns. Built with Streamlit and matplotlib, this app helps digital marketers determine if their ad results are statistically significant.

**🔗 Live App:** [https://roascalculator-b814fdda8a37.herokuapp.com/](https://roascalculator-b814fdda8a37.herokuapp.com/)

---

## 📌 Features

- Calculate **ROAS** based on product price, CPC, clicks, and conversions
- Computes a **confidence interval** for ROAS using binomial distribution logic
- Visualizes ROAS and CI with a horizontal error bar chart
- Allows you to select **confidence level** (50%–99%)
- Detects and handles invalid input (e.g., conversions > clicks)

---

## 📊 Why This Matters

Many marketers use ROAS to gauge ad success, but they often overlook **statistical significance**.  
This app answers the question:

> “Are my ad results real or just random noise?”

By calculating a confidence interval for ROAS, it helps determine if your current campaign data is strong enough to declare a winner.

---

## 🧠 Core Logic

- **Conversion Rate** = Conversions / Clicks  
- **ROAS** = (Conversions × Product Price) / (Clicks × CPC)  
- **Confidence Interval** computed using:
  - Standard error of a binomial proportion
  - Margin of error from a normal distribution
  - Adjusted upper/lower bounds for ROAS

---

## 📦 Tech Stack

- Python
- Streamlit
- NumPy
- Matplotlib

---

## 🚀 Getting Started Locally

### 1. Clone the repo

```bash
git clone https://github.com/rugvedwal/kpi-confidence-interval.git
cd kpi-confidence-interval
