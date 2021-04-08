import PyCASC
import json

casc = PyCASC.DirCASCReader("/Volumes/Sep\'s Disk/World of Warcraft")

# def dump_files():
#     global casc

#     json.dump(casc.list_files(),open("files.json","w+"))

# dump_files()

def guess_type(f):

    return f[:4]
def guess_unknowns():
    global casc

    fl = casc.list_files()

    typetbl = {}

    for x in fl:
        if "FILE_BY_ID" in x[0]:
            try:
                f = casc.get_file_by_ckey(x[1],max_size=16)
                typetbl[x[0]] = str(guess_type(f))
                print(f"{x[0]} has hdr {typetbl[x[0]]w}")
            except:
                print("Failed to read "+x[0])
    
    print(typetbl)
    json.dump(typetbl,open("types.json","w+"))

guess_unknowns()