"""
author: Fang Ren (SSRL)

2/7/2017
"""


import numpy as np
import os.path
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


def read_data(total_num_scan, index, basefile_path):
    data = []
    while (index <= total_num_scan):
        file_name = basefile_path + file_index(index)+'_1D.csv'
        if os.path.exists(file_name):
            print 'importing', basefile_path + file_index(index) + '_1D.csv'
            spectrum = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
            data.append(spectrum[:,1][-929:])
            index += 1
        else:
            index += 1
            continue
    return np.array(data)

path = 'C:\\Research_FangRen\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\raw_1D'
filename = 'Sample1_24x24_t30_'
basefile_path = os.path.join(path, filename)

data = read_data(441, 1, basefile_path)

Int_median = np.min(data, axis = 0)
plt.plot(range(len(Int_median)), Int_median)
