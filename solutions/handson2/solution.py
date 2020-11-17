# 2: check model performance with original data
check_knn_performances(X_train, X_test, y_train, y_test)

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

# 5: check performances
check_knn_performances(X_train_pca, X_test_pca, y_train, y_test)
check_knn_performances(X_train_scaled_pca, X_test_scaled_pca, y_train, y_test)

# 6 & 7: plot
plot_scaling_pcs(X_train_pca, X_train_scaled_pca,  y_train)