print(boston_houses_ds.DESCR)

X, y = boston_houses_ds.data, boston_houses_ds.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=R_STATE)
knn.fit(X_train, y_train)
r2_score(y_test, knn.predict(X_test))