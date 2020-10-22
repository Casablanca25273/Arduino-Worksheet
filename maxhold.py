# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 20:47:05 2020

@author: tankiso
"""

import pandas
import pylab
import numpy as np

data1 = pandas.read_csv('/home/tankiso/Documents/SARAO/2020_10_07_Hera_Node_18_maxhold_1kHz/2020_10_07_Hera_Node_18_maxhold_1kHz.csv', skiprows=76)
array = np.asarray(data1)                           #convert data1 to an array
freq = np.linspace(80, 6000, 64001, endpoint=True)  #creates evenly spaced freq sequence at the specified parameters
lvl1 = array[:,0]                                   #takes all values on the first column
print("The max power level is",max(lvl1))           #print max valu of power level
print("The index value of the max power level is",np.where(lvl1==max(lvl1)))#print index value of where the max value is
print("The corresponding max frequency is",freq[np.where(lvl1==max(lvl1))]) #print corresponding frequency value to index value    
pylab.plot(freq,lvl1,label='HERA on')               #plotting and labelling 
pylab.ylabel("Power Level (dBm)")                   #y-axis label
pylab.xlabel("Frequency (MHz)")                     #x-axis label

data2 = pandas.read_csv('/home/tankiso/Documents/SARAO/2020_10_07_Hera_Node_18_maxhold_1kHz/2020_10_07_Hera_Node_18_maxhold_1kHz_BG.csv', skiprows=76)
array1 = np.asarray(data2)
lvl2 = array1[:,0]               
pylab.plot(freq,lvl2,label='HERA off')
pylab.legend()                                      #place legend on axis
pylab.show()                                        #show the plots

lvl_diff = np.subtract(lvl2,lvl1)                   #calculating the difference between the two plots
pylab.plot(freq,lvl_diff)                           #plotting the difference plot
pylab.title("Difference")
pylab.xlabel("Frequency (MHz)")
pylab.ylabel("Power Level (dBm)")
pylab.show()

