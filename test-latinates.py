import json
import re

file = '../rescue/story.txt'
with open(file, 'r') as f:
    text = f.read().replace('\n', ' ').replace('  ', ' ')

file = './latinate-words.json'
with open(file, 'r') as f:
    latinates = json.load(f)
print(json.dumps(latinates, indent=4))

sentences = text.split('. ')

for sentence in sentences:
    for latinate in latinates.keys():
        if re.findall(latinates[latinate]['regex'], sentence, re.IGNORECASE):
            #print(latinate, latinates[latinate])
            print("<entry>" + latinate + "</entry>", sentence)
