import numpy as np
import pandas as pd
from preprocessing import preprocessing
from util import plot_grouped_data

df = pd.read_csv("Online Retail Data Set.csv",encoding='unicode_escape')
preprocessed_df = preprocessing(df=df)

for col in ["Country","Season","Day","Month"]:
    plot_grouped_data(col,preprocessed_df)