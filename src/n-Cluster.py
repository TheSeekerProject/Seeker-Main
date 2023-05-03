import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generate sample time series data
x = np.linspace(0, 20*np.pi, 200)
data = np.sin(x)

# Define the number of samples in the coreset
num_samples = 50

# Define the number of clusters for K-means
num_clusters = 10

# Use K-means to cluster the data
km = KMeans(n_clusters=num_clusters)
km.fit(data.reshape(-1, 1))

# Generate the coreset using the cluster centroids
cluster_indices = np.argpartition(km.transform(data.reshape(-1, 1)), num_samples, axis=0)[:num_samples]
coreset = data[cluster_indices.flatten()]

# Plot the original time series data and the coreset
plt.plot(x, data, label='Original Data')
plt.plot(x[cluster_indices.ravel()], coreset, 'o', color='red', label='Coreset')
plt.legend()
plt.show()
