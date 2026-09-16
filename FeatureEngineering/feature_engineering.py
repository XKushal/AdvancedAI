#Feature selection and Feature Engineering

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Loan approval Prediction

#step 1: data collection
data = pd.DataFrame({
    "customer_id": ["C001", "C002", "C003", "C004", "C005",
                    "C006", "C007", "C008", "C009", "C010"],

    "age": [25, 32, np.nan, 45, 29,
            41, 38, 27, 52, 31],

    "income": [45000, 75000, 38000, 120000, np.nan,
               95000, 68000, 42000, 500000, 58000],

    "debt": [5000, 12000, 15000, 10000, 25000,
             18000, 9000, 3000, 70000, 8000],

    "city": ["New York", "Chicago", "Boston", "New York", "Chicago",
             "Boston", "New York", "Chicago", "Boston", "New York"],

    "credit_score": [680, 720, 640, 760, 610,
                     700, 735, 690, 780, 710],

    "application_date": [
        "2026-01-10", "2026-01-15", "2026-02-03", "2026-02-20", "2026-03-01",
        "2026-03-18", "2026-04-02", "2026-04-14", "2026-05-01", "2026-05-17"
    ],

    "approved": [1, 1, 0, 1, 0,
                 1, 1, 1, 1, 1]
})

#step 2: data cleanup/ Imputation
print(f"\ninitial stage dataset:\n {data}")
numeric_dataset = data.select_dtypes(include='number')
missing_values = data.isnull().sum()

#loop through all columns
for column in data:
    #check only missing columns, reduce lookups
    if missing_values[column] > 0:
        #check if this column is numeric
        if column in numeric_dataset.columns:
            # Fill missing numeric values with the median of that column
            data[column] = data[column].fillna(data[column].median())
        else:
            # Fill missing categorical values with the most frequent value
            data[column] = data[column].fillna(
                data[column].value_counts().idxmax()
            )

print(f"\ndataset after cleanup/imputation: \n {data}")

#step 3: feature engineering

#once dataset is clean and ready, create new feature DTI
#debt_to_income = float(debt/income)
#pandas specialty to dicetly calculate against per column/row
data["debt_to_income"] = data["debt"]/data["income"]
print(f"\ndataset after feature engineering: \n {data}")

#step 4: one hot-encoding

#now implementing one hot-encoding
encoded_columns = pd.get_dummies(data['city'])
data = data.join(encoded_columns)
data = data.drop("city", axis=1)

print(f"\ndataset after one hot-encoding: \n {data}")

#step 5: Feature selection

#remove unwanted feature
data = data.drop("customer_id", axis=1)

#date manipulation (str ->  dtype: datetime64[us])
data["application_date"] = pd.to_datetime(data["application_date"])
data["application_month"] = data["application_date"].dt.month

data = data.drop("application_date", axis=1)

#outlier management
mean_income = data["income"].mean()
standard_deviation = data["income"].std()

upper_limit = mean_income + (2 * standard_deviation)
lower_limit = mean_income - (2 * standard_deviation)

outlier = data[(data["income"] > upper_limit) | (data["income"] < lower_limit) ]
data = data[(data["income"] < upper_limit) & (data["income"] > lower_limit) ]
data = data.reset_index(drop=True)
print(f"\noutlier: \n {outlier}")

print("\nWhich remaining features seem related to approved? pearson correlation\n")
correlation = data.corr(numeric_only=True)
print(correlation["approved"].sort_values(ascending=False))
feature_correlation = correlation["approved"].drop("approved").sort_values()

#graphical representation
feature_correlation.plot(kind="barh")
plt.title("Feature Correlation with Loan Approval")
plt.xlabel("Pearson Correlation")
plt.tight_layout()
plt.show()

#dropping least correlated feature
data = data.drop("application_month", axis=1)

print(f"\ndata after feature selection: \n {data}")

#step 6: scaling - using standarization here

columns_to_scale = data.select_dtypes(include="number").columns
for col in columns_to_scale:
    if col != "approved":
        data[col] = (data[col] - data[col].mean()) / data[col].std()

print(f"\ndata after Scaling using standarization: \n {data}")

'''
initial stage dataset:
   customer_id   age    income   debt      city  credit_score application_date  approved
0        C001  25.0   45000.0   5000  New York           680       2026-01-10         1
1        C002  32.0   75000.0  12000   Chicago           720       2026-01-15         1
2        C003   NaN   38000.0  15000    Boston           640       2026-02-03         0
3        C004  45.0  120000.0  10000  New York           760       2026-02-20         1
4        C005  29.0       NaN  25000   Chicago           610       2026-03-01         0
5        C006  41.0   95000.0  18000    Boston           700       2026-03-18         1
6        C007  38.0   68000.0   9000  New York           735       2026-04-02         1
7        C008  27.0   42000.0   3000   Chicago           690       2026-04-14         1
8        C009  52.0  500000.0  70000    Boston           780       2026-05-01         1
9        C010  31.0   58000.0   8000  New York           710       2026-05-17         1

dataset after cleanup/imputation: 
   customer_id   age    income   debt      city  credit_score application_date  approved
0        C001  25.0   45000.0   5000  New York           680       2026-01-10         1
1        C002  32.0   75000.0  12000   Chicago           720       2026-01-15         1
2        C003  32.0   38000.0  15000    Boston           640       2026-02-03         0
3        C004  45.0  120000.0  10000  New York           760       2026-02-20         1
4        C005  29.0   68000.0  25000   Chicago           610       2026-03-01         0
5        C006  41.0   95000.0  18000    Boston           700       2026-03-18         1
6        C007  38.0   68000.0   9000  New York           735       2026-04-02         1
7        C008  27.0   42000.0   3000   Chicago           690       2026-04-14         1
8        C009  52.0  500000.0  70000    Boston           780       2026-05-01         1
9        C010  31.0   58000.0   8000  New York           710       2026-05-17         1

dataset after feature engineering: 
   customer_id   age    income   debt      city  credit_score application_date  approved  debt_to_income
0        C001  25.0   45000.0   5000  New York           680       2026-01-10         1        0.111111
1        C002  32.0   75000.0  12000   Chicago           720       2026-01-15         1        0.160000
2        C003  32.0   38000.0  15000    Boston           640       2026-02-03         0        0.394737
3        C004  45.0  120000.0  10000  New York           760       2026-02-20         1        0.083333
4        C005  29.0   68000.0  25000   Chicago           610       2026-03-01         0        0.367647
5        C006  41.0   95000.0  18000    Boston           700       2026-03-18         1        0.189474
6        C007  38.0   68000.0   9000  New York           735       2026-04-02         1        0.132353
7        C008  27.0   42000.0   3000   Chicago           690       2026-04-14         1        0.071429
8        C009  52.0  500000.0  70000    Boston           780       2026-05-01         1        0.140000
9        C010  31.0   58000.0   8000  New York           710       2026-05-17         1        0.137931

dataset after one hot-encoding: 
   customer_id   age    income   debt  credit_score application_date  approved  debt_to_income  Boston  Chicago  New York
0        C001  25.0   45000.0   5000           680       2026-01-10         1        0.111111   False    False      True
1        C002  32.0   75000.0  12000           720       2026-01-15         1        0.160000   False     True     False
2        C003  32.0   38000.0  15000           640       2026-02-03         0        0.394737    True    False     False
3        C004  45.0  120000.0  10000           760       2026-02-20         1        0.083333   False    False      True
4        C005  29.0   68000.0  25000           610       2026-03-01         0        0.367647   False     True     False
5        C006  41.0   95000.0  18000           700       2026-03-18         1        0.189474    True    False     False
6        C007  38.0   68000.0   9000           735       2026-04-02         1        0.132353   False    False      True
7        C008  27.0   42000.0   3000           690       2026-04-14         1        0.071429   False     True     False
8        C009  52.0  500000.0  70000           780       2026-05-01         1        0.140000    True    False     False
9        C010  31.0   58000.0   8000           710       2026-05-17         1        0.137931   False    False      True

outlier: 
     age    income   debt  credit_score  approved  debt_to_income  Boston  Chicago  New York  application_month
8  52.0  500000.0  70000           780         1            0.14    True    False     False                  5

Which remaining features seem related to approved? pearson correlation

approved             1.000000
credit_score         0.842583
New York             0.478091
income               0.311900
age                  0.241481
application_month    0.112938
Chicago             -0.188982
Boston              -0.357143
debt                -0.692842
debt_to_income      -0.950624
Name: approved, dtype: float64

data after feature selection: 
     age    income   debt  credit_score  approved  debt_to_income  Boston  Chicago  New York
0  25.0   45000.0   5000           680         1        0.111111   False    False      True
1  32.0   75000.0  12000           720         1        0.160000   False     True     False
2  32.0   38000.0  15000           640         0        0.394737    True    False     False
3  45.0  120000.0  10000           760         1        0.083333   False    False      True
4  29.0   68000.0  25000           610         0        0.367647   False     True     False
5  41.0   95000.0  18000           700         1        0.189474    True    False     False
6  38.0   68000.0   9000           735         1        0.132353   False    False      True
7  27.0   42000.0   3000           690         1        0.071429   False     True     False
8  31.0   58000.0   8000           710         1        0.137931   False    False      True

data after Scaling using standarization: 
         age    income      debt  credit_score  approved  debt_to_income  Boston  Chicago  New York
0 -1.252743 -0.850216 -0.977647     -0.299632         1       -0.609495   False    False      True
1 -0.200439  0.275070  0.048882      0.563309         1       -0.195650   False     True     False
2 -0.200439 -1.112783  0.488824     -1.162573         0        1.791401    True    False     False
3  1.753841  1.962998 -0.244412      1.426250         1       -0.844634   False    False      True
4 -0.651427  0.012503  1.955295     -1.809779         0        1.562086   False     True     False
5  1.152524  1.025260  0.928765      0.131838         1        0.053846    True    False     False
6  0.701536  0.012503 -0.391059      0.886912         1       -0.429682   False    False      True
7 -0.952085 -0.962744 -1.270942     -0.083897         1       -0.945408   False     True     False
8 -0.350768 -0.362592 -0.537706      0.347573         1       -0.382464   False    False      True
(.venv) innocent_kushal@Kushals-MacBook-Pro FeatureEngineering % 


'''














