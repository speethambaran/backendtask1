import os
import time
from fastapi import FastAPI
from google.cloud import workflows_v1beta
from google.cloud.workflows import executions_v1beta
from google.cloud.workflows.executions_v1beta.types import executions
from google.cloud.workflows.executions_v1beta.services.executions import ExecutionsClient
from google.cloud.workflows.executions_v1beta.types import CreateExecutionRequest, Execution
import functions_framework
from flask import jsonify
import json

@functions_framework.http
def execute_workflow(request):
    y = request.args
    x = y['input'] #value in x
    # workflow connect
    project = 'infoworkflow36'
    location = 'us-central1'
    workflow = 'input-validate-workflow'
    arguments = {"input1": x}

    credentials_path = 'infoworkflow36-eef33eab504d.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

    if not project:
        raise Exception('GOOGLE_CLOUD_PROJECT env var is required.')
    parent = "projects/{}/locations/{}/workflows/{}".format(project, location, workflow)
    execution = Execution(argument=json.dumps(arguments))

    client = ExecutionsClient()
    response = None

    try:
        response = client.create_execution(parent=parent, execution=execution)
    except:
        return "Error occurred when triggering workflow execution", 500
    return {"workflow-id": response.workflow_revision_id}
