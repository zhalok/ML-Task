def check_values(df):
    missing_values = df.isnull().sum()
    nan_values = df.isna().sum()
    duplicates = df.duplicated().sum()
    unique_values = df.nunique()

    column_status = pd.DataFrame({
        "missing_values": missing_values,
        "nan_values": nan_values,
        "duplicates": duplicates,
        "unique_values": unique_values,
    })

    print(column_status)

def plot_grouped_data(groupby_column,df):
    grouped_data = df[["Total_sales",groupby_column]].groupby(groupby_column).mean()
    grouped_data.plot(kind='bar', color='skyblue', edgecolor='black')
    
def get_season(month):
    if month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Autumn'
    else:
        return 'Winter'