"""
author: fangren
"""
from import_1D import read_data
import numpy as np

## user input
folder_path = '..\\..\\data\\bckgrd_subtracted_1D\\'
base_filename1 = 'Sample1_24x24_t30_'
base_filename2 = 'Sample3_24x24_t30_'
base_filename3 = 'Sample16_2thin_24x24_t30_'
file_num = 441

basefile_path1 = folder_path + base_filename1
basefile_path2 = folder_path + base_filename2
basefile_path3 = folder_path + base_filename3
basefile_paths = [basefile_path1, basefile_path2, basefile_path3]

index = 1;
data = read_data(file_num, index, basefile_paths, wavelength= 1.54)
#data = read_data(file_num, index, basefile_paths)

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

# use ROI to filter bad data
ROI = masterdata[:, 15]
data = data[ROI > 20000]

print data.shape

np.savetxt('..//..//data//CombiView//XRD_spectra_CoFeZr.txt', data, delimiter='\t', fmt='%10.5f', comments='')