print(iris_ds.DESCR)
X, y = iris_ds.data, iris_ds.target
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=R_STATE)
knn = KNeighborsClassifier(n_neighbors=3, weights="distance")

knn.fit(X_train, y_train)
accuracy_score(y_test, knn.predict(X_test))