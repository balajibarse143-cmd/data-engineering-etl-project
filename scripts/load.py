from sqlalchemy import create_engine

def load_data(df):
    
    connection_string = "sqlite:///employee.db"
    engine = create_engine(connection_string)
    
    df.to_sql("employees", engine, if_exists="replace", index=False)
    
    print("Data Loaded Successfully")
