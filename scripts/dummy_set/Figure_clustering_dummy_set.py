"""
author: Fang Ren (SSRL)

5/25/2017
"""


import numpy as np
import os
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import spectral_clustering
import imp
from scipy.spatial.distance import cdist
from os.path import join
import scipy.io
from PIL import Image

plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")



oneD_path = '..\\..\\data\\dummy_data\\1D\\'
twoD_path = '..\\..\\data\\dummy_data\\2D\\'
save_path = '..\\..\\figures\\dummy\\'

oneD_data = []
twoD_data = []

# read data
for i in range(2278):
    spectrum = np.genfromtxt(oneD_path + str(i) + '.csv', delimiter=',')
    intensity = spectrum[:,1]
    oneD_data.append(intensity)
oneD_data = np.array(oneD_data)
print oneD_data.shape

for i in range(2278):
    intensity = scipy.io.loadmat(twoD_path + str(i) + '.mat')['cake']
    intensity = np.reshape(intensity, (intensity.shape[0]*intensity.shape[1]))
    twoD_data.append(intensity)
twoD_data = np.array(twoD_data)


# read masterdata
masterfile= '..\\..\\data\\dummy_data\\masterdata.csv'
masterdata = np.genfromtxt(masterfile, delimiter=',', skip_header=1)
A = masterdata[:,0]
B = masterdata[:,1]
C = masterdata[:,2]
peak_num = masterdata[:,3]
peak_intensity = masterdata[:,4]
FWHM = masterdata[:,5]


ternary_data = np.concatenate(([A], [C], [B], [peak_num]), axis=0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='', labelNames=('A', 'C', 'B'), scale=100,
                             sv=True, svpth=save_path, svflnm='num_of_peaks',
                             cbl='number of peaks', cmap='viridis', cb=True, style='h')

ternary_data = np.concatenate(([A], [C], [B], [FWHM]), axis=0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='', labelNames=('A', 'C', 'B'), scale=100,
                             sv=True, svpth=save_path, svflnm='FWHM',
                             cbl='FWHM', cmap='viridis', cb=True, style='h')

ternary_data = np.concatenate(([A], [C], [B], [peak_intensity]), axis=0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='', labelNames=('A', 'C', 'B'), scale=100,
                             sv=True, svpth=save_path, svflnm='peak intensity',
                             cbl='peak intensity', cmap='viridis', cb=True, style='h')

# clustering
cl = AgglomerativeClustering(n_clusters= 5, affinity = 'cosine', linkage= 'average')
labels_1D = cl.fit_predict(oneD_data)

cl2 = AgglomerativeClustering(n_clusters= 7, affinity = 'cosine', linkage= 'average')
labels_2D = cl2.fit_predict(twoD_data)

# distance_1D = cdist(oneD_data, oneD_data, 'cosine')
# similarity_1D = 1 - distance_1D
#
# cl3 = spectral_clustering(n_clusters= 4, affinity = 'precomputed', eigen_solver='arpack')
# labels_1D_sc = cl3.fit_predict(oneD_data)
#
#
# distance_2D = cdist(twoD_data, twoD_data, 'cosine')
# similarity_2D = 1 - distance_2D
# cl4 = spectral_clustering(n_clusters= 5, affinity = 'precomputed', eigen_solver='arpack')
# labels_2D_sc = cl4.fit_predict(similarity_2D)

# save result
#np.savetxt(join(save_path, 'Spectra_2d_precomputed.csv'), labels, delimiter=',')



# plotting
ternary_data = np.concatenate(([A], [C], [B], [labels_1D]), axis=0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='', labelNames=('A', 'C', 'B'), scale=100,
                             sv=True, svpth=save_path, svflnm='Figure_agglomerative_1d',
                             cbl='Agglomerative clustering (1D)', cmap='viridis', cb=True, style='h')


ternary_data = np.concatenate(([A], [C], [B], [labels_2D]), axis=0)
ternary_data = np.transpose(ternary_data)

plotTernary.plt_ternary_save(ternary_data, tertitle='', labelNames=('A', 'C', 'B'), scale=100,
                             sv=True, svpth=save_path, svflnm='Figure_agglomerative_2d',
                             cbl='Agglomerative clustering (2D)', cmap='viridis', cb=True, style='h')
#
# ternary_data = np.concatenate(([A], [C], [B], [labels_1D_sc]), axis=0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='', labelNames=('A', 'C', 'B'), scale=100,
#                              sv=True, svpth=save_path, svflnm='Figure_spectral_1d',
#                              cbl='spectral clustering (1D)', cmap='viridis', cb=True, style='h')
#
#
# ternary_data = np.concatenate(([A], [C], [B], [labels_2D_sc]), axis=0)
# ternary_data = np.transpose(ternary_data)
#
# plotTernary.plt_ternary_save(ternary_data, tertitle='', labelNames=('A', 'C', 'B'), scale=100,
#                              sv=True, svpth=save_path, svflnm='Figure_spectra_2d',
#                              cbl='spectral clustering (2D)', cmap='viridis', cb=True, style='h')

