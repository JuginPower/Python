# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:06:04 2021

@author: kraft
"""

from PyPDF2 import PdfFileMerger


pdfs = ["1.pdf", "2.pdf"]

merger = PdfFileMerger()

for pdf in pdfs:
    
    merger.append(pdf)
    
name = input('Name: ')

merger.write(f'C:/Users/kraft/Desktop/{name}.pdf')

merger.close()
print('Finish!')
