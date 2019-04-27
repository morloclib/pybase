import json
import pandas as pd
import numpy as np

unpackGeneric = json.loads
packGeneric = json.dumps

def unpackDataFrame(df):
    return(df.to_json())

def packDataFrame(json):
    return(pd.read_json(json))

#  JSON -> Matrix
def unpackMatrix(x):
    return(np.matrix(j.loads(x)))

#  Matrix -> JSON
def packMatrix(x):
    return(j.dumps(x.tolist()))
