# -*- coding: utf-8 -*-
"""
Created on Fri Aug 05 16:31:12 2016

@author: fangren
"""

import numpy as np
import matplotlib.pyplot as plt

path = '..\\..\\data\\Masterfiles\\'
save_path = '..\\..\\figures\\'

basename1 = 'Sample1_master_metadata.csv'
basename2 = 'Sample3_master_metadata.csv'
basename3 = 'Sample16_master_metadata.csv'

filename1 = path + basename1
filename2 = path + basename2
filename3 = path + basename3

data1 = np.genfromtxt(filename1, delimiter=',', skip_header = 1)
data2 = np.genfromtxt(filename2, delimiter=',', skip_header = 1)
data3 = np.genfromtxt(filename3, delimiter=',', skip_header = 1)

data = data1[:, :69]
ROI = data[:, 15]
data = data[ROI > 20000]

Co = data[:,61]*100
Fe = data[:,62]*100
Zr = data[:,63]*100
scan_num = data[:,48]


scan_chosen = []
indices = []

for i in range(len(scan_num)):
    #print float(Co[i])/float(Fe[i])
    if np.abs(float(Co[i])/float(Fe[i])- 1.5) < 0.1:
        if np.abs(Zr[i]-10) < 0.5 or np.abs(Zr[i]-30) < 1 or np.abs(Zr[i]-50) < 1 or np.abs(Zr[i]-70) < 0.7 or np.abs(Zr[i]-85) < 1:
            scan_chosen.append(scan_num[i])
            indices.append(i)

print scan_chosen
print Co[indices]
print Fe[indices]
print Zr[indices]

path = '..\\..\\data\\Detailed_analysis\\'
save_path = '..\\..\\figures\\'

Zr_10_f = path + 'Zr = 10.csv'
Zr_30_f = path + 'Zr = 30.csv'
Zr_50_f = path + 'Zr = 50.csv'
Zr_70_f = path + 'Zr = 70.csv'
Zr_85_f = path + 'Zr = 85.csv'

Zr_10 = np.genfromtxt(Zr_10_f, delimiter= ',')
Zr_30 = np.genfromtxt(Zr_30_f, delimiter= ',')
Zr_50 = np.genfromtxt(Zr_50_f, delimiter= ',')
Zr_70 = np.genfromtxt(Zr_70_f, delimiter= ',')
Zr_85 = np.genfromtxt(Zr_85_f, delimiter= ',')

plt.figure(1)
plt.plot(Zr_10[:,0], Zr_10[:,1], label = 'Zr = 10%')
plt.plot(Zr_10[:,0], Zr_30[:,1], label = 'Zr = 30%')
plt.plot(Zr_10[:,0], Zr_50[:,1], label = 'Zr = 50%')
plt.plot(Zr_10[:,0], Zr_70[:,1], label = 'Zr = 70%')
plt.plot(Zr_10[:,0], Zr_85[:,1], label = 'Zr = 85%')
plt.legend()
plt.savefig(save_path + 'detailed_analysis')