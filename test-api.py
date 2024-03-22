import json
import requests

api_endpoint ='https://tyernluxoa.execute-api.us-east-1.amazonaws.com/v1'
api_method = 'latinate'
text = "This is a  i opt quickly thing test test test. this judicious could happen. It, is possible, it really could."
parameters = {'text': text}
r = requests.post(url = api_endpoint + '/' + api_method, params = parameters)
part_analysis = r.json()
print(json.dumps(part_analysis, indent=4))
