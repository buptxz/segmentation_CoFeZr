# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 14:20:44 2016

@author: fangren
"""


import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from sklearn.cluster import DBSCAN
import imp
from scipy.spatial.distance import cdist


plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")
KMedoids = imp.load_source("KMedoids", "k_medoids_.py")

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
            file_name = basefile_path + file_index(index) + '_bckgrd_subtracted.csv'
            #file_name = basefile_path + file_index(index) + '_1D.csv'
            if os.path.exists(file_name):
                print 'importing', basefile_path + file_index(index) + '_bckgrd_subtracted.csv'
                #print 'importing', basefile_path + file_index(index) + '_1D.csv'
                spectrum = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
                data.append(spectrum[:,1][:-19])
                #data.append(spectrum[:,1][:1000])
                index += 1
            else:
                index += 1
                continue
        index = 1
    return np.array(data)


def DBSCAN_clustering(distance):
    labels = DBSCAN(eps=0.001, metric = 'precomputed', min_samples=10).fit_predict(distance)
    return labels

      
## user input
folder_path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\bckgrd_subtracted_1D\\'
base_filename1 = 'Sample1_24x24_t30_'
base_filename2 = 'Sample3_24x24_t30_'
base_filename3 = 'Sample16_2thin_24x24_t30_'
file_num = 441


## Initialization
basefile_path1 = folder_path + base_filename1
basefile_path2 = folder_path + base_filename2
basefile_path3 = folder_path + base_filename3
basefile_paths = [basefile_path1, basefile_path2, basefile_path3]
save_path = folder_path + 'clustering\\'
if not os.path.exists(save_path):
    os.makedirs(save_path)

index = 1;              
  

# read data
data = read_data(file_num, index, basefile_paths)
distance = cdist(data, data, 'cosine')
labels = DBSCAN_clustering(distance)