import boto3
import pandas as pd
from io import StringIO
import geopandas as gpd

client = boto3.client('s3')

bucket_name = 'ds-interview-sandbox'

object_key = 'shared/uga_regions.geojson'
csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
body = csv_obj['Body']
csv_string = body.read().decode('utf-8')

#df = pd.read_csv(StringIO(csv_string))
df = gpd.read_file(StringIO(csv_string))

print(df.head())
exit(0)


from sqlalchemy import create_engine
from urllib.parse import quote_plus
  
# establish connections
conn_string = 'postgresql://recruitee:%s@127.0.0.1/sandbox'% quote_plus("FraymSandboxP@ssword2022")
  
db = create_engine(conn_string)
conn = db.connect()

#df.to_sql('uga_regions', conn, if_exists= 'replace')
df.to_postgis("uga_regions", db,  if_exists= 'replace')  
