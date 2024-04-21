import pandas as pd
from util import get_season

def preprocessing(df):
    ...
    df = df[df["Quantity"]>=0]
    df = df[df["UnitPrice"]>=0]
    df = df.drop(["CustomerID","StockCode","InvoiceNo","Description"],axis=1)
    df = df.drop_duplicates()
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%d-%m-%Y %H:%M')
    df['Quantity'] = pd.to_numeric(df['Quantity'])
    df['UnitPrice'] = pd.to_numeric(df['UnitPrice'])
    df['Month'] = df['InvoiceDate'].dt.month_name()
    df['Day'] = df['InvoiceDate'].dt.day_name()
    df['Hour'] = df['InvoiceDate'].dt.hour
    df['Total_sales'] = df['Quantity'] * df['UnitPrice']
    df['Month'] = df['InvoiceDate'].dt.month
    df['Season'] = df['Month'].apply(get_season)
    df = df.drop(["InvoiceDate"],axis=1)

    return df