'''
LOGISTIC REGRESSION

Supervised classification algorithm.

example: Will a student pass? y-1, n-0
independent variable, x=hours studied
Is there some mathematical relationship between hours studied and the probability of passing?


Input:X = independent features, y = known class labels
Learns: z = b₀ + b₁x₁ + b₂x₂ + ...
Then: z → sigmoid → probability
Finally: probability → predicted class
'''

import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

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
	X = np.array([
	[3.1, 7.2],
	[4, 6.7],
	[2.9, 8],
	[5.1, 4.5],
	[6, 5],
	[5.6, 5],
	[3.3, 0.4],
	[3.9, 0.9],
	[2.8, 1],
	[0.5, 3.4],
	[1, 4],
	[0.6,4.9]])

	y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]) #4 classes

	#create the logistic regression classifier 
	classifier = linear_model.LogisticRegression(solver='lbfgs', C=1) #liblinear = binary, lbfgs=multiclass

	#train the classifier
	classifier.fit(X,y)

	#visualize the performance of the classifier 
	visualize_classifier(classifier, X, y)

if __name__ == '__main__':
	main()




