# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 17:06:41 2016

@author: fangren
"""

import os.path
import matplotlib.pyplot as plt
import numpy as np

path = 'C:\\Research_FangRen\\Data\\Metallic_glasses_data\\CoZrFe_ternary\\1D\\raw_1D'

silicon_file = os.path.join(path, 'Sample1_24x24_t30_0233_1D.csv')
spectrum_file = os.path.join(path, 'Sample1_24x24_t30_0001_1D.csv')

silicon = np.genfromtxt(silicon_file, delimiter=',')
spectrum = np.genfromtxt(spectrum_file, delimiter= ',')
Q = silicon[:, 0]
bckgrd = silicon[: ,1]
intensity = spectrum[:, 1]


plt.figure(1)
plt.subplot(211)
plt.plot(Q, bckgrd)
plt.plot(Q, intensity)

# plt.subplot(212)
# f = 1.1
# plt.plot(Q, intensity - bckgrd*f-78)
# plt.plot(Q, np.zeros(len(Q)))
#

plt.subplot(212)
f = 0.98
plt.plot(Q, intensity - bckgrd*f-160)
plt.plot(Q, np.zeros(len(Q)))

