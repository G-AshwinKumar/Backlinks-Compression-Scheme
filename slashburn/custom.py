import pandas as pd
import os

# file_path should be the full path of wherever your csv file is located
# this loads the csv into a pandas data frame
# a convenient table-like data structure
print(os.listdir())
df = pd.read_csv(r'data/graph/S.txt')

# get the max values in every column
column_maxes_series = df.max()
print("column_maxes_series")
print(column_maxes_series)
# get the max value of the Series
overall_max = column_maxes_series.max()
print(type(overall_max))
print("The overall max: ")
print(overall_max)
