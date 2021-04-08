import PyWDBX
import os

for x in os.listdir("wdc3"):
    x = "wdc3/"+x
    db = PyWDBX.DBCParser(open(x,"rb"))

    # print(db._file_data)
    d,p = db.process(db,None)
    print(d)
    # print(p)
    print(x)
    break
    # print(db.find_name())