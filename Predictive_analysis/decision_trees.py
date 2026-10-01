#decision tree
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree


# ------------------------------------------------
# 1. Load dataset
# ------------------------------------------------

input_file = "../data/data_decision_trees.txt"
data = np.loadtxt(input_file, delimiter=",")

# First two columns = features
# Last column = target label
X = data[:, :-1]
y = data[:, -1]


# ------------------------------------------------
# 2. Separate classes for visualization
# ------------------------------------------------

class_0 = X[y == 0]
class_1 = X[y == 1]

plt.figure()

plt.scatter(
    class_0[:, 0],
    class_0[:, 1],
    marker="x",
    label="Class 0"
)

plt.scatter(
    class_1[:, 0],
    class_1[:, 1],
    marker="o",
    label="Class 1"
)

plt.title("Original Dataset")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()


# ------------------------------------------------
# 3. Split training and testing datasets
# ------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=5
)


# ------------------------------------------------
# 4. Create and train Decision Tree
# ------------------------------------------------

classifier = DecisionTreeClassifier(
    criterion="gini",
    max_depth=4,
    random_state=0
)

classifier.fit(X_train, y_train)


# ------------------------------------------------
# 5. Predict on test dataset
# ------------------------------------------------

y_train_pred = classifier.predict(X_train)
y_test_pred = classifier.predict(X_test)


# ------------------------------------------------
# 6. Evaluate model performance
# ------------------------------------------------

class_names = ["Class-0", "Class-1"]

print("\n" + "#" * 40)
print("Classifier performance on training dataset\n")

print(
    classification_report(
        y_train,
        y_train_pred,
        target_names=class_names
    )
)

print("#" * 40)

print("\nClassifier performance on testing dataset\n")

print(
    classification_report(
        y_test,
        y_test_pred,
        target_names=class_names
    )
)


# ------------------------------------------------
# 7. Visualize decision boundaries
# ------------------------------------------------

def visualize_classifier(model, X, y, title):

    # Define the boundaries of our plot
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

    # Generate grid points
    xx, yy = np.meshgrid(
        np.arange(x_min, x_max, 0.01),
        np.arange(y_min, y_max, 0.01)
    )

    # Predict the class of each point in the grid
    grid_points = np.c_[xx.ravel(), yy.ravel()]
    predictions = model.predict(grid_points)

    # Restore original grid shape
    predictions = predictions.reshape(xx.shape)

    # Plot decision regions
    plt.figure()

    plt.contourf(
        xx,
        yy,
        predictions,
        alpha=0.3,
        cmap="coolwarm"
    )

    # Plot actual dataset points
    plt.scatter(
        X[:, 0],
        X[:, 1],
        c=y,
        cmap="coolwarm",
        edgecolors="black"
    )

    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")


# Visualize training data
visualize_classifier(
    classifier,
    X_train,
    y_train,
    "Decision Tree - Training Dataset"
)

# Visualize testing data
visualize_classifier(
    classifier,
    X_test,
    y_test,
    "Decision Tree - Testing Dataset"
)


# ------------------------------------------------
# 8. Visualize the actual Decision Tree
# ------------------------------------------------

plt.figure(figsize=(14, 8))

plot_tree(
    classifier,
    filled=True,
    rounded=True,
    feature_names=["Feature 1", "Feature 2"],
    class_names=class_names
)

plt.title("Decision Tree Structure")

plt.show()