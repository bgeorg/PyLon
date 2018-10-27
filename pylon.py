# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 22:43:46 2017

@author: basti
"""

# Lets build a virtual planet in Python using numpy and calculate elemental
# partitioning during core formation ... R.B.Georg
# oder of elemental vector: 0-Fe, 1-Si, 2-Ni, 3-Co, 4-V, 5-Cr, 6-W
import numpy as np
import time
import matplotlib.pyplot as plt
import accretion
ComTime = time.time()


# A few variables for sensitivity analyses ... will be passed to
# calculation routine as argument var.


testL = 50

afO2A = np.linspace(1.5, 1.7, testL);   #range for starting fO2
#aP0   = np.linspace(50, 80, testL);   #range of peak pressure
#ap    = np.linspace(1, 10 , testL);
#aq    = np.linspace(1, 10 , testL);
k = 1 #np.linspace(1, 0.0001, testL);
P0 = np.linspace(55,70, testL)
p = 1#np.linspace(1,12, testL);
q = 1;
#fO2A = 1;


Mz = np.zeros([testL,testL])



for i in range (0,testL):
    
    var1 = P0[i]  
    
    for j in range(0,testL):
        
        var2 = afO2A[j]
        
        final_zmod, DOBs = accretion.f(var1, var2)
        
        #Mz(jj)= output.zmod;
        #MOc(jj) = data.wtCore(7,1000);
        #MSic(jj) = data.wtCore(2,1000);
        
        Mz[j,i]= final_zmod;
        #MOc(jj,ii) = data.wtCore(7,100);
        #MSic(jj,ii) = data.wtCore(2,100);
        
        
    
    


Y = afO2A * 0.08104 *100
X = P0
Z = Mz
#afO2A * 0.08104;
#cscale = np.linspace(0,5,11);

#print Zmatrix to screen - and/or write to csv file ... 

fig1 = plt.contourf(X, Y, Z, 25) 
plt.colorbar()
plt.xlabel('Peak Pressure P$_{0}$')
plt.ylabel('initial FeO$_{BSE}$')
#manual_loc = [(0,1),(1,2)]
#plt.clabel(fig1, inline=1, fontsize=10)
plt.show()
print(time.time()-ComTime)



