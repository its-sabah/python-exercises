# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 00:20:58 2022

@author: AD676KL
"""

import pickle
import numpy as np
import pandas as pd

path = "https://github.com/its-sabah/python-exercises/blob/27eee77ded1f220cf1c3c01d6a0c0eabdd4be0ef/picklepy/dummy.csv"
data = pd.read_csv(path, index_col=0)

print(data)
print(type(data['col2'][3]))

with open('pickled_dummy.pkl', 'wb') as pickle_file:
    pickle.dump(data, pickle_file)
    
with open('pickled_dummy.pkl', 'rb') as pickle_file:
    new_data = pickle.load(pickle_file)

print(new_data)
print(data['col2'][3])
