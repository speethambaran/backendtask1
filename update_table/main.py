from fastapi import FastAPI
from google.cloud import bigquery
from flask import jsonify
import functions_framework
import os
import time
import calendar

credentials_path = 'infoworkflow36-d2f2af6ad4c2.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
#Construct a BigQuery client object.
client = bigquery.Client()
table_id = 'infoworkflow36.input_validate_dataset.result_check_table'
@functions_framework.http
def data_to_table(request):
    request_json = request.get_json()
    
    x = request_json['name']
    y = request_json['valid_input_check']
    z = request_json['process']
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    
    rows_to_insert = [
        {u'name': x,'valid_input_check':y,'process':z,'timestamp':time_stamp}
    ]
    #time.sleep(10) #180
    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors == []:
        print('new rows added')
        output = {"name":x , "valid_input_check":y, "process":z, "output": "sucess"}
        return jsonify(output)
    else:
        print(f'not working:, {errors}')
        output = {"got it": "x", "output": "failed"}
        return jsonify(output)