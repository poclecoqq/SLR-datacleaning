import pandas as pd
import pathlib
import os

crnt_path = pathlib.Path(__file__).parent.resolve()
df = pd.read_csv(crnt_path/"papers.csv")
for _, row in df.iterrows():
    if row['Relevant'] == "YES":
        name = row['Name']
        if len(df[df['Name'] == name]) > 1 or len(df[df['Name'] == name+' [arXiv]']) > 0:
            print(name)
