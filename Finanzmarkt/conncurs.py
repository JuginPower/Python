# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 23:09:36 2021

@author: kraft
"""
import pymysql
import pandas as pd
from funcs import MoreFuncs


class TheDatabaseConnection(MoreFuncs):
    
    def __init__(self, username, hostname, dbname, tablename):
        
        self.username = username
        self.hostname = hostname
        self.dbname = dbname
        self.tablename = tablename
        
    def to_update_indices(self, name, form=".csv"):
        
        """update the database with the data in datafolder.\nNeeds name."""
        
        conn = pymysql.connect(user=self.username, host=self.hostname, database=self.dbname)
        cursor = conn.cursor()
        sql = f"INSERT INTO {self.tablename}(Date, Open, High, Low, Close, Volume) VALUES (%s, %s, %s, %s, %s, %s)"
        
        path = f"data/{name}{form}"
        df = pd.read_csv(path)
        df.dropna(inplace=True)
        dictionary = df.to_dict(orient="list")
        
        val = self.tuple_maker_indices(dictionary)
        cursor.executemany(sql, val)
        conn.commit()
        conn.close()
    
    def select_indices(self, direction):
        
        prompt = ""
        
        if direction == "a":
            
            prompt = "ASC"
            
        elif direction == "d":
            
            prompt = "DESC"
        
        conn = pymysql.connect(user=self.username, host=self.hostname, database=self.dbname)
        cursor = conn.cursor()
        sql = f"SELECT * FROM {self.tablename} ORDER BY Date {prompt}"
        
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        
        return result
        
        