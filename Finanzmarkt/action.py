# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 23:42:07 2021

@author: kraft
"""
import pandas as pd
from pivot import PivotMaker


table_obj = PivotMaker("root", "localhost", "finance", "dax")
data = table_obj.select_indices()
table_obj.collecter(data)

current_hits = table_obj.current_hits
preVolume = table_obj.pre_volume

sample_data = dict(PreVolume=[], PreDate=[], MoveP=[], Date=[], Volume=[])

sample_data["MoveP"] = current_hits["s3"]["MoveP"][:]
sample_data["PreDate"] = preVolume["s3"]["PreDate"][:]
sample_data["PreVolume"] = preVolume["s3"]["Volume"][:]
sample_data["Date"] = current_hits["s3"]["Date"][:]
sample_data["Volume"] = current_hits["s3"]["Volume"][:]

df_anal = pd.DataFrame(sample_data, columns=["PreVolume", "PreDate", 
                                             "MoveP", "Date", "Volume"])
print(df_anal.info())
print(df_anal.corr())