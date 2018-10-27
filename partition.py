#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:27:30 2017

@author: bastian
"""
import numpy as np

def f(gTx, P, T, DIW):
#PART Summary of this function goes here
#   Detailed explanation goes here
    
    #MDCAL = np.zeros([6,5])
    #d = np.zeros(5)
    alpha = np.array([2.97, 0.28, 0.2, -0.46, 0.2, 1.85])
    lgs = np.zeros(6)
    gi = np.zeros(6)
    testo=np.zeros(6)

    
    gFeSi = 3;             #gamma FeSil
    gFe = gTx[0]
    gSi = gTx[1]
    gNi = gTx[2]
    gCo = gTx[3]
    gV  = gTx[4]
    gCr = gTx[5]
    gW  = gTx[6]
    
    gi[0] = gSi
    gi[1] = gNi
    gi[2] = gCo
    gi[3] = gV
    gi[4] = gCr
    gi[5] = gW
    
   
    
    lgFe =   np.log10(gFeSi / gFe)
    lgFeSi = np.log10(gSi / (gFe**2))
    lgFeNi = np.log10(gNi / (gFe))
    lgFeCo = np.log10(gCo / (gFe))
    lgFeV  = np.log10(gV  / (gFe**(3/2)))
    lgFeCr = np.log10(gCr / (gFe))
    lgFeW  = np.log10(gW  / (gFe**2))
    
    
    lgs[0] = lgFeSi;
    lgs[1] = lgFeNi;
    lgs[2] = lgFeCo;
    lgs[3] = lgFeV;
    lgs[4] = lgFeCr;
    lgs[5] = lgFeW;
    
 
        
        #MDCAL = [-21800 -25 -0.24  -1    2;
        #          2734 -90  0     -0.5  1;
        #           1892 -70  0     -0.5  1;
        #          -5764 -5  -0.063 -0.75 1.5;
        #          -3618  0   0     -0.5  1];
              
    MDCAL = np.array([[-21800, -25, -0.24, -1, 2],
                      [2734, -90, 0, -0.5, 1],
                      [1892, -70, 0, -0.5, 1],
                      [-5764, -5, -0.063, -0.75, 1.5],
                      [-3618, 0, 0, -0.5, 1],
                      [-6728, -77, -0.8, -1.5, 3]])
              
         #MDCAL2 = [-16520 0   -0.5  0.5 0;
         #          2916  -60  -1     1  0;
         #          1360  -35  -1     1  0;
         #          -5288  0   -1.5   1.5 0;
         #          -3379  0   -1     1  0];
        
              
              #d = [1/PTout.T; PTout.P/PTout.T; 2.7; DIW; lgFe];
    d = np.array([1/T, P/T, 2.75, DIW, lgFe])
              
         #    d2 = [1/PTout.T; PTout.P/PTout.T; oxyf.Feq; lgFe; 1];
              
    #Order: Si - Ni - Co - V - Cr - W          
    partition_matrix = 10**(alpha + (MDCAL.dot(d)) - lgs) #compute elemental partitioning taking regression params and interaction into account
    DSi = partition_matrix[0]
    DNi = partition_matrix[1]
    DCo = partition_matrix[2]
    DV  = partition_matrix[3]
    DCr = partition_matrix[4]
    DW  = partition_matrix[5]
        
    return [DSi, DNi, DCo, DV, DCr, DW]    
    