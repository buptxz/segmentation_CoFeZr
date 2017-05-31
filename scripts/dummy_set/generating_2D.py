"""
author: Fang Ren (SSRL)

5/3/2017
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import gaussian
from scipy.io import savemat


def isTextured(a, b, c):
    if a >= 40:
        return True
    else:
        return False

def cake_generation(chi, intensities, textured):
    cake = []
    for intensity in intensities:
        if not textured:
            chi_intensity = [intensity] * len(chi)
        if textured:
            chi_intensity = gaussian(len(chi), 10, sym=True)
            chi_intensity = chi_intensity / np.mean(chi_intensity) * intensity
        cake.append(chi_intensity)
    return cake

path = '..//..//data//dummy_data//1D//'
save_path = '..//..//data//dummy_data//2D//'



A = np.arange(0, 100, 1.5)
B = np.arange(0, 100, 1.5)
A, B = np.meshgrid(A, B)

C = 100-A-B

keep = (C <= 100) * (C >= 0)

A = A[keep]
B = B[keep]
C = C[keep]

for i in range(len(A)):
    print 'generating', str(i)
    spectrum = np.genfromtxt(path + str(i) + '.csv', delimiter=',')
    Q = spectrum[:,0]
    intensities = spectrum[:,1]
    #print intensities
    chi = np.arange(-60, 60, 1)
    cake = cake_generation(chi, intensities, isTextured(A[i], B[i], C[i]))
    cake = np.array(cake).T
    #print cake.shape
    Q, chi = np.meshgrid(Q, chi)
    plt.pcolormesh(Q, chi, cake)
    plt.xlabel('Q')
    plt.ylabel('ch')
    plt.savefig(save_path + str(i) + '.png')
    plt.close('all')
    savemat(save_path + str(i) + '.mat', {'cake':cake})