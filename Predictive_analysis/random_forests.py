
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier


# -----------------------------------------
# 1. Load Dataset
# -----------------------------------------

input_file = "../data/data_random_forests.txt"
data = np.loadtxt(input_file, delimiter=",")

# Features and target
X = data[:, :-1]
y = data[:, -1].astype(int)


# -----------------------------------------
# 2. Visualize Original Dataset
# -----------------------------------------

plt.figure()

for label, marker in zip([0, 1, 2], ["s", "o", "^"]):
    class_data = X[y == label]

    plt.scatter(
        class_data[:, 0],
        class_data[:, 1],
        marker=marker,
        label=f"Class {label}"
    )

plt.title("Original Dataset")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()


# -----------------------------------------
# 3. Split Training and Testing Data
# -----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=5
)


# -----------------------------------------
# 4. Create Ensemble Models
# -----------------------------------------

params = {
    "n_estimators": 100,
    "max_depth": 4,
    "random_state": 0
}

# Random Forest
rf = RandomForestClassifier(**params)

# Extremely Randomized Trees
erf = ExtraTreesClassifier(**params)


# -----------------------------------------
# 5. Train Both Models
# -----------------------------------------

rf.fit(X_train, y_train)
erf.fit(X_train, y_train)


# -----------------------------------------
# 6. Make Predictions
# -----------------------------------------

rf_train_pred = rf.predict(X_train)
rf_test_pred = rf.predict(X_test)

erf_train_pred = erf.predict(X_train)
erf_test_pred = erf.predict(X_test)


# -----------------------------------------
# 7. Evaluate Model Performance
# -----------------------------------------

class_names = ["Class-0", "Class-1", "Class-2"]

def evaluate_model(name, y_train_pred, y_test_pred):

    print("\n" + "#" * 40)
    print(f"{name} - Training Performance\n")

    print(
        classification_report(
            y_train,
            y_train_pred,
            target_names=class_names
        )
    )

    print(f"\n{name} - Testing Performance\n")

    print(
        classification_report(
            y_test,
            y_test_pred,
            target_names=class_names
        )
    )


evaluate_model(
    "Random Forest",
    rf_train_pred,
    rf_test_pred
)

evaluate_model(
    "Extra Trees",
    erf_train_pred,
    erf_test_pred
)


# -----------------------------------------
# 8. Visualize Decision Boundaries
# -----------------------------------------

def visualize_classifier(model, X, y, title):

    # Define plotting boundaries
    x_min = X[:, 0].min() - 1
    x_max = X[:, 0].max() + 1

    y_min = X[:, 1].min() - 1
    y_max = X[:, 1].max() + 1

    # Generate mesh grid
    xx, yy = np.meshgrid(
        np.arange(x_min, x_max, 0.03),
        np.arange(y_min, y_max, 0.03)
    )

    # Predict classes for grid points
    grid_points = np.c_[xx.ravel(), yy.ravel()]

    predictions = model.predict(grid_points)
    predictions = predictions.reshape(xx.shape)

    plt.figure()

    # Draw decision regions
    plt.contourf(
        xx,
        yy,
        predictions,
        alpha=0.3,
        cmap="viridis"
    )

    # Plot actual data points
    plt.scatter(
        X[:, 0],
        X[:, 1],
        c=y,
        cmap="viridis",
        edgecolors="black"
    )

    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")


# Random Forest boundaries
visualize_classifier(
    rf,
    X_test,
    y_test,
    "Random Forest - Test Dataset"
)

# Extra Trees boundaries
visualize_classifier(
    erf,
    X_test,
    y_test,
    "Extra Trees - Test Dataset"
)

plt.show()
