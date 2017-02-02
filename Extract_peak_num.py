# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 15:37:51 2016

@author: fangren
"""

import matplotlib.pyplot as plt
import numpy as np
import os
import imp
from os.path import basename

peakdet = imp.load_source("peakdet", "peak_detection.py")
  

def file_index(index):
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)


   
## user input
folder_path = 'C:\\Research_FangRen\\Data\\July2016\\CoZrFe_ternary\\1D\\CLEANED_spectra_bckgrd_subtracted\\'
base_filename1 = 'Sample1_24x24_t30_'
base_filename2 = 'Sample3_24x24_t30_'
base_filename3 = 'Sample16_2thin_24x24_t30_'
file_num = 441


## Initialization
basefile_path1 = folder_path + base_filename1
basefile_path2 = folder_path + base_filename2
basefile_path3 = folder_path + base_filename3
basefile_paths = [basefile_path3]
save_path = folder_path + 'peak_detection\\'
if not os.path.exists(save_path):
    os.makedirs(save_path)

index = 1;              

peak_num_list = []


for basefile_path in basefile_paths:
    while (index <= file_num):
        file_name = basefile_path + file_index(index) + 'bckgrd_subtracted.csv'
        if os.path.exists(file_name):
            print 'importing', basefile_path + file_index(index) + 'bckgrd_subtracted.csv'  
            data = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
            Qlist = data[:,0][-929:]
            IntAve = data[:,1][-929:]
            maxtab, mintab = peakdet.peakdet(IntAve, 20)
            if len(maxtab) == 0:
                peaks = []
            else:
                peaks = maxtab[:,0].astype(int)
            if Qlist[peaks[0]] < 1:        
                peaks = peaks[1:]
            if Qlist[peaks[-1]] > 5.5:
                peaks = peaks[:-1]
            plt.figure(1)            
            plt.plot(Qlist, IntAve)
            plt.plot(Qlist[peaks], IntAve[peaks], 'o')
            plt.savefig(save_path + basename(basefile_path) + file_index(index) + '_peak_detection.png')
            plt.close()
            peak_num = len(peaks)
            peak_num_list.append(peak_num)
            index += 1
        else:
            index += 1


np.savetxt(folder_path + 'peak_num.csv', peak_num_list, delimiter = ',')