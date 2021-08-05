# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 17:56:01 2021

@author: kraft
"""

import pandas as pd
from station import PointAndFigure as pf


dax_obj = pf('DAX')
data_points = {'Points': dax_obj.points, 'Release_Points': dax_obj.release_points}
data_rever = {'Reversales': dax_obj.reversales, 'Rever_Dates': dax_obj.rever_dates}

df_points = pd.DataFrame(data=data_points, columns=['Points', 'Release_Points'])
df_rever = pd.DataFrame(data=data_rever, columns=['Reversales', 'Rever_Dates'])

df_points.info()
df_rever.info()
