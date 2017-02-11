# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 16:22:25 2016

@author: fangren
"""

import numpy as np

def file_index(index):
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)

def read_data(total_num_scan, index, basefile_path):
    peak_position = []
    peak_intensity = []
    peak_width = []
    while (index <= total_num_scan):
        print 'processing', basefile_path + file_index(index) + '_bckgrd_subtracted_peak_fitting_Voigt.csv'
        file_name = basefile_path + file_index(index) + '_bckgrd_subtracted_peak_fitting_Voigt.csv'
        peak_info = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
        peak_position.append(peak_info[0])
        peak_intensity.append(peak_info[1])
        peak_width.append(peak_info[2])
        #print peak_info
        index += 1
    return peak_position, peak_intensity, peak_width


## user input
folder_path = 'C:\\Research_FangRen\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\peak_fitting_voigt\\'
base_filename1 = 'Sample3_24x24_t30_'
total_num_scan = 441

## Initialization
basefile_path1 = folder_path + base_filename1
index = 1;


peak_position, peak_intensity, peak_width = read_data(total_num_scan, index, basefile_path1)
np.savetxt(folder_path + 'peak_info.csv', np.concatenate(([peak_position], [peak_width], [peak_intensity])).T, header = 'peak_position, peak_width, peak_intensity', delimiter = ',')
