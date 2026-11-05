#Hierarchical Clustering (Agglomerative) with a Dendrogram
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

#9 points in 3 obvious groups: near (1,2), near (8,8) and near (1,8)
points = np.array([[1, 2], [2, 1], [1.5, 1.8], [8, 8], [9, 9], [8.5, 8.2], [1, 8], [2, 9], [1.5, 8.5]])

#Keep merging the two closest clusters (Ward linkage), then cut the tree into 3 clusters
Z = linkage(points, method = 'ward')
labels = fcluster(Z, t = 3, criterion = 'maxclust')

for cluster in sorted(set(labels)):
    print(f"Cluster {cluster}: points {(np.where(labels == cluster)[0] + 1).tolist()}")

plt.figure(figsize = (11, 4))
plt.subplot(1, 2, 1)
dendrogram(Z, labels = [f"P{i + 1}" for i in range(len(points))])
plt.title('Dendrogram')
plt.ylabel('Distance')
plt.subplot(1, 2, 2)
plt.scatter(points[:, 0], points[:, 1], c = labels, s = 80)
plt.title('Clusters')
plt.show()