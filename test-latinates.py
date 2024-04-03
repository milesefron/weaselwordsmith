import json
import re




def update_regexes():
    file = './data/latinate-words.json'
    with open(file, 'r') as f:
        latins = json.load(f)

    new = {}
    for latin in latins.keys():
        entry = latins[latin]
        regex = r"\W" + entry.get('regex')
        entry['regex'] = regex
        new[latin] = entry

    with open(file, 'w') as f:
        json.dump(new, f, indent=4)




file = './data/latinate-words.json'
with open(file, 'r') as f:
    latins = json.load(f)

text = ' ireland you must be tired'
for latin in latins.keys():
    regex = latins.get(latin).get('regex')
    if re.findall(regex, text):
        print(latin, regex)