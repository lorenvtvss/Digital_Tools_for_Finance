# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:23:53 2022

@author: Jonas.Neller
"""

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

df.to_feather("Data_frame_ftr")

#feather.write_feather("Data_frame.arrow")

df.to_hdf("Data_frame.h5", key="fx/spot")
df.to_pickle("Data_frame.pkl")


df.to_csv("abc.csv")