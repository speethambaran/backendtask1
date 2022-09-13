from fastapi import FastAPI
from google.cloud import bigquery
from flask import jsonify
import functions_framework
import os
import time

credentials_path = 'infoworkflow36-d2f2af6ad4c2.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
#Construct a BigQuery client object.
client = bigquery.Client()
table_id = 'infoworkflow36.input_validate_dataset.input_validate_table'
@functions_framework.http
def process(request):
    request_json = request.get_json()
    x = request_json['input']
    rows_to_insert = [
        {u'input': x}
    ]
    time.sleep(10) #180
    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors == []:
        print('new rows added')
        output = {"got sucess": x, "output": "sucess"}
        return jsonify(output)
    else:
        print(f'not working:, {errors}')
        output = {"got it": x, "output": "failed"}
        return jsonify(output)