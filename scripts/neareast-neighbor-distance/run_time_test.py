"""
author: Fang Ren (SSRL)

3/21/2017

run time test for calculating distance between a pair of spectra and a pair of images
"""

from scipy.spatial import distance
import scipy.io
import time
import numpy as np


# import two images for run time test
image_path = 'C:\\Research_FangRen\Data\\Metallic_glasses_data\\CoZrFe_ternary\\Qchi\\'
image_name1 = 'Sample1_24x24_t30_0001_Qchi.mat'
image_name2 = 'Sample1_24x24_t30_0002_Qchi.mat'
image1 =scipy.io.loadmat(image_path+image_name1)['cake']
image2 =scipy.io.loadmat(image_path+image_name2)['cake']


# import two spectra for run time test
spectrum_path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\raw_1D\\'
spectrum_name1 = 'Sample1_24x24_t30_0001_1D.csv'
spectrum_name2 = 'Sample1_24x24_t30_0002_1D.csv'
spectrum1 = np.genfromtxt(spectrum_path + spectrum_name1, delimiter = ',')[:, 1]
spectrum2 = np.genfromtxt(spectrum_path + spectrum_name2, delimiter = ',')[:, 1]


# run time test for calculating distances between two images
image1_flat = image1.reshape(image1.shape[0] * image1.shape[1])
image2_flat = image2.reshape(image2.shape[0] * image2.shape[1])
time1 = time.time()
for i in range(441*2):
    distance_sum = distance.cosine(image1_flat, image2_flat)
run_time1 = time.time()-time1


# run time test for calculating distances between two spectra
time2 = time.time()
for i in range(441*2):
    distance_sum = distance.cosine(spectrum1, spectrum2)
run_time2 = time.time()-time2

print run_time1, run_time2