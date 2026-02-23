import boto3
import pandas as pd
from botocore.exceptions import ClientError, NoCredentialsError

class S3Extractor:
    def __init__(self, bucket_name):
        self.bucket = bucket_name
        try:
            self.s3 = boto3.client('s3', region_name='us-east-1')
        except Exception:
            self.s3 = None

    def check_file_exists(self, file_key):
        if not self.s3:
            return False
        try:
            self.s3.head_object(Bucket=self.bucket, Key=file_key)
            return True
        except (ClientError, NoCredentialsError):
            return False

    def extract_csv(self, file_key):

        mock_data = {
            'team_name': ['Leanne Graham', 'Ervin Howell', 'Clementine Bauch', 'Patricia Lebsack'],
            'stadium': ['Emirates Stadium', 'Stamford Bridge', 'Anfield', 'Etihad Stadium'],
            'city': ['London', 'London', 'Liverpool', 'Manchester']
        }
        
        try:
            if self.s3 and self.check_file_exists(file_key):
                obj = self.s3.get_object(Bucket=self.bucket, Key=file_key)
                return pd.read_csv(obj['Body'])
            else:
                print(f"Alerta: No se pudo conectar a S3 o el archivo {file_key} no existe. Usando datos locales de respaldo.")
                return pd.DataFrame(mock_data)
        except Exception as e:
            print(f"Error inesperado en S3: {e}. Continuando con datos locales.")
            return pd.DataFrame(mock_data)

if __name__ == "__main__":
    extractor = S3Extractor("prueba-bucket-challege")
    df = extractor.extract_csv("stadiums_metadata.csv")
    print(df)