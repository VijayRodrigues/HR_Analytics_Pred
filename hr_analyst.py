import pandas as pd
import numpy as np
import pickle

df = pd.read_csv('hr_analytics_dataset.csv')

from sklearn.preprocessing import LabelEncoder
lab_enc = LabelEncoder()

df["Attrition"] = lab_enc.fit_transform(df["Attrition"])
df["BusinessTravel"] = lab_enc.fit_transform(df["BusinessTravel"])
df["Department"] = lab_enc.fit_transform(df["Department"])
df["EducationField"] = lab_enc.fit_transform(df["EducationField"])
df["Gender"] = lab_enc.fit_transform(df["Gender"])
df["JobRole"] = lab_enc.fit_transform(df["JobRole"])
df["MaritalStatus"] = lab_enc.fit_transform(df["MaritalStatus"])
df["Over18"] = lab_enc.fit_transform(df["Over18"])
df["OverTime"] = lab_enc.fit_transform(df["OverTime"])


from scipy.stats import zscore
z_score = zscore(df[['DailyRate','HourlyRate','MonthlyIncome', 'MonthlyRate','PercentSalaryHike']])
abs_zscore = np.abs(z_score)
filtering_entry = (abs_zscore < 3).all(axis=1)
df = df[filtering_entry]


X = df.drop(['Attrition','MonthlyIncome','EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours'], axis = 1)
y = df['Attrition']


from imblearn.over_sampling import SMOTE
SM = SMOTE()
x_over, y_over = SM.fit_resample(X,y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_over, y_over, test_size=0.30, random_state = 200)


from sklearn.linear_model import LogisticRegression
mod_log_reg = LogisticRegression(intercept_scaling= 5, max_iter= 70, multi_class="ovr",
                                 penalty= "l1", solver= "liblinear", tol =0.001)

mod_log_reg.fit(X_train,y_train)


pickle.dump(mod_log_reg , open('HrAnalyst.pkl', 'wb'))