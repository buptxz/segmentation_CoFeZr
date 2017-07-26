"""
author: fangren
"""

import numpy as np
import os.path

def file_index(index):
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)


def read_data(total_num_scan, index, basefile_paths, wavelength = 1.54):
    data = []
    for basefile_path in basefile_paths:
        #print basefile_path
        while (index <= total_num_scan):
            #file_name = basefile_path + file_index(index) + '_bckgrd_subtracted.csv'
            file_name = basefile_path + file_index(index) + '_1D.csv'
            if os.path.exists(file_name):
                #print 'importing', basefile_path + file_index(index) + '_bckgrd_subtracted.csv'
                print 'importing', basefile_path + file_index(index) + '_1D.csv'
                spectrum = np.genfromtxt(file_name, delimiter=',', skip_header = 0)
                if index == 1 and basefile_paths.index(basefile_path) == 0:
                    Q = spectrum[:,0][:-19]
                    twoTheta = np.arcsin(Q * wavelength /(4*np.pi)) * 2 / np.pi * 180
                    data.append(twoTheta)
                intensity = spectrum[:,1][:-19]
                intensity = intensity / np.nanmax(intensity)
                data.append(intensity)
                index += 1
            else:
                index += 1
                continue
        index = 1
    return np.array(data)

if __name__ == '__main__':
    ## user input
    folder_path = '..\\..\\data\\raw_1D\\'
    base_filename1 = 'Sample1_24x24_t30_'
    base_filename2 = 'Sample3_24x24_t30_'
    base_filename3 = 'Sample16_2thin_24x24_t30_'
    file_num = 441

    basefile_path1 = folder_path + base_filename1
    basefile_path2 = folder_path + base_filename2
    basefile_path3 = folder_path + base_filename3
    basefile_paths = [basefile_path1, basefile_path2, basefile_path3]

    index = 1;
    data = read_data(file_num, index, basefile_paths)
    print data.shape

    import matplotlib.pyplot as plt
    twoTheta = data[0]
    for i in range(1, 2):
        plt.plot(twoTheta, data[i])
    plt.show()