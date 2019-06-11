import numpy as np
import pandas as pd
import os
from ppr import PPRBear as Deer

# file_path should be the full path of wherever your csv file is located
# this loads the csv into a pandas data frame
# a convenient table-like data structure

df = pd.read_csv(r"data/graph/Slashdot0811.txt", sep=',')

# get the max values in every column
column_maxes_series = df.max()
column_min_series = df.min()
# get the max value of the Series
overall_max = column_maxes_series.max()
print(type(overall_max))
# to avoid exceeding index while computation
overall_max = overall_max+1
print(overall_max)
print("Graph: "+graphname)
print("Edges: "+str(df.shape[0]))
deer = Deer()
# bear.preprocess('modified/'+str(filename))
deer.preprocess('data/graph/Slashdot0811.txt')
# custom bin file similar
byte_size = os.path.getsize('slashburn.bin')
bit_length = byte_size * 8
print("Bit length:" + str(bit_length))
print("Bits/Edge: " + str(bit_length/(df.shape[0])))
