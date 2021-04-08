import PyCASC
import csv

import numpy as np

casc = PyCASC.DirCASCReader("/Volumes/Sep\'s Disk/World of Warcraft")

import joblib
ext_rf = joblib.load("FileExtModel.joblib")
dir_rf = joblib.load("FileDirModel.joblib")

fl = casc.list_files()
for x in fl:
    if "FILE_BY_ID" in x[0]:
        try: 
            d = casc.get_file_by_ckey(x[1],max_size=35)
        except:
            print(f"Failed to read {x[0]}")
            continue

        if len(d) >= 35:
            ty = ext_rf.predict([list(d[:35])])
            drp = dir_rf.predict_proba([list(d[:35])])
            dr = "unk"
            print(drp,np.argmax(drp))
            if drp[np.argmax(drp)]>=0.75:
                dr = dir_rf.classes_[np.argmax(drp)]
            print(x[0][11:],ty,dr,d[:35])

        # except:
        #     print(f"Failed to predict {x[0]}")