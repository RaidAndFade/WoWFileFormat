import json
j = json.load(open("types.json"))

types = {}
for x in j:
    t = j[x]
    if t in types:
        types[t].append(x)
    else:
        types[t] = [x]

json.dump(types,open("byhdr.json","w+"))