import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. Create dataset
data = {
    'Income_Level': [15, 20, 25, 80, 85, 90, 45, 50, 55, 120],
    'Purchase_Frequency': [1, 2, 2, 8, 9, 9, 5, 5, 6, 2]
}
df = pd.DataFrame(data)

# 2. Apply K-Means clustering (3 clusters)
kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
df['Cluster'] = kmeans.fit_predict(df[['Income_Level', 'Purchase_Frequency']])

# 4. Get centroid points
centroids = kmeans.cluster_centers_

# 3. Plot the clustered data
plt.figure(figsize=(8, 6))
plt.scatter(df['Income_Level'], df['Purchase_Frequency'], c=df['Cluster'], cmap='viridis', label='Customers')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')

plt.xlabel('Income Level')
plt.ylabel('Purchase Frequency')
plt.title('Customer Grouping (K-Means)')
plt.legend()
plt.show()

# Display the data with cluster assignments
print(df)
print("\nCentroid Coordinates:")
print(centroids)