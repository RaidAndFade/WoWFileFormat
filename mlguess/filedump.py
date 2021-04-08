import PyCASC
import csv

casc = PyCASC.DirCASCReader("/Volumes/Sep\'s Disk/World of Warcraft")

i = 0

def getClassification(x):
    n = x[0]
    
    if "FILE_BY_ID" in n:
        return None

    return n.split(".")[-1].upper()

with open("headerdump.csv","w+") as df:
    cv = csv.writer(df)
    fl = casc.list_files()
    fll = len(fl)
    for x in fl:
        i += 1
        if i%1000 == 0:
            print(f"[+] Processed {i}/{fll}.")
        # if i == 250:
        #     break

        try:
            cl = getClassification(x)

            if cl is None:
                continue

            d = casc.get_file_by_ckey(x[1],max_size=35)

            if len(d) >= 35:   
                cv.writerow([cl,list(d[:35]),x[0]])
        except:
            print(f"[-] Failed on {x[0]}, skipping.")