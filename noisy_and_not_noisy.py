from scipy.signal import savgol_filter
import numpy as np
import matplotlib.pyplot as plt

filename = 'C:\\Research_FangRen\\Data\\July2016\\CoZrFe_ternary\\1D\\raw_1D\\Sample1_24x24_t30_0002_1D.csv'
path = 'C:\\Research_FangRen\\Publications\\on_the_fly_paper\\Figures\\'

data = np.genfromtxt(filename, delimiter = ',')
Qlist = data[6:940,0]
IntAve = data[6:940,1]
IntAve_smoothed = savgol_filter(IntAve, 5, 2)
noise = IntAve - IntAve_smoothed

plt.figure(1, (6,5.5))
plt.subplot(211)
plt.plot(Qlist, IntAve, label = 'raw signal')
plt.plot(Qlist, IntAve_smoothed, 'r--', label = 'smoothed signal')
plt.ylabel('Intensity')
plt.xlim(0.5, 6)
plt.legend()
plt.subplot(212)
plt.plot(Qlist, noise, label = 'noise')
plt.ylabel('Noise')
plt.xlabel('Q')
plt.legend()
plt.xlim(0.5, 6)
power_noise = np.sum(np.square(noise))/len(noise)
power_signal = np.sum(np.square(IntAve))/len(IntAve)
SNR = power_signal/power_noise
plt.savefig(path+'figure1', dpi = 600)

