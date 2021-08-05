# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 12:53:52 2021

@author: kraft
"""

import sqlite3
import pandas as pd


conn = sqlite3.connect('Indizes.db')

data_names = ["data/DAX.csv"]

for name in data_names:
    
    df = pd.read_csv(name, encoding='utf-8')
    df.drop(columns=['Adj Close'], inplace=True)
    df.dropna(inplace=True)
    print(df.info())
    print('\nDie Daten sind von:', name)
    
    symbol = input('Geben Sie hier das Symbol ein: ')
    df['Symbol'] = symbol
    print(df.head())
    print(df.info())
    
    quest = input('Ist das Ok?\n(n/y): ')
    
    if quest == 'y':
        
        df.to_sql('indices', conn, if_exists='append', index=False)
        
    else:
        
        continue

conn.commit()
conn.close()
