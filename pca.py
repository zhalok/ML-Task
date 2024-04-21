import numpy as np
from sklearn.decomposition import PCA

def principal_component_analysis(n_components,X):
    pca_ = PCA(n_components=n_components)  
    pca_.fit(X=X)
    principal_components = pca_.transform(X=X)
    return principal_components