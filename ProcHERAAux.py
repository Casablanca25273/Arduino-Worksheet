# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 23:02:31 2020

@author: tankiso
"""

import pandas
import numpy as np
import matplotlib.pyplot as plt

data1 = pandas.read_csv('/home/tankiso/Documents/SARAO/ProcHeraAux.csv')
print(data1)
array = np.asarray(data1)
print(array)
freq1 = array[:,0]
lvl1 = array[:,1]
lvl2 = array[:,2]
lvl3 = array[:,3]
plt.plot(freq1,lvl1, label=1)
plt.plot(freq1,lvl2, label=2)
plt.plot(freq1,lvl3, label=3)
#plt.title("Lab RFI 125 MHz")
plt.xlabel("Frequency (MHz)")
plt.ylabel("Power Level (dBm)")
plt.legend()
#plt.savefig('lab_rfi_125MHz.png' )
plt.show()