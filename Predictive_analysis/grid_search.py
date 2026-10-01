
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import classification_report


# 1. Load the dataset
data = np.loadtxt("../data/data_random_forests.txt", delimiter=",")

X = data[:, :-1]
y = data[:, -1].astype(int)


# 2. Split training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=5,
    stratify=y
)


# 3. Define hyperparameter combinations (book)
parameter_grid = [
    {
        "n_estimators": [100],
        "max_depth": [2, 4, 7, 12, 16]
    },
    {
        "max_depth": [4],
        "n_estimators": [25, 50, 100, 250]
    }
]


# 4. Metrics to optimize independently
metrics = ["precision_weighted", "recall_weighted"]

for metric in metrics:

    print(f"\nSearching best parameters for: {metric}")

    # 5. Create Grid Search
    grid = GridSearchCV(
        estimator=ExtraTreesClassifier(random_state=0),
        param_grid=parameter_grid,
        cv=5,
        scoring=metric,
        n_jobs=-1
    )

    # 6. Search using training data only
    grid.fit(X_train, y_train)

    # 7. Print all tested configurations
    results = grid.cv_results_

    for params, score in zip(
        results["params"],
        results["mean_test_score"]
    ):
        print(params, "-->", round(score, 3))

    # 8. Best hyperparameters
    print("\nBest parameters:", grid.best_params_)
    print("Best validation score:", grid.best_score_)

    # 9. Evaluate best model on unseen test data
    y_pred = grid.predict(X_test)

    print("\nTesting performance:")
    print(classification_report(y_test, y_pred))
