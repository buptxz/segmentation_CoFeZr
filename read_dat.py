import numpy as np
import matplotlib.pyplot as plt

filename = 'C:\\Research_FangRen\\XRF_Co_Fe_Zr\\mca_files\\Sample1_24x24_t30_scan1_mca.dat'

data = np.genfromtxt(filename, delimiter=' ')

plt.plot(range(2049), data[1])

'''
23  V       4.95220   4.94464   5.42729
27  Co      6.93032   6.91530   7.64943
'''


