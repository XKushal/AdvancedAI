'''
NAIVE BAYES

Given the features, which class is most likely?
like P(contains 'free' | spam), like how often does 'free' occurs in spam email?

Bayes theorem:
"Given what I observed,
which class is most probable?"

Naive Bayes:
"Assume the features contribute independently,
then compare the class probabilities."

Gaussian Naive Bayes:
"Do the same thing,
but model numeric features with bell curves."
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

def visualize_classifier(classifier, X, y):
	#define the min and max values for X and y
	#that will be used in the mesh grid
	min_x, max_x = X[:, 0].min() - 1.0, X[:, 0].max() + 1.0 #[:, 0] - all rows, column 0 (a11, a21, a31, ...an1),
	min_y, max_y = X[:, 1].min() - 1.0, X[:, 1].max() + 1.0 #[:, 1] - all rows, column 1 (a12, a22, a32, ...an2)

	#define the step size to use in plotting the mesh grid
	mesh_step_size = 0.01

	#define the mesh grid of X and Y values
	x_vals, y_vals = np.meshgrid(np.arange(min_x, max_x, mesh_step_size), np.arange(min_y, max_y, mesh_step_size))

	#run the classifier on mesh grid, x,y values: [1.0, 1.01, 1.02, ...] into original 2D vector matrix format
	output = classifier.predict(np.c_[x_vals.ravel(), y_vals.ravel()])

	#reshape the output array
	output = output.reshape(x_vals.shape)

	#create a plot
	plt.figure()

	#chose a color scheme for the plot
	plt.pcolormesh(x_vals, y_vals, output, cmap=plt.cm.gray)

	#overlay the training points on the plot
	plt.scatter(X[:, 0], X[:, 1], c=y, s=75, edgecolors='black', linewidth=1, cmap=plt.cm.Paired)

	#specify the boundaries of the plot
	plt.xlim(x_vals.min(), x_vals.max())
	plt.ylim(y_vals.min(), y_vals.max())

	# Specify the ticks on the X and Y axes
	plt.xticks((np.arange(int(X[:, 0].min() - 1), int(X[:, 0].max() +1), 1.0)))
	plt.yticks((np.arange(int(X[:, 1].min() - 1), int(X[:, 1].max() +1), 1.0)))

	plt.show()

def main():
	input_file = 'data_multivar_nb.txt'
	#load data from input file
	data = np.loadtxt(input_file, delimiter=',')
	print(data)
	x, y = data[:,:-1], data[:,-1]

	#create naive bayes classifer
	classifier = GaussianNB()
	classifier.fit(x,y) #train the classifier 
	y_pred = classifier.predict(x) #predict the values for training data

	#compute accuracy
	accuracy =  100.0 * (y == y_pred).sum() / x.shape[0]
	print("Accuracy of Naïve Bayes classifier =", round(accuracy, 2), "%")

	#visualize the performance of the classifier 
	visualize_classifier(classifier, x, y)

	#spilit the data into training and test data
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 3)
	classifier_new = GaussianNB()
	classifier_new.fit(x_train, y_train)
	y_test_pred = classifier_new.predict(x_test)

	#compute the accurace of the classifier
	accuracy = 100.0 * (y_test == y_test_pred).sum() / x_test.shape[0]
	print("Accuracy of the new classifier =", round(accuracy, 2), "%")

	# Visualize the performance of the classifier
	visualize_classifier(classifier_new, x_test, y_test)

	# cross validation
	num_folds = 3
	accuracy_values = cross_val_score(classifier,x, y, scoring='accuracy', cv=num_folds)
	print("Accuracy: " + str(round(100*accuracy_values.mean(), 2)) + "%")

	precision_values = cross_val_score(classifier,x, y, scoring='precision_weighted', cv=num_folds)
	print("Precision: " + str(round(100*precision_values.mean(), 2)) +"%")

	recall_values = cross_val_score(classifier,x, y, scoring='recall_weighted', cv=num_folds)
	print("Recall: " + str(round(100*recall_values.mean(), 2)) + "%")

	f1_values = cross_val_score(classifier,x, y, scoring='f1_weighted', cv=num_folds)
	print("F1: " + str(round(100*f1_values.mean(), 2)) + "%")


if __name__ == '__main__':
	main()
