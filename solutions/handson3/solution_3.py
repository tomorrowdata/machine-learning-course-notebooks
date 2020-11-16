X, y = boston_houses_ds.data, boston_houses_ds.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=R_STATE)

dt = DecisionTreeRegressor(random_state=R_STATE)
dt.fit(X_train, y_train)
r2_score(y_test, dt.predict(X_test))

dt = DecisionTreeRegressor(random_state=R_STATE, max_depth=10, criterion="mae")
dt.fit(X_train, y_train)
r2_score(y_test, dt.predict(X_test))