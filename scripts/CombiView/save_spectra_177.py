"""
author: fangren
"""
from import_1D import read_data
import numpy as np

## user input
folder_path = '..\\..\\data\\1D\\'
base_filename1 = 'Sample1_24x24_t30_'
basefile_path1 = folder_path + base_filename1
basefile_paths = [basefile_path1]  # if there are more than one folder you want to organize, put all in this bracket

index = 1
file_num = 177

data = read_data(file_num, index, basefile_paths, wavelength= 1.54)
np.savetxt('..//..//data//CombiView//XRD_spectra_CoFeZr.txt', data, delimiter='\t', fmt='%10.5f', comments='')