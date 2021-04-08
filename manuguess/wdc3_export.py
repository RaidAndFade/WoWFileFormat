import PyCASC
import json


unk = json.load(open("unk.json"))

fnmap = {k[0]:k[1] for k in unk}

byhdr = json.load(open("byhdr.json"))

wdb3l = [] 

for x in byhdr["b'WDC3'"]:
    wdb3l.append((fnmap[x],x[11:]))

print(wdb3l)

casc = PyCASC.DirCASCReader("/Volumes/Sep\'s Disk/World of Warcraft")

for x in wdb3l:
    d = casc.get_file_by_ckey(x[0])
    with open(f"wdc3/{x[1]}.dbc","wb+") as f:
        f.write(d)

    