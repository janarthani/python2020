# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:58:50 2020

@author: Janu

This is my API call practice.
"""

# =============================================================================
# import requests
# 
# r = requests.get('https://reqres.in/api/users/2')
# print (r.json())
# 
# =============================================================================

import requests
import json

API_KEY = "tvqMUraccM_P"
PROJECT_TOKEN =  "tfK498xDYawp"
RUN_TOKEN = "tygyzXJSH1B5"

response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={"api_key": API_KEY})
data = json.loads(response.text)

print(data)