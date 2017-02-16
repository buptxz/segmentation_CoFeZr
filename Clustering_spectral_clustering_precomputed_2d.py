# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 14:20:44 2016

@author: fangren
"""

import numpy as np
import os
from sklearn.cluster import SpectralClustering
import imp
from scipy.spatial.distance import cdist
from os.path import join
import scipy.io
from PIL import Image

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
        # print basefile_path
        silicon_file = basefile_path + '0233_Qchi.mat'
        silicon_Qchi = scipy.io.loadmat(silicon_file)
        silicon = silicon_Qchi['cake']
        while (index <= total_num_scan):
            file_name = basefile_path + file_index(index) + '_Qchi.mat'
            # file_name = basefile_path + file_index(index) + '_1D.csv'
            if os.path.exists(file_name):
                print 'importing', basefile_path + file_index(index) + '_Qchi.mat'
                # print 'importing', basefile_path + file_index(index) + '_1D.csv'
                Qchi = scipy.io.loadmat(file_name)
                cake = Qchi['cake']
                # plt.imshow(cake)
                # plt.figure(2)
                # plt.imshow(silicon)
                cake = cake - silicon*0.95
                # plt.figure(3)
                # plt.imshow(cake)
                im = Image.fromarray(cake)
                im_compressed = im.resize((100, 100), Image.ANTIALIAS)
                cake_compressed = np.array(im_compressed)
                cake = cake_compressed.reshape(cake_compressed.shape[0] * cake_compressed.shape[1])
                data.append(cake)
                index += 1
            else:
                index += 1
                continue
        #     break
        # break
        index = 1
    return np.array(data)


def spectra(similarity, clusters):
    cl = SpectralClustering(n_clusters=clusters, affinity = 'precomputed', eigen_solver='arpack')
    labels = cl.fit_predict(similarity)
    return labels

## user input
folder_path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\Qchi\\'
base_filename1 = 'Sample1_24x24_t30_'
base_filename2 = 'Sample3_24x24_t30_'
base_filename3 = 'Sample16_2thin_24x24_t30_'
file_num = 441

## Initialization
basefile_path1 = folder_path + base_filename1
basefile_path2 = folder_path + base_filename2
basefile_path3 = folder_path + base_filename3
basefile_paths = [basefile_path1, basefile_path2, basefile_path3]

save_path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\Clustering\\'

index = 1;

# read data
data = read_data(file_num, index, basefile_paths)

# read masterdata
path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\Masterfiles\\high\\'
basename1 = 'Sample1_master_metadata.csv'
basename2 = 'Sample3_master_metadata.csv'
basename3 = 'Sample16_master_metadata.csv'

filename1 = path + basename1
filename2 = path + basename2
filename3 = path + basename3

data1 = np.genfromtxt(filename1, delimiter=',', skip_header=1)
data2 = np.genfromtxt(filename2, delimiter=',', skip_header=1)
data3 = np.genfromtxt(filename3, delimiter=',', skip_header=1)

masterdata = np.concatenate((data1[:, :69], data2[:, :69], data3[:, :69]))

# use ROI to filter bad data
ROI = masterdata[:, 15]
masterdata = masterdata[ROI > 20000]
data = data[ROI > 20000]

# DBSCAN clustering
distance = cdist(data, data, 'cosine')
similarity = 1 - distance



labels = spectra(similarity, 7)

# save result
np.savetxt(join(save_path, 'Spectra_2d_precomputed.csv'), labels, delimiter=',')

# plotting
Co = masterdata[:, 58] * 100
Fe = masterdata[:, 59] * 100
Zr = masterdata[:, 60] * 100

ternary_data = np.concatenate(([Co], [Fe], [Zr], [labels]), axis=0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='', labelNames=('Co', 'Fe', 'Zr'), scale=100,
                             sv=True, svpth=save_path, svflnm='Spectra_2d_precomputed',
                             cbl='Scale', cmap='viridis', cb=True, style='h')