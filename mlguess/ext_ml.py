import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

import joblib


inputs = pd.read_csv("inputs.csv",usecols=range(1,36))

outputs = pd.read_csv("outputs_ext.csv",usecols=[1])

inputs_train, inputs_test, outputs_train, outputs_test = \
    train_test_split (inputs, outputs, test_size = 0.33, random_state = 42)

rf = RandomForestClassifier(n_estimators=100)

rf.fit(inputs_train,outputs_train)

acc = rf.score(inputs_test,outputs_test)

print(f"Model trained with {acc:f}% accuracy.")

joblib.dump(rf,"FileExtModel.joblib")