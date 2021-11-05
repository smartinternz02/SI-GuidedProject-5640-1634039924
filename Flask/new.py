import requests

import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "kts70omrII5P-4S9XCV-xWlxqmQouW65uEqcB__CiWIA"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["mfr","type","G1","G2","G3","G4","G5","G6","calories","protein","fat","sodium","fiber","carbo","sugars","potass","vitamins","shelf","weight","cups"]], "values": [[  0.  ,   1.  ,   0.  ,   0.  ,   0.  ,   0.  ,   0.  ,   0.  ,
       100.  ,   2.  ,   1.  , 140.  ,   2.  ,  11.  ,  10.  , 120.  ,
        25.  ,   3.  ,   1.  ,   0.75]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/d18d52cb-55ec-40df-9e62-b8de982c3585/predictions?version=2021-10-28', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
predictions=response_scoring.json()
print("Final Prediction:")
print(predictions['predictions'][0]['values'][0][0])
#print(prediction)
