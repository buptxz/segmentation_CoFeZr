# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 14:20:44 2016

@author: fangren
"""


import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import imp
from scipy.spatial.distance import cdist
import pyclust


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
            file_name = basefile_path + file_index(index) + 'bckgrd_subtracted.csv'
            #file_name = basefile_path + file_index(index) + '_1D.csv'
            if os.path.exists(file_name):
                print 'importing', basefile_path + file_index(index) + 'bckgrd_subtracted.csv'
                #print 'importing', basefile_path + file_index(index) + '_1D.csv'
                spectrum = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
                data.append(spectrum[:,1][-929:])
                #data.append(spectrum[:,1][:1000])
                index += 1
            else:
                index += 1
                continue
        index = 1
    return np.array(data)

def GMM_clustering(data):
    GMM_clusters = pyclust.GMM(5)
    GMM_clusters.fit(data)
    labels = GMM_clusters.labels_
    return labels

def addLabels(labels, folder_path):
    """
    add Imax, I column to an existing CSV spreadsheet
    create three lists for plotting: plate_x, plate_y, ratio of Imax and Iave
    ROI1, ROI2...
    """  
    labels = np.array([labels]).transpose()
    for filename in glob.glob(os.path.join(folder_path, '*.csv')):
        if filename[-5] == 'h':
            master_data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
            master_data = np.nan_to_num(master_data)
#            print master_data.shape, labels.shape
            master_data = np.concatenate((master_data, labels), axis = 1)
            np.savetxt(save_path + 'GMM_clustering.csv', master_data, \
            delimiter=",", header="register#,plate_x,plate_y,Seconds,i0,i1,mon,bstop,Omron,CH6,\
            CH7,TEMP,marccd,ICRxT,OCRxT,ROI1,ROI2,ROI3,ROI4,ROI5,ROI6,ROI7,ROI8,ROI9,\
            ROI10,RIO11,ROI12,ROI13,SWX,CCD1,CTEMP,Timer,pd1,pd2,pd3,pd4,pd5,pd6,pd7,\
            pd8,pd9,pd10,pd11,pd12,pd13,pd14,pd15,pd16,scan#,Imax,Iave,ratio,scan#,texture,\
            Co, Fe, Zr, peak_position, peak_width, peak_intensity, db_labels")


def twoD_visualize(folder_path):
    """
    create three lists for plotting: plate_x, plate_y, ROI1, ROI2, ROI3...
    """
    for filename in glob.glob(os.path.join(folder_path, '*.csv')):
        if filename[-5] == 'h':
            data = np.genfromtxt(filename, delimiter=',', skip_header = 0)
            plate_x = data[:,1]
            plate_y = data[:,2]
            plate_x = np.nan_to_num(plate_x)
            plate_y = np.nan_to_num(plate_y)
            metal1 = data[:,54]
            metal2 = data[:,55]
            metal3 = data[:,56]
    return plate_x, plate_y, metal1, metal2, metal3
                 
           
      
## user input
folder_path = 'C:\\Research_FangRen\\1D\\CLEANED_spectra_bckgrd_subtracted\\'
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

labels = GMM_clustering(data)
addLabels(labels, folder_path)
plate_x, plate_y, metal1, metal2, metal3 = twoD_visualize(folder_path)
#

ternary_data = np.concatenate(([metal1],[metal2],[metal3],[labels]), axis = 0)
ternary_data = np.transpose(ternary_data)


plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','Fe','Zr'), scale=100,
                       sv=True, svpth=save_path, svflnm='GMM_clustering',
                       cbl='Scale', cmap='jet', cb=True, style='h')

plt.close('all')