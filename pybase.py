import json
#  import pandas as pd
#  import numpy as np

unpackGeneric = json.loads
packGeneric = json.dumps


def packList(x):
  return json.dumps(list(x))

def unpackList(x):
  return json.loads(x)

packFloatList = packList
unpackFloatList = unpackList

#  def packDataFrame(df):
#      return(df.to_json(orient="table"))
#  #### example format for a character count table
#  #  {
#  #      "schema": {
#  #          "fields":[
#  #              {"name":"index","type":"string"},
#  #              {"name":"count","type":"integer"}
#  #          ],
#  #          "primaryKey":["index"],
#  #          "pandas_version":"0.20.0"
#  #      },
#  #      "data": [
#  #          {"index":"f","count":2},
#  #          {"index":"d","count":2},
#  #          {"index":"s","count":1}
#  #      ]
#  #  }
#
#  def unpackDataFrame(json):
#      return(pd.read_json(json))
#
#  #  JSON -> Matrix
#  def unpackMatrix(x):
#      return(np.matrix(json.loads(x)))
#
#  #  Matrix -> JSON
#  def packMatrix(x):
#      return(json.dumps(x.tolist()))
