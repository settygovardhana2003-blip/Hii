#Dimensionality Reduction using PCA (Iris dataset: 4 features -> 2 features)
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X = StandardScaler().fit_transform(iris.data)     #Scale all features to the same range

pca = PCA(n_components = 2)
X_pca = pca.fit_transform(X)

print("Shape before:", X.shape)
print("Shape after: ", X_pca.shape)
print("Variance explained by each component:", pca.explained_variance_ratio_.round(3))
print(f"Total variance kept: {pca.explained_variance_ratio_.sum() * 100:.1f}%")

plt.scatter(X_pca[:, 0], X_pca[:, 1], c = iris.target)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Iris Dataset reduced from 4D to 2D')
plt.show()