# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 14:06:47 2019

@author: Shiva
"""

import pandas as pd


prefix = 'rawdata/'

train_df = pd.read_csv(prefix + 'train1.csv', header=None)
train_df.head()

eval_df = pd.read_csv(prefix + 'test1.csv', header=None)
eval_df.head()


train_df = pd.DataFrame({
    'text': train_df[1].replace(r'\n', ' ', regex=True),
    'label':train_df[0]
})

print(train_df.head())

eval_df = pd.DataFrame({
    'text': eval_df[1].replace(r'\n', ' ', regex=True),
    'label':eval_df[0]
})

print(eval_df.head())