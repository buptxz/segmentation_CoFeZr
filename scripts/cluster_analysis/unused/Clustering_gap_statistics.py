# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:54:35 2016

@author: fangren
"""

import numpy as np
import scipy
import scipy.cluster.vq
import scipy.spatial.distance
dst = scipy.spatial.distance.euclidean
from sklearn.cluster import k_means
import matplotlib.pyplot as plt
import os


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
    data = []
    for basefile_path in basefile_paths:
        #print basefile_path
        while (index <= total_num_scan):
            
            file_name = basefile_path + file_index(index) + '_1D.csv'
            if os.path.isfile(file_name):
                print 'importing', basefile_path + file_index(index) + '_1D.csv'  
                spectrum = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
                data.append(spectrum[:,1][:1000])
                index += 1
            else:
                index += 1
                continue
        index = 1
    return np.array(data)


def gap(data, refs=None, nrefs=20, ks=range(1,11)):
    """
    Compute the Gap statistic for an nxm dataset in data.
    Either give a precomputed set of reference distributions in refs as an (n,m,k) scipy array,
    or state the number k of reference distributions in nrefs for automatic generation with a
    uniformed distribution within the bounding box of data.
    Give the list of k-values for which you want to compute the statistic in ks.
    """
    shape = data.shape
    if refs==None:
        tops = data.max(axis=0)
        bots = data.min(axis=0)
        dists = scipy.matrix(scipy.diag(tops-bots))
	

        rands = scipy.random.random_sample(size=(shape[0],shape[1],nrefs))
        for i in range(nrefs):
            rands[:,:,i] = rands[:,:,i]*dists+bots
    else:
        rands = refs

    gaps = scipy.zeros((len(ks),))
    for (i,k) in enumerate(ks):
        print 'calculating gaps for', k, 'clusters'
        (kmc,kml,inertia) = k_means(data, k, init='k-means++')
        disp = sum([dst(data[m,:],kmc[kml[m],:]) for m in range(shape[0])])

        refdisps = scipy.zeros((rands.shape[2],))
        for j in range(rands.shape[2]):
            (kmc,kml,inertia) = k_means(rands[:,:,j], k, init='k-means++')
            refdisps[j] = sum([dst(rands[m,:,j],kmc[kml[m],:]) for m in range(shape[0])])
        gaps[i] = scipy.log(scipy.mean(refdisps))-scipy.log(disp)
        print 'gap =', gaps[i]
    return gaps

    
## user input
folder_path = 'C:\\Research_FangRen\\Data\\July2016\\CoZrFe_ternary\\1D\\raw_1D\\'
base_filename1 = 'Sample1_24x24_t30_'
base_filename2 = 'Sample3_24x24_t30_'
base_filename3 = 'Sample16_2thin_24x24_t30_'
file_num = 441


## Initialization
basefile_path1 = folder_path + base_filename1
basefile_path2 = folder_path + base_filename2
basefile_path3 = folder_path + base_filename3
basefile_paths = [basefile_path1, basefile_path2, basefile_path3]
save_path = folder_path + 'clustering\\'
if not os.path.exists(save_path):
    os.makedirs(save_path)

index = 1;              

# read data
data = read_data(file_num, index, basefile_paths)

# run gap statistics
gaps = gap(data)
ks=range(1,11)
plt.plot(ks, gaps)
