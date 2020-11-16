X, y = breast_ds.data, breast_ds.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=R_STATE)

ridge = Ridge()
lasso = Lasso(alpha=0.01)
lr = LinearRegression()

ridge.fit(X_train, y_train)
lasso.fit(X_train, y_train)
lr.fit(X_train, y_train)

print(r2_score(y_test, ridge.predict(X_test)))
print(r2_score(y_test, lasso.predict(X_test)))
print(r2_score(y_test, lr.predict(X_test)))

plot_coefficients_given_models(breast_ds, [lr, ridge, lasso])