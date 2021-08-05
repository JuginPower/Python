# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:32:52 2021

@author: kraft
"""
import pymysql
from conncurs import TheDatabaseConnection


class PivotMaker(TheDatabaseConnection):
    
    def __init__(self, username, hostname, dbname, tablename):
        
        super().__init__(username, hostname, dbname, tablename)
        
        self.current_hits = dict(s3=dict(Date=[], Total=[], MoveP=[], Volume=[]), 
                                 s2=dict(Date=[], Total=[], MoveP=[], Volume=[]), 
                                 s1=dict(Date=[], Total=[], MoveP=[], Volume=[]), 
                                 r3=dict(Date=[], Total=[], MoveP=[], Volume=[]), 
                                 r2=dict(Date=[], Total=[], MoveP=[], Volume=[]), 
                                 r1=dict(Date=[], Total=[], MoveP=[], Volume=[]), 
                                 pivot=dict(Date=[], Total=[], MoveP=[], Volume=[]))
        
        self.pre_volume = dict(s3=dict(PreDate=[], Volume=[]), 
                               s2=dict(PreDate=[], Volume=[]), 
                               s1=dict(PreDate=[], Volume=[]), 
                               r3=dict(PreDate=[], Volume=[]), 
                               r2=dict(PreDate=[], Volume=[]), 
                               r1=dict(PreDate=[], Volume=[]), 
                               pivot=dict(PreDate=[], Volume=[]))
        
    def select_indices(self):
        
        """Select any data in the database."""
        
        conn = pymysql.connect(user=self.username, host=self.hostname, database=self.dbname)
        cursor = conn.cursor()
        sql = f"SELECT Date, Open, High, Low, Close, Volume FROM {self.tablename} ORDER BY Date ASC"
        cursor.execute(sql)
        result = cursor.fetchall()
        
        conn.commit()
        conn.close()
        
        return result
    
    def select_indices_year(self, year):
        
        """Select Data per year as integer."""
        
        conn = pymysql.connect(user=self.username, host=self.hostname, database=self.dbname)
        cursor = conn.cursor()
        sql = f"SELECT Date, Open, High, Low, Close, Volume FROM {self.tablename} WHERE Date BETWEEN '{year-1}-12-31' AND '{year+1}-01-01' ORDER BY Date ASC"
        cursor.execute(sql)
        result = cursor.fetchall()
        
        conn.commit()
        conn.close()
        
        return result
    
    def collecter(self, datas):
        
        """Insert Data for Full Analyze!"""
        
        self.current_hits["pivot"]["Total"] = self.analyzer(datas, "pivot")
        self.current_hits["r1"]["Total"] = self.analyzer(datas, "r1")
        self.current_hits["r2"]["Total"] = self.analyzer(datas, "r2")
        self.current_hits["r3"]["Total"] = self.analyzer(datas, "r3")
        self.current_hits["s1"]["Total"] = self.analyzer(datas, "s1")
        self.current_hits["s2"]["Total"] = self.analyzer(datas, "s2")
        self.current_hits["s3"]["Total"] = self.analyzer(datas, "s3")
    
    def pivoter(self, high, low, close):
        
        """Make a dictionary of pivots."""
        
        pivot = (high+low+close)/3
        r1 = 2*pivot-low
        r2 = pivot+(high-low)
        r3 = r1+(high-low)
        s1 = 2*pivot-high
        s2 = pivot-(high-low)
        s3 = s1-(high-low)
        
        pivot_container = {"pivot": pivot, "r1": r1, "r2": r2, "r3": r3, 
                           "s1": s1,"s2": s2, "s3": s3}
        
        return pivot_container
        
    def analyzer(self, datas, piv):
        
        datas = list(datas)
        counter = 0
        
        while datas:
            
            try:
                
                current_day = datas.pop(0)
                pivots = self.pivoter(current_day[2], current_day[3], 
                                      current_day[4])
                current_day = list(current_day)
                pre_volume = current_day.pop()
                future_day = datas.pop(0)
                future_day = list(future_day)
                f_date = future_day.pop(0)
                c_date = current_day.pop(0)
                current_volume = future_day.pop()
                 
            except IndexError:
                
                break
            
            else:
                
                hit = self.counter(pivots[f"{piv}"], future_day, piv)
                
                if hit > 0:
                    
                    moveP = future_day[1] - future_day[2]
                    self.current_hits[f"{piv}"]["MoveP"].append(abs(moveP))
                    self.current_hits[f"{piv}"]["Date"].append(str(f_date))
                    self.current_hits[f"{piv}"]["Volume"].append(current_volume)
                    self.pre_volume[f"{piv}"]["PreDate"].append(str(c_date))
                    self.pre_volume[f"{piv}"]["Volume"].append(pre_volume)
                
                counter += hit
            
        return counter
    
    def counter(self, pivot, f_day, name):
        
        count = 0
        
        if f_day[0] < pivot:
            
            for num in f_day[1:]:
                
                if num >= pivot:
                    
                    count += 1
                    
        elif f_day[0] > pivot:
            
            for num in f_day[1:]:
                
                if num <= pivot:
                    
                    count += 1
               
                    
        return count
    
    