import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift, estimate_bandwidth
from itertools import cycle

# Load data from input file
X = np.loadtxt('../data/data_clustering.txt', delimiter=',')

# ----------------------------------------
# 1. Estimate bandwidth
# bandwidth_X: Estimated window size
# ----------------------------------------

bandwidth_X = estimate_bandwidth(
    X,
    quantile=0.1, #controls which range of those distances influences the estimate.
    n_samples=len(X)
)

# ----------------------------------------
# 2. Create and train Mean Shift
# ----------------------------------------

meanshift_model = MeanShift(
    bandwidth=bandwidth_X,
    bin_seeding=True
)

meanshift_model.fit(X)

# ----------------------------------------
# 3. Extract cluster centers and lables
# ----------------------------------------

cluster_centers = meanshift_model.cluster_centers_ #Final coordinates of discovered cluster centers

# ----------------------------------------
# 4. Estimate the number of clusters
# ----------------------------------------

labels = meanshift_model.labels_ #Cluster assignment of every data point

num_clusters = len(np.unique(labels))

print("\nNumber of clusters in input data =", num_clusters)

print("Cluster labels:", meanshift_model.labels_)
print("Cluster centers:\n", meanshift_model.cluster_centers_)

# Print each data point with its assigned cluster
for point, label in zip(X, meanshift_model.labels_):
    print(f"Point: {point} -> Cluster: {label}")

# ----------------------------------------
# 5. Visualize clusters and centers
# ----------------------------------------

plt.figure()

markers = 'o*xvs'

for i, marker in zip(range(num_clusters), cycle(markers)):

    # Plot points belonging to the current cluster
    plt.scatter(
        X[labels == i, 0],
        X[labels == i, 1],
        marker=marker,
        color='black'
    )

    # Plot the center of the current cluster
    cluster_center = cluster_centers[i]

    plt.plot(
        cluster_center[0],
        cluster_center[1],
        marker='o',
        markerfacecolor='black',
        markeredgecolor='black',
        markersize=15
    )

plt.title('Clusters')
plt.show()
