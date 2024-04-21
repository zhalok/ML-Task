import numpy as np

class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth

    def fit(self, X, y):
        self.n_features = X.shape[1]
        self.tree = self._grow_tree(X, y)

    def _grow_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        n_labels = len(np.unique(y))

 
        if (self.max_depth is not None and depth >= self.max_depth) or n_labels == 1:
            
            return {'value': np.mean(y)}
                

        best_feature, best_threshold = self._find_best_split(X, y)

        left_idxs = X[:, best_feature] < best_threshold
        X_left, y_left = X[left_idxs], y[left_idxs]
        X_right, y_right = X[~left_idxs], y[~left_idxs]

        return {'feature_idx': best_feature,
                'threshold': best_threshold,
                'left': self._grow_tree(X_left, y_left, depth + 1),
                'right': self._grow_tree(X_right, y_right, depth + 1)}

    def _find_best_split(self, X, y):
        best_feature, best_threshold, best_variance = None, None, float('inf')
        for feature_idx in range(self.n_features):
            min_value = np.min(X[:, feature_idx])
            max_value = np.max(X[:, feature_idx])
            thresholds = np.random.uniform(low=min_value, high=max_value, size=100)

            for threshold in thresholds:
                left_idxs = X[:, feature_idx] < threshold
                var_left = np.var(y[left_idxs])
                var_right = np.var(y[~left_idxs])
                variance = var_left + var_right
                if variance < best_variance:
                    best_feature, best_threshold, best_variance = feature_idx, threshold, variance
        return best_feature, best_threshold

    def predict(self, X):
        return np.array([self._predict_tree(x, self.tree) for x in X])

    def _predict_tree(self, x, tree):
        if 'value' in tree:
            return tree['value']
        feature_val = x[tree['feature_idx']]
        branch = tree['left'] if feature_val < tree['threshold'] else tree['right']
        return self._predict_tree(x, branch)
