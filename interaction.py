#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 13:09:03 2017

@author: bastian
"""
import numpy as np

def f(gT, eTeM, eTeSi, fmolar):
#GSOLVENT Summary of this function goes here
#   Detailed explanation goes here
 

    i=1
    gcalc = np.zeros(8)
    A = np.zeros(8)
    B = np.zeros(8)
    C = np.zeros(8)
    Aa = np.zeros(8) 
    Bb = np.zeros(8)
    Cc = np.zeros(8)

    A = eTeM * (fmolar + np.log(1-fmolar))

    sumA = np.sum(A[[1, 2, 3, 4, 5, 6, 7]])

    for j in range (2,8):

        B[j] =  eTeSi[j] * fmolar[i] * fmolar[j] * (1-(1/(1-fmolar[i])) - (1/(1-fmolar[j])));

        C[j] = (eTeSi[j]/2) * (fmolar[i]**2) * (fmolar[j]**2) * ((3/(1-fmolar[i])) + (3/(1-fmolar[j])) + (fmolar[i]/(1-fmolar[i])) + (fmolar[j]/(1-fmolar[j])**2) -3  );

            

    sumB = sum(B)
    sumC = sum(C)

    gcalc[0] = np.exp(sumA + sumB - sumC)

    for q in range (1,8):
    
    
        Aa[q] = np.log(gcalc[0]) + np.log(gT[q]) - eTeM[q]*np.log(1-fmolar[q])

    
        if (q == 1):
    

            Bb[q] = eTeSi[2] * fmolar[2] * (1+(np.log(1-fmolar[2]) / fmolar[2]) - (1/(1-fmolar[1])))
            Cc[q] = eTeSi[2] * (fmolar[2]**2) * fmolar[1] * ( (1/(1-fmolar[1])) + (1/(1-fmolar[2])) + (fmolar[1]/(2*(1-fmolar[1])**2)) -1)

        else:
        
            Bb[q] = eTeSi[q] * fmolar[i] * (1+(np.log(1-fmolar[i]) / fmolar[i]) - (1/(1-fmolar[q])));
            Cc[q] = eTeSi[q] * (fmolar[i]**2) * fmolar[q] * ( (1/(1-fmolar[q])) + (1/(1-fmolar[i])) + (fmolar[q]/(2*(1-fmolar[q])**2)) -1)
     



    sums = np.exp(Aa - Bb + Cc)

    gcalc[[1, 2, 3, 4, 5, 6, 7]] = sums[[1, 2, 3, 4, 5, 6, 7]]
    gcalc[0] = np.exp(sumA + sumB - sumC)
    return gcalc


