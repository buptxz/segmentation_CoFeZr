# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 16:22:25 2016

@author: fangren
"""

import numpy as np


## user input
folder_path = 'C:\\Research_FangRen\\XRF_Co_Fe_Zr\\mca_files\\Sample16_peak_fit\\'
base_filename = 'Sample16_2thin_24x24_t30_'
master_path = 'C:\Research_FangRen\XRF_Co_Fe_Zr\mca_files\master_files\\'
master_file = 'Sample16_master_metadata_high.csv'

save_path = 'C:\Research_FangRen\XRF_Co_Fe_Zr\mca_files\master_files_XRF\\'

## Initialization
basefile_path = folder_path + base_filename
index = 1
total_num_scan = 440

Fe_alpha1 = []
Fe_alpha2 = []
Fe_beta = []
Co_alpha1 = []
Co_alpha2 = []
Co_beta = []

while (index <= total_num_scan):
    print 'processing', basefile_path + str(index) + '_peak_analysis.csv'
    file_name = basefile_path + str(index) + '_peak_analysis.csv'
    XRF_info = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
    Fe_alpha1.append(XRF_info[0][0])
    Fe_alpha2.append(XRF_info[0][1])
    Fe_beta.append((XRF_info[0][0]+XRF_info[0][1])*0.137)
    Co_alpha1.append((XRF_info[0][2]-(XRF_info[0][0]+XRF_info[0][1])*0.137)/3*2)
    Co_alpha2.append((XRF_info[0][2]-(XRF_info[0][0]+XRF_info[0][1])*0.137)/3)
    Co_beta.append(XRF_info[0][3])
    index += 1

XRF_channels = np.concatenate(([Fe_alpha1], [Fe_alpha2], [Fe_beta], [Co_alpha1], [Co_alpha2], [Co_beta]), axis = 0)
print XRF_channels.T.shape


header_string = 'Fe_alpha1,Fe_alpha2,Fe_beta,Co_alpha1,Co_alpha2,Co_beta'
# print header_string
np.savetxt(save_path + master_file, XRF_channels.T, delimiter=",", header= header_string)