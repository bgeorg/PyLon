# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 22:03:20 2017

@author: basti
"""

import numpy as np

def f(DObs):
#ZSCORE Summary of this function goes here
#   Detailed explanation goes here



 u = np.shape(DObs)
 w = u[1]
 zs = np.zeros([6,w])
 zmod = np.zeros(w)

 for k in range (0,w):


    zs[0,k]  =  ((DObs[0,k] - 0.225) / 0.125)
    zs[1,k]  =  ((DObs[1,k] - 26) / 2)
    zs[2,k]  =  ((DObs[2,k] - 24.5) / 1.5)
    zs[3,k]  =  ((DObs[3,k] - 1.9) / 0.6)
    zs[4,k]  =  ((DObs[4,k] - 3) / 1)     
    zs[5,k]  =  ((DObs[5,k] - 20) / 10)
   
    zmod[k] = np.sqrt(( (zs[1,k]**2) + (zs[2,k]**2) + (zs[3,k]**2) + (zs[4,k]**2) + (zs[5,k]**2)) / 5); 

 return [zs, zmod]