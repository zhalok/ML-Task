import pandas as pd

def encode(df):
    X = df.drop(["Total_sales"],axis=1)
    y = df["Total_sales"] 
    categorical_features = [col for col in X.columns if X[col].dtype=="object"]
    X = pd.get_dummies(X, columns=categorical_features,dtype=int)

    return X,y