from sklearn.preprocessing import StandardScaler

def scale(X):
    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)

    return X
