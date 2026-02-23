import pandas as pd
from datetime import datetime

class DataTransformer:
    def __init__(self):
        pass

    def enrich_football_data(self, df_fixtures, df_stadiums):
        if df_fixtures is None or df_stadiums is None:
            return None

        df_enriched = pd.merge(
            df_fixtures, 
            df_stadiums, 
            left_on='teams.home.name', 
            right_on='team_name', 
            how='left'
        )

        df_enriched['total_goals'] = df_enriched['goals.home'] + df_enriched['goals.away']
        df_enriched['is_high_scoring'] = df_enriched['total_goals'] > 2
        df_enriched['transformation_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        columns_to_keep = [
            'fixture.id', 'fixture.date', 'teams.home.name', 'teams.away.name', 
            'goals.home', 'goals.away', 'total_goals', 'is_high_scoring', 
            'stadium', 'city', 'transformation_date'
        ]
        
        return df_enriched[columns_to_keep]

if __name__ == "__main__":
    from src.extractors.api_extractor import FootballExtractor
    from src.extractors.s3_extractor import S3Extractor

    api_ext = FootballExtractor()
    s3_ext = S3Extractor("stori-bucket")

    df_api = api_ext.get_fixtures_by_date()
    df_s3 = s3_ext.extract_csv("metadata.csv")

    transformer = DataTransformer()
    final_df = transformer.enrich_football_data(df_api, df_s3)
    print(final_df)
    