import numpy as np
import pandas as pd
import os
from ppr import PPRBear as Bear
import time
# file_path should be the full path of wherever your csv file is located
# this loads the csv into a pandas data frame
# a convenient table-like data structure

graphname = 'tvshow_edges.csv'
filename = "data/graph/"+graphname
df = pd.read_csv(filename, sep=',')

# get the max values in every column
column_maxes_series = df.max()
column_min_series = df.min()
# get the max value of the Series
overall_max = column_maxes_series.max()
# to avoid exceeding index while computation
overall_max = overall_max+1
print("Graph: " + graphname)
print("Edges: "+str(df.shape[0]))
bear = Bear()
start = time.time()
# bear.preprocess('modified/'+str(filename))
bear.preprocess(filename)
end = time.time()
print("Slashburn Reordering time: "+str(end - start)+"s")
# custom bin file similar
byte_size = os.path.getsize("data/compressed/"+graphname)
bit_length = byte_size * 8
print("Bit length:" + str(bit_length))
print("Bits/Edge: " + str(bit_length/(df.shape[0])))
