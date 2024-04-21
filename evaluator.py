from sklearn.metrics import mean_squared_error, r2_score


def evaluate(X_test, y_test, model):

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)

    return mse