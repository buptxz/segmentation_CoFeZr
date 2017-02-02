from scipy.signal import savgol_filter
import numpy as np
import matplotlib.pyplot as plt

folder = 'C:\\Research_FangRen\\Data\\July2016\\CoZrFe_ternary\\1D\\raw_1D\\'
basefilename1 = 'Sample1_24x24_t30_'
basefilename2 = 'Sample3_24x24_t30_'
basefilename3 = 'Sample16_2thin_24x24_t30_'

basefilenames = [basefilename1, basefilename2, basefilename3]
index = 1

def file_index(index):
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)

SNRs = []
for basefilename in basefilenames:
    while(index <= 441):
        filename = folder + basefilename + file_index(index) + '_1D.csv'
        print 'processing', filename
        data = np.genfromtxt(filename, delimiter = ',')
        Qlist = data[6:940,0]
        IntAve = data[6:940,1]
        IntAve_smoothed = savgol_filter(IntAve, 5, 2)
        noise = IntAve - IntAve_smoothed
        # plt.plot(Qlist, IntAve)
        # plt.plot(Qlist, IntAve_smoothed)
        # plt.plot(Qlist, noise)
        power_noise = np.sum(np.square(noise))/len(noise)
        power_signal = np.sum(np.square(IntAve))/len(IntAve)
        SNR = power_signal/power_noise
        SNRs.append(SNR)
        index += 1
    index = 1

np.savetxt(folder + 'SNR.csv', SNRs, delimiter = ',')