import os
from src.extractors.api_extractor import FootballExtractor
from src.extractors.s3_extractor import S3Extractor
from src.transformers.data_transformer import DataTransformer
from src.loaders.db_loader import DBLoader

def run_pipeline():
    db_config = {
        "user": "postgres",
        "password": "TU_CONTRASEÑA_AQUI",
        "host": "localhost",
        "port": "5432",
        "database": "stori_db"
    }

    print("Iniciando Ingesta...")
    api_ext = FootballExtractor()
    s3_ext = S3Extractor(bucket_name="stori-challenge-bucket")

    df_api = api_ext.get_fixtures_by_date()
    df_s3 = s3_ext.extract_csv("stadiums_metadata.csv")

    if df_api is not None and df_s3 is not None:
        print("Iniciando Transformación...")
        transformer = DataTransformer()
        df_final = transformer.enrich_football_data(df_api, df_s3)

        print("Iniciando Carga en DB...")
        loader = DBLoader(db_config)
        loader.save_to_db(df_final, "fact_football_matches")
        print("Proceso completado exitosamente.")
    else:
        print("Error: No se pudo obtener información de las fuentes.")

if __name__ == "__main__":
    run_pipeline()