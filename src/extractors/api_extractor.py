import requests
import pandas as pd
from datetime import datetime

class FootballExtractor:
    def __init__(self, api_key="TU_API_KEY_AQUI"):
        # Usaremos un endpoint de prueba o una URL base estructurada
        self.base_url = "https://v3.football.api-sports.io"
        self.headers = {
            'x-rapidapi-host': "v3.football.api-sports.io",
            'x-rapidapi-key': api_key
        }

    def get_fixtures_by_date(self, league_id=39, date=None):
        """
        Extrae partidos de una liga (39 = Premier League) en una fecha específica.
        Esto cumple con la 'ingesta incremental' basada en fechas.
        """
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
            
        endpoint = f"{self.base_url}/fixtures"
        params = {"league": league_id, "season": 2023, "date": date}
        
        try:
            # En un entorno real, aquí harías el request
            # response = requests.get(endpoint, headers=self.headers, params=params)
            # data = response.json()
            
            # Simulacro de datos para que puedas correrlo localmente sin API KEY aún [cite: 17]
            mock_data = [
                {"fixture": {"id": 101, "date": date}, "teams": {"home": {"name": "Arsenal"}, "away": {"name": "Chelsea"}}, "goals": {"home": 2, "away": 1}},
                {"fixture": {"id": 102, "date": date}, "teams": {"home": {"name": "Liverpool"}, "away": {"name": "City"}}, "goals": {"home": 0, "away": 0}}
            ]
            
            df = pd.json_normalize(mock_data)
            # Añadimos metadatos de transformación como pide el reto 
            df['ingested_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            return df
            
        except Exception as e:
            print(f"Error en la extracción de fútbol: {e}")
            return None

if __name__ == "__main__":
    extractor = FootballExtractor()
    # Probamos traer los datos de "hoy"
    df_partidos = extractor.get_fixtures_by_date()
    print("--- Datos extraídos de la API de Fútbol ---")
    print(df_partidos.head())