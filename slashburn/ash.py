import numpy as np
import pandas as pd
import os
from ppr import PPRBear as Deer
import tensorflow as tf

# file_path should be the full path of wherever your csv file is located
# this loads the csv into a pandas data frame
# a convenient table-like data structure


graphname = 'Slashdot0811'
filename = graphname+'.txt'
print(os.listdir())
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
#sess = tf.Session()
#bear = Bear(sess, 100, filename)
deer = Deer()
# bear.preprocess('modified/'+str(filename))
deer.preprocess('data/graph/Slashdot0811.txt')

""" To find width of each column
print(column_maxes_series[0]-column_min_series[0]+1)
print(column_maxes_series[1]-column_min_series[1]+1) 
"""


# To find ppr of a given node bear.query(self,node_to_find_ppr)
# r = bear.query(
#   np.ones(column_maxes_series[0]-column_min_series[0]+1)/(column_maxes_series[1]-column_min_series[1]+1))
#   np.ones(overall_max)/overall_max)

# Tried different compression standards to find balance between speed and compression ratio
# Note: Definition removed in utils will throw errors
# byte_size = os.path.getsize('smallerfile')
# bz2 compression
#bit_length = byte_size * 8
#print("Bit length:" + str(bit_length))
#print("Bits/Edge: " + str(bit_length/(overall_max-1)))

# custom dat file similar in performance to bin
#byte_size = os.path.getsize('AF_custom.dat')
#bit_length = byte_size * 8
#print("Bit length:" + str(bit_length))
#print("Bits/Edge: " + str(bit_length/(overall_max-1)))

# custom bin file similar
byte_size = os.path.getsize('slashburn.bin')
bit_length = byte_size * 8
print("Bit length:" + str(bit_length))
print("Bits/Edge: " + str(bit_length/(df.shape[0])))

# To print computed ppr
#  print(r.sum())
