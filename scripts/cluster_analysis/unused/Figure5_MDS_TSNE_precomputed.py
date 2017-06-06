# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 14:20:44 2016

@author: fangren
"""


import numpy as np
import os
from sklearn.manifold import TSNE, MDS
import imp
from scipy.spatial.distance import cdist
from os.path import join


plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


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
                index += 1
            else:
                index += 1
                continue
        index = 1
    return np.array(data)


      
## user input
folder_path = '..\\..\\data\\bckgrd_subtracted_1D\\'

base_filename1 = 'Sample1_24x24_t30_'
base_filename2 = 'Sample3_24x24_t30_'
base_filename3 = 'Sample16_2thin_24x24_t30_'
file_num = 441


## Initialization
basefile_path1 = folder_path + base_filename1
basefile_path2 = folder_path + base_filename2
basefile_path3 = folder_path + base_filename3
basefile_paths = [basefile_path1, basefile_path2, basefile_path3]

save_path = '..\\..\\figures\\'

index = 1;              
  

# read data
data = read_data(file_num, index, basefile_paths)


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

#print masterdata.shape

# use ROI to filter bad data
ROI = masterdata[:, 15]
masterdata = masterdata[ROI > 20000]
data = data[ROI > 20000]

distance = cdist(data, data, 'cosine')

class_1 = TSNE(n_components= 2, metric= 'cosine')
result_1 = class_1.fit_transform(data)

class_2 = MDS(n_components= 2, dissimilarity= 'precomputed')
result_2 = class_2.fit_transform(distance)

# save result
results = np.concatenate((result_1, result_2), axis = 1)
np.savetxt(join(save_path, 'Dimensionality_reduction_1d_precomputed.csv'), results, delimiter=',')


# plotting
Co = masterdata[:,61]*100
Fe = masterdata[:,62]*100
Zr = masterdata[:,63]*100


ternary_data = np.concatenate(([Co],[Fe],[Zr],[result_1[:,0]]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='Figure5_TSNE_precomputed_1',
                       cbl='TSNE_precomputed_1', cmap='viridis', cb=True, style='h')


ternary_data = np.concatenate(([Co],[Fe],[Zr],[result_1[:,1]]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='Figure5_TSNE_precomputed_2',
                       cbl='TSNE_precomputed_2', cmap='viridis', cb=True, style='h')


ternary_data = np.concatenate(([Co],[Fe],[Zr],[result_2[:,0]]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='Figure5_MSD_1d_precomputed_1',
                       cbl='MSD_1d_precomputed_1', cmap='viridis', cb=True, style='h')


ternary_data = np.concatenate(([Co],[Fe],[Zr],[result_2[:,1]]), axis = 0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='Figure5_MSD_1d_precomputed_2',
                       cbl='MSD_1d_precomputed_2', cmap='viridis', cb=True, style='h')