#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 15:20:13 2017

@author: bastian
"""


import numpy as np


#order of cbe - note Python 0-indexing: 0-Si, 1-Ni, 2-Co, 3-V, 4-Cr, 5-W 
def f(Dcal, cbe, F, mb, mc, m, k):
        
    DSE = 50000
    #eflux = np.zeros([6,3])

    j = 0 #Si 
    Si_BE = cbe[j] * m
    Si_Sil = ((cbe[j] / (1-F)) * mb) - ((Dcal[j] * cbe[j]) / (F*Dcal[j] + (1-F)) * (k * mc))
    Si_Met = (Dcal[j] * cbe[j]) / (F*Dcal[j] + (1-F)) * (mc * k) #calc conc on Metal
    
    j = 1 #Ni
    Ni_BE = cbe[j] * m                
    Ni_Sil = (DSE*cbe[j] / (F*DSE + (1-F)) * (1/Dcal[j]) * mb)*k
    Ni_Met = (DSE*cbe[j] / (F*DSE + (1-F)) * mc) - Ni_Sil #calc conc on Metal
       
     
    j=2 #Co    
    Co_BE = cbe[j] * m                
    Co_Sil = (DSE*cbe[j] / (F*DSE + (1-F)) * (1/Dcal[j]) * mb)*k;
    Co_Met = (DSE*cbe[j] / (F*DSE + (1-F)) * mc) - Co_Sil #calc conc on Metal 
    
    j=3 #V                  
    V_BE = cbe[j] * m
    V_Sil = ((cbe[j] / (1-F)) * mb) - ((Dcal[j] * cbe[j]) / (F*Dcal[j] + (1-F)) * (k * mc));
    V_Met = (Dcal[j] * cbe[j]) / (F*Dcal[j] + (1-F)) * (mc * k); #calc conc on Metal
       
    j=4 #Cr    
    Cr_BE = cbe[j] * m
    Cr_Sil = ((cbe[j] / (1-F)) * mb) - ((Dcal[j] * cbe[j]) / (F*Dcal[j] + (1-F)) * (k * mc));
    Cr_Met = (Dcal[j] * cbe[j]) / (F*Dcal[j] + (1-F)) * (mc * k); #calc conc on Metal    
       
    j=5 #W                 
    W_BE = cbe[j] * m                
    W_Sil = (DSE*cbe[j] / (F*DSE + (1-F)) * (1/Dcal[j]) * mb)*k;
    W_Met = (DSE*cbe[j] / (F*DSE + (1-F)) * mc) - W_Sil; #calc conc on Metal       
    
#    eflux = np.array([[Si_BE, Si_Sil, Si_Met],
#                     [Ni_BE, Ni_Sil, Ni_Met],
#                     [Co_BE, Co_Sil, Co_Met],
#                     [V_BE,   V_Sil,  V_Met],
#                     [Cr_BE, Cr_Sil, Cr_Met],
#                     [W_BE,   W_Sil,  W_Met]])     
    
    return [Si_BE, Si_Sil, Si_Met, Ni_BE, Ni_Sil, Ni_Met,Co_BE, Co_Sil, Co_Met,V_BE, V_Sil, V_Met,Cr_BE, Cr_Sil, Cr_Met, W_BE, W_Sil, W_Met]