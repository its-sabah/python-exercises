# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 00:20:58 2022

@author: AD676KL
"""

import pickle
import numpy as np
import pandas as pd


data = pd.read_csv(r"C:\Users\AD676KL\OneDrive - EY\__Learning\_python\picklepy\dummy.csv")
print(data)
print(type(data['col2'][3]))

with open('df_t.pkl', 'wb') as pickle_file:
    pickle.dump(data, pickle_file)
    
with open('df_t.pkl', 'rb') as pickle_file:
    new_data = pickle.load(pickle_file)

print(new_data)
print(data['col2'][3])
