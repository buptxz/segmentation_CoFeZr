# -*- coding: utf-8 -*-
"""
Created on Fri Aug 05 16:31:12 2016

@author: fangren
"""

import numpy as np
import matplotlib.pyplot as plt

def file_index(index):
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)

plt.figure(1, figsize = (4, 6))
def read_data(indices, basefile_path):
    data = []
    for index in indices:
#        print 'importing', basefile_path + file_index(index) + 'bckgrd_subtracted.csv'  
        file_name = basefile_path + file_index(index) + 'bckgrd_subtracted.csv'
        spectrum = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
        plt.plot(spectrum[:,0],spectrum[:,1])
#        data.append(spectrum[:,1][:1000])
    return np.array(data)

#indices = range(325, 303, -1)
#indices = range(96, 117)
indices1 = [164, 187, 188, 189, 190, 215, 216, 217, 243, 244, 269, 270, 296, 322]
indices2 = [283, 310, 335, 336, 360, 383]
indices1.reverse()
indices2.reverse()



folder_path = 'C:\\Research_FangRen\\Data\\July2016\\CoVZr_ternary\\1Dfiles\\high_power_8_14_17\\background_subtracted\\'
base_filename1 = 'Sample17_24x24_t30_'
base_filename2 = 'Sample8_24x24_t30_'


basefile_path1 = folder_path + base_filename1
basefile_path2 = folder_path + base_filename2


data = read_data(indices2, basefile_path2) + read_data(indices1, basefile_path1)


    
#Qlist = [0.641494956 + i * 0.005659752277277276 for i in range(929)]
##num_of_scan = [325-i for i in range(len(indices))]
#num_of_scan = range(len(indices))
##num_of_scan = [i+96 for i in range(len(indices))]
#Qlist, num_of_scan = np.meshgrid(Qlist, num_of_scan)
#
#plt.pcolormesh(Qlist, num_of_scan, data)

plt.xlabel('Q')
plt.ylabel('intensity')
plt.xlim((1.5, 4))
plt.ylim((-50, 1250))
#plt.colorbar()
