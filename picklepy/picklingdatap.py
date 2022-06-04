# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 00:20:58 2022

@author: AD676KL
"""

import pickle
import numpy as np

data = np.ones(100)
with open('datap.pkl', 'wb') as pickle_file:
    pickle.dump(data, pickle_file)
    
with open('datap.pkl', 'rb') as pickle_file:
    new_data = pickle.load(pickle_file)


