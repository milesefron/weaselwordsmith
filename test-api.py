import json
import requests

api_endpoint ='https://tyernluxoa.execute-api.us-east-1.amazonaws.com/v1'
api_method = 'stats'
text = "This is a test test test. this could happen. It, is possible, it really could."
parameters = {'text': text}
r = requests.post(url = api_endpoint + '/' + api_method, params = parameters)
part_analysis = r.json()
print(json.dumps(part_analysis, indent=4))
