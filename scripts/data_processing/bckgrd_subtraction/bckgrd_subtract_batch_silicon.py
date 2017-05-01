# -*- coding: utf-8 -*-
"""
Created on Feb 3, 2017

@author: fangren
"""

import os.path
import matplotlib.pyplot as plt
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

path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\raw_1D'
save_path = 'C:\\Research_FangRen\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\bckgrd_subtracted_1D'
basename = 'Sample1_24x24_t30_'

silicon_file = os.path.join(path, 'Sample1_24x24_t30_0233_1D.csv')


silicon = np.genfromtxt(silicon_file, delimiter=',')
Q = silicon[1:943, 0]
bckgrd = silicon[1:943 ,1]
f = 1
bckgrd = bckgrd*f

index = 1
total_num_scan = 441

while (index <= total_num_scan):

    file_name = os.path.join(path, basename + file_index(index) + '_1D.csv')
    print 'processing', file_name
    if os.path.exists(file_name):
        spectrum = np.genfromtxt(file_name, delimiter=',', skip_header=0)[1:943, 1]
        spectrum = spectrum - bckgrd
        np.savetxt(os.path.join(save_path, basename + file_index(index) + '_bckgrd_subtracted.csv'), np.concatenate(([Q], [spectrum])).T, delimiter= ',')
        plt.plot(Q, spectrum)
        plt.plot(Q, [np.min(spectrum)]*len(Q), 'r--')
        plt.savefig(os.path.join(save_path, basename + file_index(index) + '_bckgrd_subtracted.png'))
        plt.close('all')
        index += 1
    else:
        index += 1
        continue
