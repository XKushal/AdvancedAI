import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("train.csv")
X = data.iloc[:,0:20]
y = data.iloc[:,-1] #pick last column for the target feature 

model = ExtraTreesClassifier()
model.fit(X,y)
print(model.feature_importances_) #inbuilt class

feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(5).plot(kind='barh')
plt.show()