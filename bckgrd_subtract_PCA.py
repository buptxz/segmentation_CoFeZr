"""
author: Fang Ren (SSRL)

2/7/2017
"""


import numpy as np
import os.path
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


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

PCA_class = PCA(n_components= 10)
PCA_class.fit(data)

components = PCA_class.components_

plt.figure(1)
plt.subplot(521)
plt.plot(range(components.shape[1]), components[0, :])
plt.subplot(522)
plt.plot(range(components.shape[1]), components[1, :])
plt.subplot(523)
plt.plot(range(components.shape[1]), components[2, :])
plt.subplot(524)
plt.plot(range(components.shape[1]), components[3, :])
plt.subplot(525)
plt.plot(range(components.shape[1]), components[4, :])
plt.subplot(526)
plt.plot(range(components.shape[1]), components[5, :])
plt.subplot(527)
plt.plot(range(components.shape[1]), components[6, :])
plt.subplot(528)
plt.plot(range(components.shape[1]), components[7, :])
plt.subplot(529)
plt.plot(range(components.shape[1]), components[8, :])
plt.subplot(5,2,10)
plt.plot(range(components.shape[1]), components[9, :])



