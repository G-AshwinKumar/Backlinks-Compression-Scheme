import os
import pandas as pd


with os.scandir('samples/almost') as entries:
    for entry in entries:
        df = pd.read_csv('samples/almost/'+entry.name, sep=',', header=None)
        df.to_csv('modified/'+entry.name, sep=' ', header=None, index=None)
