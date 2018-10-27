#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 10:58:16 2017

@author: bastian
"""

#This code computes the oxygen fugacity in BSE and as DIW
import numpy as np

print(1)

#def fO2m(fO2A, p, q, M, Me):
def f(fO2A, p, q, M, Me): #, p, q, M, Me):   
    ## Compute oxygen fugacity in BSE ##
    
   fO2i = fO2A * 0.08104;                  # fO2i Starting FeO content in silicate.
   fO2BE = fO2i * (1-0.323)                #FeO in Bulk Earth
   F = 0.323

   fO2 = (fO2A + (1-fO2A) * ((M[0] / Me)**(p/q)))*0.08104           #fO2 gradient function
   Fec = (F - (1-F) * (fO2 / 1.2864)) / F                                   #Fe weight content Core
   DIW = 2 * np.log10((fO2) / Fec)                                          #fO2 as DIW
   Feq = np.log10((fO2) / Fec)                                              #fO2 as DIW
   
   return [fO2BE, fO2, Fec, DIW, Feq] 



#[DIW, Fec, fO2, Feq]
    


