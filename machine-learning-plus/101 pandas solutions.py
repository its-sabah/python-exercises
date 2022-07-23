# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 10:55:26 2022

@author: sabah

Purpose: Working on tasks from:
    https://www.machinelearningplus.com/python/101-pandas-exercises-python/
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy


# 1. How to import pandas and check the version?
pd.show_versions
#%%
# 2. How to create a series from a list, numpy array and dict?
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

list_series = pd.Series(mylist)
arr_series = pd.Series(myarr)
dict_series = pd.Series(mydict)

print(list_series, arr_series, dict_series)
#%%
# 3. How to convert the index of a series into a column of a dataframe?
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)

df = pd.DataFrame(ser).reset_index()
del mylist, myarr, mydict, list_series, arr_series, dict_series
#%%
# 4. How to combine many series to form a dataframe?
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df = pd.DataFrame({"col1": ser1, 
                   "col2": ser2})
#%%
# 5. How to assign name to the series’ index?
ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser.name = 'aphabets'

print(ser.head())
#%%
# 6. How to get the items of series A not present in series B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

     # my soln 1
ser_u = pd.Series(np.union1d(ser1, ser2))
ser_i = pd.Series(np.intersect1d(ser1, ser2))
print(ser_u, ser_i)

ser_u = ser_u[~ser_u.isin(ser_i)]
#%%
# 8. How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
ser = pd.Series(np.random.normal(10, 5, 25)).sort_values(ascending=True).reset_index(drop=True)

     # my soln 1
n = len(ser)-1
minm = 0
q25 = np.round_(n/4, decimals=0)
med = np.round(0.5*n, decimals=0)
q75 = np.round(3*n/4, decimals=0)
maxm = n
print(len(ser))

quartiles = np.array([ser[minm], ser[q25], ser[med], ser[q75], ser[maxm]])
soln = np.percentile(ser, q=[0, 25, 50, 75, 100])

print(quartiles)
print(soln)
#%%
# 9. How to get frequency counts of unique items of a series?
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

     # my soln 1
dict_ser = {}
for i in ser:
    if i in dict_ser:
        dict_ser[i] = dict_ser[i] +1
    else:
        dict_ser[i] = 1
        
print(ser.value_counts())
#%%
# X: 10. How to keep only top 2 most frequent values as it is and replace everything else as ‘Other’?
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
ser_og = ser
ser_og = ser_og.apply(deepcopy)
# =============================================================================
#      # my soln 1
# ser_counts = ser.value_counts().sort_values(ascending=False).rename_axis("number").reset_index()
# ser_counts.rename({0:"value"}, axis=1, inplace=True)
# ser_counts['value'][1] = 'Other'
# ser_counts['value'][0] = "Other"
# =============================================================================

    # their soln
ser[~ser.isin(ser.value_counts().index[:2])] = "Other"

#####












