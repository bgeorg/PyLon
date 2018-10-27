#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 09:56:06 2017

@author: bastian
"""

#Planetary Accretion model R. B. Georg, Python 3 - PlanPy

import numpy as np

import bulkcomps
import fO2m
import PT
import gamma
import partition
import metsilequi
import wttomolar
import epsilon
import interaction

#ComTime = time.time()

def f(var1, var2):
#Accretion Frame 


    fO2A = var2
    p = 1
    q = 1
    P0 = var1
    T0 = 1873
    cbe = bulkcomps.cbe
    k = 1

    n = 1000
    Ms = 0
    Me = 1
    Mt = np.linspace(Ms, Me, n+1)

    M = np.zeros((1,3))
    h = np.zeros((6,3))
    ebudgets = np.zeros((6,3))
    Dcal = np.zeros(6)
    wtCore = np.zeros([8,n])
    wtBSE = np.zeros([6,n])


    F = 0.323   #metal-silicate proportion Earth
    m = 1/n     #accretion step
    mb = m * (1-F)  #mass fraction silciate earth
    mc = m * F      #mass fraction core
    Mv = np.array([Ms, Ms*(1-F), Ms*F]) #Mass accretion vector Bulk Earth
    mv = np.array([m , mb, mc])         #reservoir fractions


    gcalc = 0   #set initial activity coeff to 0 - recalc at end of each iteration.



    u = len(Mt)  #set length of simulation
    
    #begin accretion: 
    for i in range(0, u-1):
    #print(i)
        M = Mv + mv #Mass accretion Earth
        
        Mv = M
    
    #compute fO2 evolution:
        fO2BE, fO2, Fec, DIW, Feq = fO2m.f(fO2A, p, q, M, Me) #, p, q, M, Me)
        FeOcore = (fO2BE - (1-F) * fO2) / F                                        #FeO partitioning into Core
        Ocore = FeOcore / 4.49;
    
    #Compute Pressure and Temperature Evolution
        P, T, T0T = PT.f(P0, M, T0);
    
    #compute evolution of activity coefficients
        [gT] = gamma.f(T0T, T);
    
        if (i==0):
            gTx = gT
        else:
            gTx = gcalc
    
    #compute partition coeffs
        DSi, DNi, DCo, DV, DCr, DW = partition.f(gTx, P, T, DIW)
        Dcal = np.array([DSi, DNi, DCo, DV, DCr, DW])
    
    #compute metal-silicate partitioning fluxes
        Si_BE, Si_Sil, Si_Met, Ni_BE, Ni_Sil, Ni_Met,Co_BE, Co_Sil, Co_Met,V_BE, V_Sil, V_Met,Cr_BE, Cr_Sil, Cr_Met, W_BE, W_Sil, W_Met = metsilequi.f(Dcal, cbe, F, mb, mc, m, k);
    
        eflux = np.array([[Si_BE, Si_Sil, Si_Met],
                          [Ni_BE, Ni_Sil, Ni_Met],
                          [Co_BE, Co_Sil, Co_Met],
                          [V_BE,   V_Sil,  V_Met],
                          [Cr_BE, Cr_Sil, Cr_Met],
                          [W_BE,   W_Sil,  W_Met]]) #elfux = np.array(eflux)
    
        ebudgets = h + eflux;
        h = ebudgets;

        fmolar, wtcomp = wttomolar.f(ebudgets, Ocore, Fec, M)
    
        wtCore[:,i] = wtcomp
        wtBSE[:,i]  = ebudgets[:,1] / M[1]
    #DObs[:,i] = wtCore[[1,2,3,4,5,7]] / wtBSE
    
        #compute epsilon interaction parameters
        eTeM, eTeSi  = epsilon.f(T0T)
    
        #compute interaction of solutes in solvent
        gcalc = interaction.f(gT, eTeM, eTeSi, fmolar)
    
    
    
    #gcalc = gT    
    DObs = wtCore[[1,2,3,4,5,7]] / wtBSE    
             
    import zscoremod

    zs, zmod = zscoremod.f(DObs)
    final_zmod = zmod[-1]

    return final_zmod, DObs
#print(time.time()-ComTime)