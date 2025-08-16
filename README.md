# 💻 Laptop Price Prediction & Statistical Analysis  

This project explores **laptop prices** through **data analysis, hypothesis testing, and machine learning**.  
It aims to understand the key factors influencing laptop prices and to build predictive models for price estimation.  

---

## 📌 Objectives
- Perform **Exploratory Data Analysis (EDA)** to identify patterns in laptop features vs. price.  
- Apply **statistical hypothesis tests** (Z-test, T-test, ANOVA, Chi-square) for feature significance.  
- Build and evaluate **ML regression models** for price prediction.  
- Provide **business insights** on what drives laptop pricing.  

---

## 📂 Dataset
- **Source**: Kaggle Laptop Price dataset (or custom dataset used in notebook).  
- **Features**: Company, Type, RAM, GPU, CPU, Storage, Weight, OS, Screen size, Touchscreen, etc.  
- **Target Variable**: `Price`  

---

## 🔎 Exploratory Data Analysis
- Distribution of laptop prices.  
- Feature correlations (RAM, CPU speed, brand).  
- Visualization of categorical vs. numerical features.  
- Outlier detection and treatment.  

---

## 📊 Statistical Analysis
This notebook covers **hypothesis testing** methods:  

- **Z-test** → Testing population mean/proportion assumptions.  
- **T-test** → One-sample, two-sample, and paired tests for feature comparison.  
- **Chi-square test** → Testing categorical feature independence (e.g., Brand vs. OS).  
- **ANOVA** → Comparing mean prices across multiple laptop brands/types.  

✅ Helps identify whether differences in price are **statistically significant** or just random variation.  

---

## 🤖 Machine Learning Models
Implemented regression models:  
- **Linear Regression**  
- **Ridge & Lasso Regression**  
- **Random Forest Regressor**  
- **XGBoost Regressor**  

✅ Model evaluation with **R², MAE, RMSE**.  
✅ Hyperparameter tuning for optimized predictions.  

---

## 📈 Key Insights
- RAM size and CPU speed are strong predictors of laptop price.  
- Touchscreen and GPU presence significantly impact price.  
- Certain brands show statistically higher average prices (**ANOVA result**).  
- Ensemble models (Random Forest, XGBoost) outperform simple linear regression.  

---

## 🛠️ Tech Stack
- **Language**: Python  
- **Libraries**: pandas, numpy, matplotlib, seaborn, scipy, scikit-learn, xgboost  
- **Environment**: Jupyter Notebook  

---

## 🚀 How to Run
1. Clone this repo:  
   ```bash
   git clone https://github.com/yourusername/Laptop-Price-Prediction.git
   cd Laptop-Price-Prediction
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the notebook:  
   ```bash
   jupyter notebook Laptop_price.ipynb
   ```

---

## 📌 Learning Outcomes
- Perform **EDA & visualization** on real-world datasets.  
- Apply **hypothesis testing (Z-test, T-test, ANOVA, Chi-square)** to validate assumptions.  
- Build & compare **ML regression models**.  
- Translate data insights into **business-level recommendations**.  

---

## 📜 License
This project is open-source and available under the **MIT License**.  
