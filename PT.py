#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:01:35 2017

@author: bastian
"""

def f(P0, M, T0):
    ## calcualte Temperature and Pressure for equilibration
    P = P0 * ((M[0])**(2/3))    #increasing Pressure of Accretion
    #T = 28.57 * P + 1973;       %Temperature Geotherm - Wade and Wood - use Badro later on!
    T = 0.5 * (2022 + 54.21*P - 0.34*(P**2) + 9.0747E-4*(P**3) + (1940*((P/29) +1)**(1/1.9)));
    T0T = T0 / T;

       
    return [P, T, T0T]