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

def read_data(total_num_scan, index, basefile_paths):
    peak_position = []
    peak_intensity = []
    peak_width = []
    for basefile_path in basefile_paths:    
        while (index <= total_num_scan):
            print 'processing', basefile_path + file_index(index) + 'bckgrd_subtracted_peak_analysis_Voigt.csv'  
            file_name = basefile_path + file_index(index) + 'bckgrd_subtracted_peak_analysis_Voigt.csv'
            peak_info = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
            peak_position.append(peak_info[1][0])
            peak_intensity.append(peak_info[1][1])
            peak_width.append(peak_info[1][2])                
            index += 1
        index = 1
    return peak_position, peak_intensity, peak_width


## user input
folder_path = 'C:\\Research_FangRen\\Data\\July2016\\CoZrFe_ternary\\1D\\Sample16\\background_subtracted\\peak_fit_threePeaks_Voigt\\'
base_filename1 = 'Sample16_2thin_24x24_t30_'
base_filename2 = 'Sample14_7thin_24x24_t30_'
base_filename3 = 'Sample17_24x24_t30_'
total_num_scan = 441

## Initialization
basefile_path1 = folder_path + base_filename1
basefile_path2 = folder_path + base_filename2
basefile_path3 = folder_path + base_filename3
basefile_paths = [basefile_path1]
index = 1;


peak_position, peak_intensity, peak_width = read_data(total_num_scan, index, basefile_paths)
np.savetxt(folder_path + 'peak_position.csv', peak_position, delimiter = ',')
np.savetxt(folder_path + 'peak_width.csv', peak_width, delimiter = ',')
np.savetxt(folder_path + 'peak_intensity.csv', peak_intensity, delimiter = ',')
