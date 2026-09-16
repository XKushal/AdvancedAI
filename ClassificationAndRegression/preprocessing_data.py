import numpy as np
from sklearn import preprocessing

input_data = np.array([
	[5.1, -2.9, 3.3],
	[-1.2, 7.8, -6.1],
	[3.9, 0.4, 2.1],
	[7.3, -9.9, -4.5]
	])

#1. binarization - Numeircal value to Boolean
data_binarized = preprocessing.Binarizer(threshold=2.1).transform(input_data)
print("\nBinarized data:\n", data_binarized)

#2. Mean removal
mean_value = input_data.mean(axis=0) #calculate vertically one column at a time
std_value = input_data.std(axis=0)

data_scaled = preprocessing.scale(input_data)
mean_value = data_scaled.mean(axis=0)
std_value = data_scaled.std(axis=0)

print("Mean =", mean_value)
print("Std deviation =", std_value)

#3. Scaling: Changing range of values for a variable
#MinMaxScaler Algorithm (x-Min(x))/(Max(x) - Min(x)
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,1)) #scale value between 0 and 1
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data) #learn + change

print("\nMin max scaled data:\n", data_scaled_minmax)

#4. Normalization: Changing distribution of the data
data_normalized_l1 = preprocessing.normalize(input_data, norm='l1') #sum of absolute value = 1
data_normalized_l2 = preprocessing.normalize(input_data, norm='l2') #sum of squares = 1

print("\nL1 normalized data:\n", data_normalized_l1)
print("\nL2 normalized data:\n", data_normalized_l2)
