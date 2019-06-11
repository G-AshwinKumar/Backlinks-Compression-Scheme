import os
import pandas as pd


with os.scandir('data/convert') as entries:
    for entry in entries:
        df = pd.read_csv('data/convert/'+entry.name, sep='\s+', header=None)
        df.to_csv('modified/'+entry.name, header=None, index=None)
