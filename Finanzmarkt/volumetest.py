# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 19:41:14 2021

@author: kraft
"""
from conncurs import TheDatabaseConnection


class SimpleAnalyzer(TheDatabaseConnection):
    
    def __init__(self, username, hostname, dbname, tablename):
        
        super().__init__(username, hostname, dbname, tablename)
        
        self.volumeTest = dict()