import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs

# Generate synthetic time series data
n_samples = 300
n_features = 100
centers = 3
random_state = 42
data, y = make_blobs(n_samples=n_samples, n_features=n_features, centers=centers, random_state=random_state)

# Standardize the data
scaler = StandardScaler()
data = scaler.fit_transform(data)

# Perform hierarchical clustering
Z = linkage(data, method='ward')
clusters = fcluster(Z, centers, criterion='maxclust')

# Plot the dendrogram
plt.figure()
dendrogram(Z)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Euclidean Distance')
plt.show()

# Choose a representative time series from each cluster
representative_idxs = []
for i in range(1, centers + 1):
    cluster_points = data[clusters == i]
    centroid = np.mean(cluster_points, axis=0)
    representative_idx = np.argmin(np.linalg.norm(cluster_points - centroid, axis=1))
    representative_idxs.append(representative_idx)

representatives = data[representative_idxs]

# Perform K-means clustering on the representatives
kmeans = KMeans(n_clusters=centers, random_state=random_state)
kmeans.fit(representatives)

# Perform importance sampling
weights = np.zeros(n_samples)
for i in range(centers):
    cluster_points = data[clusters == i + 1]
    distances = np.linalg.norm(cluster_points - kmeans.cluster_centers_[i], axis=1)
    weights[clusters == i + 1] = 1 / (distances + 1e-10)

normalized_weights = weights / np.sum(weights)
coreset_indices = np.random.choice(n_samples, size=n_samples // 10, replace=False, p=normalized_weights)
coreset = data[coreset_indices]

# Plot the time series data
plt.figure()
for i in range(coreset.shape[1]):
    plt.plot(coreset[:, i], alpha=0.1)
plt.title('Coreset of Time Series Data')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()
