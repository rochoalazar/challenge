import boto3
import pandas as pd
from botocore.exceptions import ClientError

class S3Extractor:
    def __init__(self, bucket_name):
        self.s3 = boto3.client('s3')
        self.bucket = bucket_name

    def check_file_exists(self, file_key):
        try:
            self.s3.head_object(Bucket=self.bucket, Key=file_key)
            return True
        except ClientError:
            return False

    def extract_csv(self, file_key):
        if not self.check_file_exists(file_key):
            print(f"File {file_key} not found.")
            return None
            
        mock_data = {
            'team_name': ['Arsenal', 'Chelsea', 'Liverpool', 'City'],
            'stadium': ['Emirates Stadium', 'Stamford Bridge', 'Anfield', 'Etihad Stadium'],
            'city': ['London', 'London', 'Liverpool', 'Manchester']
        }
        return pd.DataFrame(mock_data)

if __name__ == "__main__":
    extractor = S3Extractor("stori-challenge-bucket")
    df = extractor.extract_csv("stadiums_metadata.csv")
    print(df)