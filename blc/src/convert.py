import os
import pandas as pd


with os.scandir('samples/almost/HR_edges.csv') as entries:
    for entry in entries:
        df = pd.read_csv('samples/almost/'+entry.name, sep='\t', header=None)
        df.to_csv('modified/'+entry.name, sep=' ', header=None, index=None)
