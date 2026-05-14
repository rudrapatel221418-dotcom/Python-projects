from sklearn.cluster import DBSCAN

X = [
    [1, 1],
    [1, 2],
    [2, 1],
    [2, 2],
    [8, 8],
    [8, 9],
    [9, 8],
    [5, 5],
    [10, 1],
    [0, 6],
]

dbscan = DBSCAN(eps=1.5, min_samples=2)
labels = dbscan.fit_predict(X)

print("DBSCAN Labels:", labels)
print("Note: -1 means noise (outlier)")