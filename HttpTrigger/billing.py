import requests
import json
from datetime import date,timedelta

def get_token(id,secret):
    login_url = "ID:"+id+"Secret:"+secret;
    return login_url;

class AzureBilling():
    def __init__(self,id,secret,scope):
        self.id = id;
        self.secret = secret;
        self.scope = scope;
        self.token = get_token(id,secret);

    def get_token(self):
        login_url = "";

    def print(self):
        print(self.token);

#    def query(self):
