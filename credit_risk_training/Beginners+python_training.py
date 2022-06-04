3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 19:23:27 2022

@author: AD676KL
"""
#%%
#   Task 1: importing files / libraries / functions 

import numpy as np
import pandas as pd
from datetime import timedelta
#%%
#   Task 3: basic column operations 

# 1. col names
aapl_df = pd.read_csv(r"C:\Users\AD676KL\Downloads\Python Training\AAPL.csv")
ibm_df = pd.read_csv(r"C:\Users\AD676KL\Downloads\Python Training\IBM.csv")
print(aapl_df.head(2))
col_lst = list(aapl_df.columns.values)
col_lst = [col for col in col_lst if col not in ('High', 'Low')]
aapl_df = aapl_df[col_lst]
aapl_df = aapl_df.drop(aapl_df.columns[1], axis=1)
aapl_df = aapl_df[aapl_df.columns[:3]]

aapl_df.rename({"Adj Close": "Adj Close",
           "apple": "apple",
           "Close": "Close"})
print(aapl_df.head(3))
aapl_df.rename({"Date":"AAPL"}, axis='columns', inplace=True)
aapl_df.rename({"AAPL": "apple"}, axis='columns', inplace=True)
#print(df.head(2))
#%%

#   Task 4: merging data and processing missing values
df['apple'] = pd.to_datetime(df['apple'], format='%Y-%m-%d')

missing_val_count = [1 for x in df['apple'] if x == np.NaN]
print(sum(missing_val_count))

#%%

#   Task 5: data rearrangement / change type and calculations
df_ascending = df.sort_values('Adj Close')
df_descending = df.sort_values('Adj Close', ascending=False)

df['Adj Close'] = [float(x) for x in df['Adj Close']]
print(type(df['Adj Close'][2]))
df['Adj Close'] = [str(x) for x in df['Adj Close']]
print(type(df['Adj Close'][2]))

#%%

#   Task 6: shifting data and create lags / returns 
print(df.head(10))
df["AAPL+10d"] = df["AAPL"] + timedelta(days=10)
df2 = df[['Adj Close', 'AAPL+10d']]
print(df2.head(10))

df.drop("AAPL+10d", axis=1, inplace=True)
df3 = pd.merge(left=df, right=df2, how='left', left_on="AAPL", right_on="AAPL+10d") # something going wrong here
df3.sort_values('AAPL', inplace=True)
print(df)

df3['AAPL+5d'] = df3["AAPL+10d"] - timedelta(days=5)

#%%

#   Task 6: date operation
df.sort_values('AAPL', inplace=True)
df_dates = df[(df['AAPL'] > '2011-05-03 00:00:00') & (df['AAPL'] < '2012-05-03 00:00:00')]
print(type(df["AAPL"][4]))

#%%

#   Task 7: basic matrix operation

m=df.to_numpy()
#print(len(m[1,]))
df_m=pd.DataFrame(m, columns=('Col1', 'Col2', 'Col3'))

m=m[:,:2]*2
mt = m.transpose()

m0 = np.zeros((5,5))
m1 = np.ones((15,5))
#print(m1)

sq_m = [[1,2,3],[4,6,7],[17,19,23]]
sq_inv = np.linalg.inv(sq_m)
sq_dt = np.linalg.det(sq_m)
sq_eval,sq_evect = np.linalg.eig(sq_m)

print(sq_inv, sq_dt, sq_eval, sq_evect)