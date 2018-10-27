#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:11:32 2017

@author: bastian
"""

import numpy as np
#apply temperature extrapolation on activity coefs
def f(T0T, T):

    gT = np.zeros(8);


      
#gamma_0 values temperature scaled: 
#order Fe-Si-Ni-Co-V-Cr-O-W


  
    gT[0] = np.exp(T0T*np.log(0.8762))
    gT[1] = np.exp(T0T*np.log(0.0045))
    gT[2] = np.exp(T0T*np.log(0.66))
    gT[3] = np.exp(T0T*np.log(0.55))
    gT[4] = np.exp(T0T*np.log(0.08))
    gT[5] = np.exp(T0T*np.log(0.7705))
    gT[6] = np.exp(4.29-16500/T)
    gT[7] = np.exp(T0T*np.log(1))
    
    return [gT]