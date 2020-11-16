# 1: split test and training
X, y = wine_ds.data, wine_ds.target
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=R_STATE)

# 2: fit the reference model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
accuracy_score(y_test, knn.predict(X_test))

# 3: fit the scaler with the training data
scaler = StandardScaler()
scaler.fit(X_train)
X_train_sc, X_test_sc = scaler.transform(X_train), scaler.transform(X_test)

# 4: apply pca to both normalized and no-normalized
pca_vanilla = PCA(n_components=5)
pca_vanilla.fit(X_train)
pca_scaled = PCA(n_components=5)
pca_scaled.fit(X_train_sc)

X_train_pca, X_test_pca = pca_vanilla.transform(X_train), pca_vanilla.transform(X_test)
X_train_scaled_pca, X_test_scaled_pca = pca_scaled.transform(X_train_sc), pca_scaled.transform(X_test_sc)

# 5: plot
plot_scaling_pcs(X_train_pca, X_train_scaled_pca,  y_train)

# 6: train and test
knn_pca = KNeighborsClassifier(n_neighbors=3)
knn_pca.fit(X_train_pca, y_train)
accuracy_score(y_test, knn_pca.predict(X_test_pca))

# 6: train and test
knn_sc = KNeighborsClassifier(n_neighbors=3)
knn_sc.fit(X_train_scaled_pca, y_train)
accuracy_score(y_test, knn_sc.predict(X_test_scaled_pca))