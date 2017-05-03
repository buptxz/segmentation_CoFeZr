"""
author: Fang Ren (SSRL)

5/3/2017
"""

import numpy as np
#from plotTernary import plt_ternary_save
import matplotlib.pyplot as plt

A = np.arange(0, 100, 4)
B = np.arange(0, 100, 4)
A, B = np.meshgrid(A, B)

C = 100-A-B

keep = (C <= 100) * (C >= 0)

A = A[keep]
B = B[keep]
C = C[keep]
length = len(A)
intensity = [0.5]*length
peak_position = B*[0.02]+2
print len(A)

save_path = '..\\..\\data\\dummy_data\\1D\\'



def isHighIntensity(a, b, c):
    if b >66:
        return True
    else:
        return False

def is3peaks(a, b, c):
    if c > 66:
        return True
    else:
        return False

def isAmorphous(a, b, c):
    if (a > 10) and (b > 10) and (c > 10):
        return True
    else:
        return False

def func(x, *params):
    """
    create a Lorentzian fitted curve according to params
    """
    ctr = params[0]
    amp = params[1]
    wid = params[2]
    y = 0.5 * amp * np.exp(-4 * np.log(2) * ((x - ctr) / wid) ** 2) + 0.5 * amp * wid ** 2 / 4 / (
        (x - ctr) ** 2 + wid ** 2 / 4)
    return y


# ternary_data = np.concatenate(([A],[C],[B],[intensity]), axis = 0)
# ternary_data = np.transpose(ternary_data)
#
# plt_ternary_save(ternary_data, tertitle='',  labelNames=('A','C','B'), scale=100,
#                        sv=True, svpth=save_path, svflnm='gray_ternary_dummy',
#                        cbl='', cmap='gray', cb=True, style='h')
#
#
# ternary_data = np.concatenate(([A],[C],[B],[peak_position]), axis = 0)
# ternary_data = np.transpose(ternary_data)
#
# plt_ternary_save(ternary_data, tertitle='',  labelNames=('A','C','B'), scale=100,
#                        sv=True, svpth=save_path, svflnm='peak_position_dummy',
#                        cbl='', cmap='viridis', cb=True, style='h')

peak_positions = []
peak_intensity = []
FWHM = []

for i in range(length):
    a = A[i]
    b = B[i]
    c = C[i]
    if isHighIntensity(a, b, c):
        peak_intensity.append(1000)
    else:
        peak_intensity.append(500)
    if isAmorphous(a,b,c):
        FWHM.append(0.8)
    else:
        FWHM.append(0.1)
    if is3peaks(a,b,c):
        peak_positions.append([peak_position[i], peak_position[i]+0.4, peak_position[i]+0.8])
    else:
        peak_positions.append([peak_position[i]])

# ternary_data = np.concatenate(([A],[C],[B],[peak_intensity]), axis = 0)
# ternary_data = np.transpose(ternary_data)
#
# plt_ternary_save(ternary_data, tertitle='',  labelNames=('A','C','B'), scale=100,
#                        sv=True, svpth=save_path, svflnm='peak_intensity_dummy',
#                        cbl='', cmap='viridis', cb=True, style='h')

print len(peak_positions)
print peak_intensity
print FWHM
Q = np.arange(0.5, 6, 0.01)


for i in range(length):
    intensity = np.zeros_like(Q)
    for peak_position in peak_positions[i]:
        params = [peak_position, peak_intensity[i], FWHM[i]]
        intensity += func(Q, *params)
    plt.plot(Q, intensity)
    plt.savefig(save_path + str(i) + '.jpg')
    plt.close('all')
    np.savetxt(save_path + str(i) + '.csv', np.concatenate(([Q], [intensity])).T, delimiter= ',')
