import os
from src.extractors.api_extractor import FootballExtractor
from src.extractors.s3_extractor import S3Extractor
from src.transformers.data_transformer import DataTransformer
from src.loaders.db_loader import DBLoader
from src.utils.notifications import SlackNotifier

def run_pipeline():
    notifier = SlackNotifier(webhook_url=os.getenv("SLACK_WEBHOOK"))
    
    try:
        db_config = {
            "user": "postgres",
            "password": "TU_CONTRASEÑA",
            "host": "localhost",
            "port": "5432",
            "database": "stori_db"
        }

        api_ext = FootballExtractor()
        s3_ext = S3Extractor(bucket_name="stori-challenge-bucket")

        df_api = api_ext.get_fixtures_by_date()
        df_s3 = s3_ext.extract_csv("stadiums_metadata.csv")

        if df_api is not None and df_s3 is not None:
            transformer = DataTransformer()
            df_final = transformer.enrich_football_data(df_api, df_s3)

            loader = DBLoader(db_config)
            loader.save_to_db(df_final, "fact_football_matches")
        else:
            raise Exception("No se pudieron obtener datos de las fuentes.")

    except Exception as e:
        notifier.send_error(str(e))
        print(f"Proceso fallido: {e}")

if __name__ == "__main__":
    run_pipeline()