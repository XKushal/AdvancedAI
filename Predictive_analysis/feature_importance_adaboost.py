
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_diabetes
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_squared_error,
    explained_variance_score
)


# -----------------------------------------
# 1. Load Dataset
# -----------------------------------------

housing_data = load_diabetes()

X = housing_data.data
y = housing_data.target

feature_names = np.array(housing_data.feature_names)


# -----------------------------------------
# 2. Split Training and Testing Data
# -----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=7
)


# -----------------------------------------
# 3. Create AdaBoost Regressor
# -----------------------------------------

regressor = AdaBoostRegressor(
    estimator=DecisionTreeRegressor(max_depth=4),
    n_estimators=400,
    random_state=7
)


# -----------------------------------------
# 4. Train Model
# -----------------------------------------

regressor.fit(X_train, y_train)


# -----------------------------------------
# 5. Make Predictions and Evaluate
# -----------------------------------------

y_pred = regressor.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
evs = explained_variance_score(y_test, y_pred)

print("\nADABOOST REGRESSOR")
print("Mean squared error:", round(mse, 2))
print("Explained variance score:", round(evs, 2))


# -----------------------------------------
# 6. Compute Feature Importance
# -----------------------------------------

feature_importances = regressor.feature_importances_

# Normalize relative to highest importance
feature_importances = 100.0 * (
    feature_importances / max(feature_importances)
)


# -----------------------------------------
# 7. Sort Features by Importance
# -----------------------------------------

index_sorted = np.argsort(feature_importances)[::-1]

for index in index_sorted:
    print(
        feature_names[index],
        "->",
        round(feature_importances[index], 2)
    )


# -----------------------------------------
# 8. Visualize Feature Importance
# -----------------------------------------

plt.figure(figsize=(10, 6))

plt.barh(
    feature_names[index_sorted],
    feature_importances[index_sorted]
)

plt.gca().invert_yaxis()

plt.xlabel("Relative Feature Importance")
plt.ylabel("Features")
plt.title("Feature Importance using AdaBoost Regressor")

plt.tight_layout()
plt.show()
