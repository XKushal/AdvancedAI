
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import patches
from sklearn import datasets
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import train_test_split
from sklearn.metrics import adjusted_rand_score

# ----------------------------------------
# 1. Load the Iris dataset
# ----------------------------------------

iris = datasets.load_iris()

X = iris.data
y = iris.target

# ----------------------------------------
# 2. Split the dataset (60/40)
# ----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.4,
    random_state=0,
    stratify=y
)

# Three known species in the Iris dataset
num_classes = len(np.unique(y_train))

# ----------------------------------------
# 3. Create the GMM
# ----------------------------------------

classifier = GaussianMixture(
    n_components=num_classes,
    covariance_type='full',
    init_params='kmeans',
    max_iter=20,
    random_state=0
)

# ----------------------------------------
# 4. Train the GMM (unlabeled features)
# ----------------------------------------

classifier.fit(X_train)

# ----------------------------------------
# 5. Extract centers and labels
# ----------------------------------------

cluster_centers = classifier.means_

y_train_pred = classifier.predict(X_train)
y_test_pred = classifier.predict(X_test)

print("\nGaussian means:\n", cluster_centers)

print("\nTraining cluster labels:\n", y_train_pred)

print("\nTesting cluster labels:\n", y_test_pred)

# ----------------------------------------
# 6. Predict membership probabilities
# ----------------------------------------

probabilities = classifier.predict_proba(X_test)

print("\nProbabilities for first 5 test points:\n")
print(probabilities[:5])

# ----------------------------------------
# 7. Evaluate grouping against Iris labels
# ----------------------------------------

ari_training = adjusted_rand_score(
    y_train, y_train_pred
)

ari_testing = adjusted_rand_score(
    y_test, y_test_pred
)

print("\nTraining ARI =", ari_training)
print("Testing ARI =", ari_testing)

# ----------------------------------------
# 8. Draw Gaussian distribution ellipses
# ----------------------------------------

plt.figure()

colors = ['blue', 'green', 'red']
axis_handle = plt.gca()

for i, color in enumerate(colors):

    # Use the first two feature dimensions
    covariance = classifier.covariances_[i][:2, :2]

    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(
        covariance
    )

    # Largest eigenvalue gives the major axis
    major_vector = eigenvectors[:, 1]

    # Calculate rotation angle
    angle = np.degrees(
        np.arctan2(
            major_vector[1],
            major_vector[0]
        )
    )

    # Ellipse dimensions: two standard deviations
    width = 4 * np.sqrt(eigenvalues[1])
    height = 4 * np.sqrt(eigenvalues[0])

    # Draw ellipse centered at Gaussian mean
    ellipse = patches.Ellipse(
        xy=classifier.means_[i, :2],
        width=width,
        height=height,
        angle=angle,
        color=color,
        alpha=0.25
    )

    axis_handle.add_patch(ellipse)

# ----------------------------------------
# 9. Plot original training data
# ----------------------------------------

for i, color in enumerate(colors):

    current_data = X_train[y_train_pred == i]

    plt.scatter(
        current_data[:, 0],
        current_data[:, 1],
        marker='o',
        facecolors='none',
        edgecolors=color,
        s=40,
        label=f'Component {i}'
    )

# ----------------------------------------
# 10. Overlay test data
# ----------------------------------------

plt.scatter(
    X_test[:, 0],
    X_test[:, 1],
    marker='s',
    facecolors='none',
    edgecolors='black',
    s=40,
    label='Test data'
)

plt.title('Gaussian Mixture Model')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.legend()
plt.show()
