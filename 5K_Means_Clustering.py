#K-Means Clustering
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#9 points in 3 obvious groups: near (1,2), near (8,8) and near (1,8)
points = np.array([[1, 2], [2, 1], [1.5, 1.8], [8, 8], [9, 9], [8.5, 8.2], [1, 8], [2, 9], [1.5, 8.5]])

kmeans = KMeans(n_clusters = 3, n_init = 10, random_state = 0).fit(points)

print("Labels:   ", kmeans.labels_)
print("Centroids:\n", kmeans.cluster_centers_.round(2))
print("New point [2, 2] belongs to cluster:", kmeans.predict([[2, 2]])[0])

plt.scatter(points[:, 0], points[:, 1], c = kmeans.labels_, s = 80)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'red', marker = 'X', s = 200, label = 'Centroids')
plt.title('K-Means Clustering (K = 3)')
plt.legend()
plt.show()