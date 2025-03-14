
# 📊 HR Analytics Project - Understanding Attrition in HR

## 📌 Problem Statement
Every year, companies invest significant time and money in hiring and training employees. These training programs aim to enhance employee effectiveness. However, **HR Analytics** plays a crucial role beyond just improving performance. 

### 🔍 What is HR Analytics?
**Human Resource Analytics (HR Analytics)** applies analytical processes to an organization's HR department to improve employee performance and achieve a better return on investment. Instead of simply tracking employee efficiency, HR Analytics helps gather meaningful insights that drive strategic decision-making.

### ⚠️ Understanding Attrition in HR
**Attrition** in HR refers to the gradual loss of employees over time. High attrition rates can negatively impact organizations in various ways. HR professionals use **analytics** to design compensation programs, work culture initiatives, and motivation systems to **retain top employees**.

## 💡 Why is Employee Attrition a Concern?
Employee attrition can be **costly** for organizations due to:
- **Hiring & onboarding costs** – Job postings, interviews, and training
- **Loss of experience** – Frequent turnover leads to a lack of expertise
- **Customer dissatisfaction** – Clients prefer interacting with familiar employees
- **Productivity drop** – Frequent hiring leads to errors and inefficiencies

HR Analytics helps in **analyzing and predicting** attrition patterns, allowing businesses to take proactive measures.

---

## 🏗️ Project Structure
```bash
HR_Analytics_Attrition/
│
├── data/
│   ├── raw/
│   │   └── employee_data.csv        # Original dataset
│   ├── processed/
│   │   └── cleaned_employee_data.csv # Cleaned dataset after preprocessing
│   └── README.md                     # Dataset description
│
├── notebooks/
│   ├── 01_EDA.ipynb                  # Exploratory Data Analysis
│   ├── 02_Feature_Engineering.ipynb   # Feature Engineering and Data Processing
│   ├── 03_Model_Training.ipynb        # Building and evaluating models
│   ├── 04_Prediction.ipynb            # Using the trained model for predictions
│
├── src/
│   ├── data_preprocessing.py          # Script for data cleaning and processing
│   ├── model_training.py              # Script for model training & evaluation
│   ├── utils.py                        # Utility functions (visualization, metrics, etc.)
│   └── config.py                       # Configuration settings (paths, hyperparameters, etc.)
│
├── results/
│   ├── plots/                          # Saved plots (attrition trends, correlations, etc.)
│   ├── model_performance.txt           # Model evaluation metrics
│
├── tests/
│   ├── test_data_processing.py         # Unit tests for data preprocessing
│   ├── test_model_training.py          # Unit tests for model training
│
├── README.md                           # Project documentation (this file)
├── requirements.txt                     # List of dependencies
├── LICENSE                              # License details
└── .gitignore                           # Files and directories to ignore in Git
```

---


## 🎯 Objectives of the Project
- ✔️ Perform **Exploratory Data Analysis (EDA)** to identify attrition trends  
- ✔️ Apply **Feature Engineering** techniques to improve model performance  
- ✔️ Train **Machine Learning models** to predict employee attrition  
- ✔️ Interpret model results and provide **data-driven recommendations**  

---

## 🛠️ Technologies Used
- **Python** 🐍  
- **Pandas** 📊 – Data Manipulation  
- **Matplotlib & Seaborn** 📈 – Data Visualization  
- **Scikit-learn** 🤖 – Machine Learning  
- **XGBoost & Random Forest** 🌲 – Advanced ML models  

---

## 📊 Expected Outcomes
- ✅ Identify **key factors** contributing to employee attrition  
- ✅ Develop a **predictive model** to assess attrition risk  
- ✅ Provide **recommendations** to HR for reducing attrition

---

##Heroku link:

https://attrition-rate-pred.herokuapp.com/
