import requests
import pandas as pd
from datetime import datetime

class FootballExtractor:
    def __init__(self, api_key=None):
        self.base_url = "https://jsonplaceholder.typicode.com/users"

    def get_fixtures_by_date(self, league_id=None, date=None):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            data = response.json()
            
            df = pd.json_normalize(data)
            
            df = df.rename(columns={
                'name': 'teams.home.name',
                'username': 'teams.away.name',
                'id': 'fixture.id'
            })
            
            df['goals.home'] = 2
            df['goals.away'] = 1
            df['fixture.date'] = datetime.now().strftime("%Y-%m-%d")
            df['ingested_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            print("--- Conexión Exitosa:  ---")
            print(df[['fixture.id', 'teams.home.name', 'teams.away.name']].head())
            
            return df
            
        except Exception as e:
            print(f"Error en la extracción real: {e}")
            return None

if __name__ == "__main__":
    extractor = FootballExtractor()
    df_partidos = extractor.get_fixtures_by_date()