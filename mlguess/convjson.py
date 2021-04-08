import pandas as pd

import json

data = pd.read_csv("headerdump.csv",header=None,names=("TYPE","DATA","PATH"))

inputs = data['DATA'].apply(json.loads).apply(pd.Series)

outputs_ext = data[["TYPE"]]

paths = data["PATH"].str.split("/", n = 1, expand = True) 

data['DIR'] = paths[0]

outputs_path = data[['DIR']]

# outputs_path = data[["PATH"]].apply(lambda x:x.split("/")[0])

inputs.to_csv("inputs.csv")
outputs_ext.to_csv("outputs_ext.csv")
outputs_path.to_csv("outputs_dir.csv")