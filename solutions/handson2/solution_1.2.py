# here a dataframe with the features X (input) and output y (target)
X_df, y_se = create_dataframe_series(iris_ds)

def train_test_score(X, y, n_neighbors=3):
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=R_STATE)
    knn = KNeighborsClassifier(n_neighbors=n_neighbors, weights="distance")
    knn.fit(X_train, y_train)
    return accuracy_score(y_test, knn.predict(X_test))

print(train_test_score(X_df[["petal_width_(cm)"]], y_se))
print(train_test_score(X_df[["sepal_width_(cm)"]], y_se))
print(train_test_score(X_df[["petal_length_(cm)"]], y_se))
print(train_test_score(X_df[["petal_length_(cm)", "petal_width_(cm)"]], y_se))
print(train_test_score(X_df[["sepal_length_(cm)", "sepal_width_(cm)"]], y_se))

X_df["length"] = X_df["petal_length_(cm)"] /  X_df["sepal_length_(cm)"]
X_df["width"] = X_df["petal_width_(cm)"] /  X_df["sepal_width_(cm)"]
train_test_score(X_df[["length", "width"]], y_se)