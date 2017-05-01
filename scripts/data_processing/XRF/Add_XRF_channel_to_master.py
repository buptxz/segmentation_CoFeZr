# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 16:22:25 2016

@author: fangren
"""

import numpy as np


## user input
folder_path = 'C:\Research_FangRen\Data\Metallic_glasses_data\CoZrFe_ternary\XRF\mca_files\XRF_channels_fit_Sample6\\'
base_filename = 'Sample6_24x24_t30_'

master_path = 'C:\\Research_FangRen\Data\\Metallic_glasses_data\\CoZrFe_ternary\\XRF\\master_files_XRF\\'
master_file = 'Sample6_master_metadata.csv'

save_path = 'C:\\Research_FangRen\Data\\Metallic_glasses_data\\CoZrFe_ternary\\XRF\\master_files_XRF\\'

## Initialization
basefile_path = folder_path + base_filename
index = 1
total_num_scan = 440

Fe_alpha = []
Fe_beta = []
Co_alpha = []
Co_beta = []

while (index <= total_num_scan):
    print 'processing', basefile_path + str(index) + '_XRF_fit.csv'
    file_name = basefile_path + str(index) + '_XRF_fit.csv'
    XRF_info = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
    Fe_alpha.append(XRF_info[0][0])
    Fe_beta.append(XRF_info[0][1])
    Co_alpha.append(XRF_info[0][2])
    Co_beta.append(XRF_info[0][3])
    index += 1

XRF_channels = np.concatenate(([Fe_alpha], [Fe_beta], [Co_alpha], [Co_beta]), axis = 0)
print XRF_channels.T.shape


header_string = 'Fe_alpha,Fe_beta,Co_alpha,Co_beta'
# print header_string
np.savetxt(save_path + master_file, XRF_channels.T, delimiter=",", header= header_string)