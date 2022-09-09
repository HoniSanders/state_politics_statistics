import os
import pandas as pd
import numpy as np
from pathlib import Path

dirr = 'Legislative_Control_csvs'

source_csv = 'statelegislaturecomposition_orig.csv'
final_csv = 'statelegislaturecomposition.csv'
with open(source_csv) as f:
    master_df = pd.read_csv(f)
    master_df = master_df[master_df['State'] != '']
    master_df = master_df.dropna(how='all')

print(master_df.shape)
print(master_df.head())

for file in os.listdir(dirr):
    year = file.split('_')[1].split('.')[0]
    print(file, year)
    try:    # avoid .DS_Store
        a=int(year)-0
    except ValueError:
        continue
    with open(Path(dirr)/file) as f:
        tmp_df = pd.read_csv(f)
        #print(tmp_df.columns.values.tolist())
        tmp_df = tmp_df[tmp_df.STATE != '']
        tmp_df = tmp_df.dropna(how='all')
        print(year, tmp_df.shape)
        if year in master_df.columns.values.tolist():
            print(master_df[master_df[year] != tmp_df['Legislature Control']])
        else:
            master_df[year] = tmp_df['Legislature Control']
cols = master_df.columns.values.tolist()
print(cols)
print(master_df.columns.sort_values(ascending=False))
master_df = master_df[master_df.columns.sort_values(ascending=False)]
print(master_df.columns.values.tolist())
master_df.to_csv(final_csv, index=False)
