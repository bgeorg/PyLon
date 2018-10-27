#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 09:32:01 2017

@author: bastian
"""

import numpy as np

def f(ebudgets, Ocore, Fec, M):

#order wtcomp 0-Fe, 1-Si, 2-Ni, 3-Co, 4-V, 5-Cr, 6-O, 7-W 
#convert weight to molar conc in core

    wtcomp = np.zeros(8)
    fmolar = np.zeros(8)

    wtcomp[0] = Fec
    wtcomp[[1,2,3,4,5,7]] = ebudgets[:,2] / M[2]
#wtcomp(7) = metinv.Ocore;

#FeOi = 0.12;
#FeOe = 0.081;
#DFeO = FeOi - FeOe;
#FeOc = DFeO * (0.677/0.323);
#OFeO = FeOc / 4.4906;
    OSiO = 15.999*(2*(wtcomp[1]/28.086))

    wtcomp[6] = Ocore + OSiO

    s1 = np.sum(wtcomp)

    while s1 > 1:
    
        b = wtcomp[1] - 0.001
        wtcomp[1] = b
    
        OSiO = 15.999*(2*(wtcomp[1]/28.086))

        wtcomp[6] = Ocore + OSiO

        s1 = np.sum(wtcomp)

        

    emasses = np.array([55.847,
                        28.086,
                        58.693,
                        58.933,
                        50.942,
                        51.996,
                        15.999,
                        183.34])
       


    fmolar = (wtcomp /emasses) /(np.sum(wtcomp /emasses)) 


    return [fmolar, wtcomp]
