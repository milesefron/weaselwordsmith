import json
import requests
from textwrap import wrap

def handle_long_text(text, max_length, api_endpoint, api_method):
    analysis = {
        'counts': {},
        'sentences': {}
    }
    if 'latinate' in api_method:
        analysis['alternatives'] = {}

    parts = wrap(text, max_length)
    for part in parts:
        parameters = {'text': part}
        print(api_endpoint + '/' + api_method)
        r = requests.post(url = api_endpoint + '/' + api_method, params = parameters)
        part_analysis = r.json()


        for term in part_analysis['counts']:
            current = analysis.get('counts').get(term, 0)
            analysis['counts'][term] = current + part_analysis['counts'][term]


        for term in part_analysis['sentences']:
            current = analysis.get('sentences').get(term, [])
            for sentence in part_analysis['sentences'][term]:
                current.append(sentence)
                analysis['sentences'][term] = current
        
        for term in part_analysis['alternatives']:
            analysis['alternatives'][term] = part_analysis['alternatives'][term]
                
    analysis['counts'] = dict(sorted(analysis['counts'].items(), key=lambda x:x[1], reverse=True))
    return analysis