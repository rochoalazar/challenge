import psycopg2
from sqlalchemy import create_all

class DBLoader:
    def __init__(self, db_config):
        self.user = db_config['user']
        self.password = db_config['password']
        self.host = db_config['host']
        self.port = db_config['port']
        self.database = db_config['database']

    def save_to_db(self, df, table_name):
        if df is None:
            return
        
        from sqlalchemy import create_engine
        conn_string = f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
        engine = create_engine(conn_string)
        
        try:
            df.to_sql(table_name, engine, if_exists='append', index=False)
            print(f"Data successfully loaded to {table_name}")
        except Exception as e:
            print(f"Error loading to DB: {e}")

if __name__ == "__main__":
    import pandas as pd
    config = {
        "user": "postgres",
        "password": "Thomaspiketty8",
        "host": "localhost",
        "port": "5432",
        "database": "stori_db"
    }
    loader = DBLoader(config)
    test_df = pd.DataFrame({'test_col': [1, 2]})
    loader.save_to_db(test_df, "test_table")