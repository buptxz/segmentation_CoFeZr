# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 17:06:41 2016

@author: fangren
"""

from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
import os


def file_index(index):
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)

def read_data(total_num_scan, index, basefile_paths):
    data = []
    for basefile_path in basefile_paths:
        #print basefile_path
        while (index <= total_num_scan):
            #file_name = basefile_path + file_index(index) + 'bckgrd_subtracted.csv'
            file_name = basefile_path + file_index(index) + '_1D.csv'
            if os.path.exists(file_name):
                #print 'importing', basefile_path + file_index(index) + 'bckgrd_subtracted.csv'
                print 'importing', basefile_path + file_index(index) + '_1D.csv'
                spectrum = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
                #data.append(spectrum[:,1][-929:])
                data.append(spectrum[:,1][:1000])
                index += 1
            else:
                index += 1
                continue
        index = 1
    return np.array(data)
    

## user input
folder_path = 'C:\\Research_FangRen\\Data\\July2016\\CoZrFe_ternary\\1D\\raw_1D\\'
base_filename1 = 'Sample1_24x24_t30_'
base_filename2 = 'Sample3_24x24_t30_'
base_filename3 = 'Sample16_2thin_24x24_t30_'
file_num = 441


## Initialization
basefile_path1 = folder_path + base_filename1
basefile_path2 = folder_path + base_filename2
basefile_path3 = folder_path + base_filename3
basefile_paths = [basefile_path1, basefile_path2, basefile_path3]

index = 1;              
  

# read data
data = read_data(file_num, index, basefile_paths)



X = [i+1 for i in range(data.shape[0])]
Y = [i+1 for i in range(data.shape[0])]
X, Y = np.meshgrid(X, Y)


# generate a Euclidean distance map
distance_map = cdist(data, data, 'euclidean')

plt.figure(1)
plt.title('Euclidean distance')
plt.pcolormesh(X, Y, distance_map)
plt.xlim((1, data.shape[0]))
plt.ylim((1, data.shape[0]))
plt.show()


# generate a cosine distance map
distance_map = cdist(data, data, 'cosine')
plt.figure(2)
plt.title('Cosine distance')
plt.pcolormesh(X, Y, distance_map)
plt.xlim((1, data.shape[0]))
plt.ylim((1, data.shape[0]))
plt.show()


# generate a cityblock distance map
distance_map = cdist(data, data, 'cityblock')
plt.figure(3)
plt.title('Cityblock distance')
plt.pcolormesh(X, Y, distance_map)
plt.xlim((1, data.shape[0]))
plt.ylim((1, data.shape[0]))
plt.show()
