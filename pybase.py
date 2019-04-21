import json
import pandas as pd
import numpy as np

unpackGeneric = json.loads
packGeneric = json.dumps

def unpackDataFrame(df):
    return(df.to_json(orient="table"))
#### example format for a character count table
#  {
#      "schema": {
#          "fields":[
#              {"name":"index","type":"string"},
#              {"name":"count","type":"integer"}
#          ],
#          "primaryKey":["index"],
#          "pandas_version":"0.20.0"
#      },
#      "data": [
#          {"index":"f","count":2},
#          {"index":"d","count":2},
#          {"index":"s","count":1}
#      ]
#  }

def packDataFrame(json):
    return(pd.read_json(json))
