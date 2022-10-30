# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:23:53 2022

@author: Jonas.Neller
"""

from time import time
import pandas as pd
import numpy as np
import os
import pyarrow.feather as feather
import h5py

df = pd.DataFrame(np.random.normal(size=(1000000 , 3)),
                 columns=["1", "2", "3" ],
                 dtype=np.float32)
df['Twin1']='1'
df['Twin2']='1'

# to csv
df.to_csv("abc.csv")

# # to hdf
%time df.to_hdf("Data_frame.h5", key="fx/spot")

# to pickle
%time df.to_pickle("Data_frame.pkl")

# to feather
%time feather.write_feather(df, "Data_frame.arrow")

#Imported times to txt file via command line 
#cd ..\GitHub\Digital-Tools-for-Finance\Homeworks\Week5
#python Data_frame.py > file.txt