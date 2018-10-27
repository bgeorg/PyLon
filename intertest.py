# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 21:06:47 2017

@author: basti
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 13:09:03 2017

@author: bastian
"""
import numpy as np

#def f(gT, eTeM, eTeSi, fmolar):
#GSOLVENT Summary of this function goes here
#   Detailed explanation goes here
    
fmolar = np.array([0.772092948686305,
                   0.0438985186732777,
                   0.0446235968484070,
                   0.00213883520707417,
                   0.000135665427992814,
                   0.00819973542180840,
                   0.128910568648118,
                   1.31087017009571e-07])
    
    
eTeM = np.array([0,
                 4.19685817768262,
                 0.0585608117816179,
                 0.575847982519243,
                 3.21108451269205,
                 0,
                 -0.488006764846816,
                 0])
    
eTeSi = np.array([0,
                  4.19685817768262,
                  3.66005073635112,
                  2.24483111829535,
                  0.976013529693632,
                  0.244003382423408,
                  -2.44003382423408,
                  8.93052379669673])
    
gT = np.array([1.00870763566421,
               0.103827717238345,
               0.980913701274428,
               0.834559316312387,
               0.307387368234395,
               0.898063232123363,
               0.823750017254329,
               1.50617315729696])

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
 #   return gcalc


