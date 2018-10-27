#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 12:26:22 2017

@author: bastian
"""
import numpy as np

def f(T0T):
#function to scale activity coef to T
    eM = np.zeros(8)
    eSi = np.zeros(8)
#interaction parameter matrix, order is
# Fe - Si - Ni - Co - V - Cr - O - W

#e = [0	 0	  0	   0	   0	 0    0;
#     0	 8.6  7.5  4.6    2.0    0.5  -5;
#     0	 0	  0.12 0	   0	 0    0;
#     0	 0	  0	   1.18    0	 0    0;
#     0	 0	  0	   0	   6.58	 0    0;
#     0	 0	  0	   0	   0     0    0;
#     0   0    0    0       0     0    -1];
 
 
    e = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 8.6, 7.5,    4.6,   2.0,  0.5,  -5,  18.3],
                  [0	, 0,  0.12,   0,	    0,	 0,    0,    0],
                  [0	, 0,	  0,	  1.18,  0,	 0,    0,    0],
                  [0	, 0,	  0,	  0,	    6.58, 0,    0,    0],
                  [0	, 0,	  0,	  0,	    0,    0,    0,    0],
                  [0, 0,   0,  0,    0,    0,    -1,   0],
                  [0, 0, 0,   0,   0,   0,   0,    0]])
 
 
 #Badro's epsilon
# e = [0	 0	  0	   0	   0	 0   0;
#      0	 12.41  1.16  0    2    0.5 -5;
#      0	 0	  0.12 0	   0	 0   0;
#      0	 0	  0	   1.18    0	 0   0;
#      0	 0	  0	   0	   6.48	 0   0;
#      0	 0	  0	   0	   0     0   0;
#      0  0    0    0       0     0  -1];
 
 
 
    eM = np.diagonal(e)
    eSi = e[1,:].T
 
    eTeM = (T0T*(eM));
    eTeSi =(T0T*(eSi));
 
    return [eTeM, eTeSi]

