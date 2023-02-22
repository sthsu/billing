import logging
import os,sys
import azure.functions as func

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0,dir_path)
from billing import *

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    az = AzureBilling("a","b","c")

    az.print();

    if True:
        return func.HttpResponse(az.token)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
