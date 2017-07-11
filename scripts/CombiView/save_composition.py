"""
author: fangren
"""
import numpy as np


# read masterdata
path = '..\\..\\data\\Masterfiles\\'
basename1 = 'Sample1_master_metadata.csv'
basename2 = 'Sample3_master_metadata.csv'
basename3 = 'Sample16_master_metadata.csv'

filename1 = path + basename1
filename2 = path + basename2
filename3 = path + basename3

data1 = np.genfromtxt(filename1, delimiter=',', skip_header = 1)
data2 = np.genfromtxt(filename2, delimiter=',', skip_header = 1)
data3 = np.genfromtxt(filename3, delimiter=',', skip_header = 1)

masterdata = np.concatenate((data1[:, :69], data2[:, :69], data3[:, :69]))


# use ROI to filter bad data
ROI = masterdata[:, 15]
masterdata = masterdata[ROI > 20000]

composition = masterdata[:,61:64]*100
print composition.shape
#composition = np.round(composition, 2)
#print composition

np.savetxt('..//..//data//CombiView//composition_CoFeZr.txt', composition, fmt='%10.2f', delimiter='\t', header = 'Co, Fe, Zr', comments='')