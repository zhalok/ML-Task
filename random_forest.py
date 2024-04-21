import numpy as np
from decision_tree import DecisionTree



class RandomForestRegressor:
    def __init__(self, n_estimators=10, max_depth=None, bootstrap=True):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.bootstrap = bootstrap

    def fit(self, X, y):
        self.trees = []
        for _ in range(self.n_estimators):
            tree = DecisionTree(max_depth=self.max_depth)
            if self.bootstrap:
                idxs = np.random.choice(len(X), size=len(X), replace=True)
                X_bootstrapped, y_bootstrapped = X[idxs], y[idxs]
            else:
                X_bootstrapped, y_bootstrapped = X, y
            tree.fit(X_bootstrapped, y_bootstrapped)
            self.trees.append(tree)

    def predict(self, X):
        predictions = np.array([tree.predict(X) for tree in self.trees])
        return np.mean(predictions, axis=0)