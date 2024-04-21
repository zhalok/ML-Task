import numpy as np
import pandas as pd
from preprocessing import preprocessing
from encoder import encode
from spliter import split
from scaler import scale
from pca import principal_component_analysis
from evaluator import evaluate
from random_forest import RandomForestRegressor



df = pd.read_csv("Online Retail Data Set.csv",encoding='unicode_escape')
preprocessed_df = preprocessing(df=df)
X,y = encode(preprocessed_df)
X = scale(X)
X = principal_component_analysis(n_components=20,X=X)
X_train, X_test, y_train, y_test = split(X,y)
regressor = RandomForestRegressor(max_depth=4,n_estimators=12)
regressor.fit(X_train,y_train.values)
result = evaluate(X_test=X_test,y_test=y_test,model=regressor)
print(result)