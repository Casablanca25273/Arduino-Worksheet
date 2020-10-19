# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 20:47:05 2020

@author: tankiso
"""

import pandas
import pylab
import numpy as np

data1 = pandas.read_csv('/home/tankiso/Documents/SARAO/2020_10_07_Hera_Node_18_maxhold_1kHz/2020_10_07_Hera_Node_18_maxhold_1kHz.csv', skiprows=76)
#print(data1)
array = np.asarray(data1)
#print(array)
freq1 = array[:,0]/1000000.00 
freq1 = np.linspace(80, 6000, 64001, endpoint=True)
lvl1 = array[:,:]               
#plt.xlim(80,6000)
pylab.plot(freq1,lvl1)
pylab.ylabel("Power Level (dBm)")
pylab.xlabel("Frequency (MHz)")


data2 = pandas.read_csv('/home/tankiso/Documents/SARAO/2020_10_07_Hera_Node_18_maxhold_1kHz/2020_10_07_Hera_Node_18_maxhold_1kHz_BG.csv', skiprows=76)
#print(data2)
array1 = np.asarray(data2)
#print(array1)
freq2 = array1[:,0]/1000000.00 
freq2 = np.linspace(80, 6000, 64001, endpoint=True)
lvl2 = array1[:,:]               
#plt.xlim(80,6000)
pylab.plot(freq2,lvl2)
#pylab.ylabel("Power Level (dBm)")
#pylab.xlabel("Frequency (MHz)")
pylab.legend()
pylab.show()

lvl_diff = np.subtract(lvl2,lvl1)
freq2 = np.linspace(80, 6000, 64001, endpoint=True)
pylab.plot(freq1,lvl_diff)
pylab.title("Difference")
pylab.xlabel("Frequency (MHz)")
pylab.ylabel("Power Level (dBm)")
pylab.show()