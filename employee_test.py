import pandas as pd
import numpy as np

df = pd.read_csv("employee_list.csv")
#print(df)

'''
df.head() - first 5 rows
df.tail() - last 5 rows
df.info() - data types, memory usage, ect
df.describe() - summary statistic for the numerical columns
df.columns - column names as a list
df.index - gives us the range of csv file
'''
print(df.columns)