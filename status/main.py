from fastapi import FastAPI, HTTPException, status
import requests, os
from google.cloud import bigquery
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import workflows_v1beta
from google.cloud.workflows import executions_v1beta

app = FastAPI()

cred = credentials.Certificate('infoworkflow36-6865f12a3d08.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.get('/checkstatus')
async def status(x):
    # workflow connect
    project = 'infoworkflow36'
    location = 'us-central1'
    workflow = 'input-validate-workflow'

    # firebase credentials

    collection = db.collection(u'fastapibackend')
    doc = collection.document(x)
    res = doc.get().to_dict()
    print(res)

    credentials_path = 'infoworkflow36-eef33eab504d.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

    # workflow execution
    execution_client = executions_v1beta.ExecutionsClient()
    workflows_client = workflows_v1beta.WorkflowsClient()

    # Construct a BigQuery client object.
    client = bigquery.Client()
    table = client.get_table('infoworkflow36.input_validate_dataset.input_validate_table')
    table_id = table
    rows_iter = client.list_rows(table_id)  # Make an API request.

    # Making a get request

    response = requests.get('https://us-central1-infoworkflow36.cloudfunctions.net/execute_workflow?input='+x)

    # print response
    print(response)

    # print request status_code
    print(response.status_code)
    if response.status_code == 200:
        return {"response": response.status_code}
    else:
        return {"firebase_state": res}
