# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 23:02:31 2020

@author: tankiso
"""

import pandas
import numpy as np
import matplotlib.pyplot as plt

procHera = pandas.read_csv('/home/tankiso/Documents/SARAO/ProcHeraAux.csv')
array = np.asarray(procHera)                        #convert procHera to an array
freq1 = array[:,0]                                  #takes all values on the first column
PowtoEfield = array[:,1] 
data1 = pandas.read_csv('/home/tankiso/Documents/SARAO/2020_10_07_Hera_Node_18_maxhold_1kHz/2020_10_07_Hera_Node_18_maxhold_1kHz.csv', skiprows=76)
array1 = np.asarray(data1)                          #convert data1 to an array
freq = np.linspace(80, 6000, 64001, endpoint=True)  #creates evenly spaced freq sequence at the specified parameters
lvl1 = array1[:,0] 

plt.plot(freq1,PowtoEfield)
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power (dB)")
plt.title("Power to E-field")
plt.savefig('powtoefield.jpeg')
plt.show()
 
data2 = pandas.read_csv('/home/tankiso/Documents/SARAO/2020_10_07_Hera_Node_18_maxhold_1kHz/2020_10_07_Hera_Node_18_maxhold_1kHz_BG.csv', skiprows=76)
array1 = np.asarray(data2)
lvl2 = array1[:,0]               

E_Spec = array[:,2]                                 #takes all values on third column
E_Cont = array[:,3] 

print("The E-Field strength at 1 m of the maximum emission is", max(lvl1+PowtoEfield))#print the sum

plt.plot(freq1,lvl1+PowtoEfield,label='HERA')
plt.plot(freq1,lvl2+PowtoEfield, label='Background', color='black')
plt.plot(freq1,E_Spec,color='r',label='E_Spec')
plt.plot(freq1,E_Cont,color='orange', label='E_Cont') 
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power (dBuV/m)")
plt.title("E-Field")
plt.legend()
plt.savefig('E-Field.jpeg')
plt.show()


lvl_diff = np.subtract((lvl1+PowtoEfield),E_Spec)               #calculate difference between the specified paramenters
print("The max diff between E_spec and HERA is", max(lvl_diff))#print the max difference 
plt.plot(freq1,lvl_diff, label='Diff') 
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power (dBuV/m)")
plt.title("Shielding")
plt.savefig('shield.jpeg')
plt.show()
