from util import check_values
from util import plot_grouped_data

def eda(df):
    ...
    df.describe()
    check_values(df=df)

    for col in ["Country","Season","Day","Month"]:
        plot_grouped_data(col,df=df)