# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 22:29:20 2021

@author: kraft
"""
import sqlite3
import pandas as pd
from math import floor, ceil


class PointAndFigure:
    
    def __init__(self, table_name, boxsize=200):
        
        """Optional Boxgröße angeben.\nDefault: 200"""
        
        self.table_name = table_name
        self.boxsize = boxsize
        self.fail = 'Irgendwas ist schief gelaufen, wiederholen Sie die Eingabe.'
        self.points = []
        self.release_points = []
        self.reversales = []
        self.rever_dates = []
        
        self.values = self.get_values()
        self.starter()
        
    def get_values(self, colum_name='Close'):
        
        sql = f"SELECT {colum_name} FROM indices WHERE Symbol='{self.table_name}'"
        
        conn = sqlite3.connect('Indizes.db')
        df = pd.read_sql(sql, conn)
        values = [x for x in df[colum_name]]
        
        return values
        
    def get_reversale_date(self, value, column_names='Close, Date'):
        
        sql = f"SELECT {column_names} FROM indices WHERE Symbol='{self.table_name}'"
        
        conn = sqlite3.connect('Indizes.db')
        df = pd.read_sql(sql, conn)
        
        for row in df.index:
            
            if df.loc[row, 'Close'] == value:
                
                x = row
                self.rever_dates.append(df.loc[x, 'Date'])
                break
        
    def floor_ceil(self, one_point):
        
        """floors if upper 0\nceil if under 0"""
        
        point = 0
        
        if one_point > 0:
                
            point = floor(one_point)
            
        elif one_point < 0:
            
            point = ceil(one_point)
            
        return point
        
    def starter(self):
        
        """Starts the algorithm."""

        release_point = self.values.pop(0)
        release_point = release_point//self.boxsize*self.boxsize
        
        while True:
            
            second_point = self.values.pop(0)
            point = (release_point/self.boxsize) - (second_point/self.boxsize)
            
            orig_point = self.floor_ceil(point)
                
            if orig_point >= 3:
                
                release_point = second_point//self.boxsize*self.boxsize+self.boxsize
                self.get_reversale_date(second_point)
                self.points.append(orig_point*-1)
                self.release_points.append(release_point)
                self.reversales.append('down')
                break
                
            if orig_point <= -3:
                
                release_point = second_point//self.boxsize*self.boxsize
                self.get_reversale_date(second_point)
                self.points.append(abs(orig_point))
                self.release_points.append(release_point)
                self.reversales.append('up')
                break
            
        if self.reversales[-1] == 'up':
            
            self.trend_up()
            
        elif self.reversales[-1] == 'down':
            
            self.trend_down()
                
    def trend_up(self):
        
        """Follows the upper trend till reversale."""
        
        release_point = self.release_points[-1]
        
        while True:
            
            try:
            
                second_point = self.values.pop(0)
                
            except IndexError:
                
                break
            
            else:
                
                point = (release_point/self.boxsize)-(second_point/self.boxsize)
            
                orig_point = self.floor_ceil(point)
                
                if orig_point >= 3:
                    
                    release_point = second_point//self.boxsize*self.boxsize+self.boxsize
                    self.get_reversale_date(second_point)
                    self.points.append(orig_point*-1)
                    self.release_points.append(release_point)
                    self.reversales.append('down')
                    self.trend_down()
                    break
                    
                elif orig_point <= -1:
                    
                    release_point = second_point//self.boxsize*self.boxsize
                    
                    self.release_points.append(release_point)
                    self.points.append(abs(orig_point))
            
    def trend_down(self):
        
        """Follows the down trend till reversale."""
        
        release_point = self.release_points[-1]
        
        while True:
             
            try:
                
                second_point = self.values.pop(0)
                
            except IndexError:
                
                break
            
            else: 
                
                point = (release_point/self.boxsize) - (second_point/self.boxsize)
                
                orig_point = self.floor_ceil(point)
                
                if orig_point <= -3:
                    
                    release_point = second_point//self.boxsize*self.boxsize
                    self.get_reversale_date(second_point)
                    self.points.append(abs(orig_point))
                    self.release_points.append(release_point)
                    self.reversales.append('up')
                    self.trend_up()
                    break
                    
                elif orig_point >= 1:
                    
                    release_point = second_point//self.boxsize*self.boxsize+self.boxsize
                    
                    self.release_points.append(release_point)
                    self.points.append(orig_point*-1)
            
# Try muss über while oder nur bei second_point