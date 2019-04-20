import json
import pandas as pd
import numpy as np

unpackGeneric = json.loads
packGeneric = json.dumps

def unpackDataFrame(df):
    return(df.to_json())

def packDataFrame(json):
    return(pd.read_json(json))
