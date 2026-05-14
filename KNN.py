from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Create a small dataset
X = [
    [1, 2],
    [2, 3],
    [3, 3],
    [6, 5],
    [7, 7],
    [8, 6]
]

y = [0, 0, 0, 1, 1, 1]  # Labels (classes)

# Step 2: Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Step 3: Create KNN model (K = 3)
knn = KNeighborsClassifier(n_neighbors=3)

# Step 4: Train the model
knn.fit(X_train, y_train)

# Step 5: Make predictions
y_pred = knn.predict(X_test)

# Step 6: Check accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))