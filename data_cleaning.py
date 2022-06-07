# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 10:18:45 2022

@author: sebgi
"""

import pandas as pd

df = pd.read_csv('datasets/QVI_purchase_behaviour.csv')

df.info()

df.nunique()

