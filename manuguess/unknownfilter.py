import json

j = json.load(open("files.json","r+"))
o = []

for e in j:
    if "FILE_BY_ID" in e[0]:
        o.append(e)

json.dump(o,open("unk.json","w+"))