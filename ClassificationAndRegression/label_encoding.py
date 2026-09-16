import numpy as np
from sklearn import preprocessing

input_labels = ['red', 'black', 'red', 'green', 'black', 'yellow','white']

#create a label encoder object and train it
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels) #learn
encoded_values = encoder.transform(input_labels) #transform
print("\nencoded_values:", encoded_values.tolist())

#print the mapping
print("\nLabel mapping:")
for i, item in enumerate(encoder.classes_):
	print(item, '--->', i)

encoded_test_values = [4, 0, 2, 1]
decoded_lables = encoder.inverse_transform(encoded_test_values)
print("\nencoded_test_values =", encoded_test_values)
print("decoded_lables =", decoded_lables)