import os
import psycopg2
from flask import Flask,request
from urllib.parse import quote_plus


app = Flask(__name__)
url = 'postgresql://recruitee:%s@127.0.0.1/sandbox'% quote_plus("FraymSandboxP@ssword2022")
connection = psycopg2.connect(url)

@app.get("/api/count")
def get_count_by_sex_region():
    sex = request.args.get('sex')
    region = request.args.get('area')
    query ="select count(*) from (select v001, \"LATNUM\", \"LONGNUM\", iso_code from (select ug_clusters.v001, \"LATNUM\", \"LONGNUM\", sex from ug_clusters inner join uga_dhs_2016 on ug_clusters.v001=uga_dhs_2016.v001 where sex='"+ sex + "') as A, uga_regions where  ST_WITHIN(st_setsrid(ST_MakePoint(\"LONGNUM\", \"LATNUM\"),4326), geometry) and iso_code ~ '^" + region +"') as B"
    print(query)
    count=0
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            count = cursor.fetchone()[0]
    print(count)
    return {"count": count}


app.run(debug=True)
