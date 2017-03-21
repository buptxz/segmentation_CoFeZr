# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 14:03:38 2016

@author: Tri Duong, Fang Ren
"""


import numpy as np
from scipy.spatial import distance
import matplotlib.pyplot as plt
import os.path
import scipy.io
import time

time1 = time.time()


def find_neighbour(index, scan_register, length_of_row):
    """
    return the neighbour directly to right of the desired index and neighbour directly underneath the desired index
    """
    register = scan_register[index-1]
    register_neighbour1 = register - 1
    register_neighbour2 = register - length_of_row
    try:
         index_neighbour1 = scan_register.index(register_neighbour1)+1
         index_neighbour2 = scan_register.index(register_neighbour2)+1
    except ValueError:
         index_neighbour1 = index
         index_neighbour2 = index
    return index_neighbour1, index_neighbour2

def file_index(index):
    """
    formatting the index of each file
    """
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)

def import_data(index, path, base_filename):
    # print basefile_path
    file_name = path + base_filename + file_index(index) + '_Qchi.mat'
    #print 'importing', path + base_filename + file_index(index) + '_Qchi.mat'
    Qchi = scipy.io.loadmat(file_name)
    cake = Qchi['cake']
    # im = Image.fromarray(cake)
    # im_compressed = im.resize((100, 100), Image.ANTIALIAS)
    # cake_compressed = np.array(im_compressed)
    cake_compressed = cake
    cake = cake_compressed.reshape(cake_compressed.shape[0] * cake_compressed.shape[1])
    return cake

path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\Qchi\\'
master_path = 'C:\\Research_FangRen\Data\\Metallic_glasses_data\\CoZrFe_ternary\\Masterfiles\\high\\'
base_filename = 'Sample1_24x24_t30_'

master_file = os.path.join(master_path, 'Sample1_master_metadata.csv')
master_data = np.genfromtxt(master_file, delimiter=',', skip_header=1)
scan_register = list(master_data[:,0])

distances = []
for i in range(441):
    index = i + 1
    index_neighbor1, index_neighbor2 = find_neighbour(index, scan_register, 25)
    point_of_interest = import_data(index, path, base_filename)
    neighbor1 = import_data(index_neighbor1, path, base_filename)
    neighbor2 = import_data(index_neighbor2, path, base_filename)
    distance_sum = distance.cosine(point_of_interest, neighbor1) + distance.cosine(point_of_interest, neighbor2)
    distances.append(distance_sum)

# np.savetxt(path + 'nearest_neighbor_distances_2d.csv', distances, delimiter=',')

runtime = time.time()-time1

print runtime