def transform_data(df):
    
    # fill missing salary with average
    df['salary'] = df['salary'].fillna(df['salary'].mean())
    
    # remove duplicates
    df = df.drop_duplicates()
    
    print("Data Transformed Successfully")
    return df
