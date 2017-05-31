"""
author: Travis Williams

May 2017
"""


import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def imp_materials_project(flpth):
    # Import Data from Materials Project folder
    # Folder should contain JSON files downloaded from materials project

    globpth = glob.glob(flpth + '\\*')

    matprojdataframe = pd.DataFrame()
    nm_list = list()
    for pth in globpth:
        tempdf = pd.read_json(pth, orient='columns', lines=True)
        xray_df = pd.DataFrame(tempdf.loc[:, 'pattern'][0], columns=tempdf.loc[:, 'meta'][0])
        nm_list += [pth.split('\\')[-1].split('.')[0]]

        arr_list = [nm_list, ['amplitude','hkl','two_theta','d_spacing']]

        matprojdataframe = pd.concat([matprojdataframe, xray_df], axis=1)

    mind = pd.MultiIndex.from_product(arr_list)
    matprojdataframe = matprojdataframe.transpose().set_index(keys=mind).transpose()

    return matprojdataframe

def imp_spectrum_data(pth):
    tempdf = pd.read_csv(pth, header=None, names=['Q','I']).dropna()
    q_arr = tempdf.loc[:, 'Q'].values
    i_arr = tempdf.loc[:, 'I'].values
    return q_arr, i_arr

def conv_to_q(two_theta):
    q = 4 * np.pi * np.sin(np.deg2rad(two_theta / 2)) / 1.5418
    return q

if __name__ == '__main__':
    # UI Parameters
    matprojpth = r'C:\Users\quick\Raw Data\MG Co-Fe-V-Zr\matprojXRDcalcs\Co-Fe-Zr'
    xrd_data_path = r'C:\Users\quick\Raw Data\MG Co-Fe-V-Zr'
    save_path = r'C:\Users\quick\Raw Data\MG Co-Fe-V-Zr'
    fllst = ['Zr = 10', 'Zr = 30', 'Zr = 50', 'Zr = 70', 'Zr = 85']

    mpdf = imp_materials_project(matprojpth)

    for flnm in fllst:
        Q, I = imp_spectrum_data('{base}\\{flnm}.csv'.format(base=xrd_data_path, flnm=flnm))

        crystal_list = mpdf.columns.levels[0].values
        fig, ax = plt.subplots(4, 5, figsize=(25,20))

        for ii, crys in enumerate(crystal_list):
            xx = np.floor(ii/5)
            yy = ii-5*np.floor(ii/5)
            ax[xx, yy].plot(Q, I)

            crysdf = mpdf.loc[:, crys].dropna()
            crysdf['amplitude'] = crysdf.loc[:, 'amplitude'] / 100 * np.max(I)
            crysdf['Q'] = crysdf.loc[:, 'two_theta'].apply(conv_to_q)
            for xrd_diff_pk in crysdf.iterrows():
                xrd_Q = xrd_diff_pk[1]['Q']
                xrd_I = xrd_diff_pk[1]['amplitude']
                ax[xx, yy].vlines(xrd_Q, 0, xrd_I, linestyles='dashed')

                # Option to show hkl on plot
                if xrd_I > np.max(I)/10:
                    ax[xx, yy].annotate(s=xrd_diff_pk[1]['hkl'],
                                        xy=(xrd_Q, xrd_I),
                                        verticalalignment='baseline',
                                        horizontalalignment='right bottom',
                                        rotation=270)

            ax[xx, yy].set_title(crys)
            ax[xx, yy].set_xlim([1,6])
            ax[xx, yy].set_xlabel('Q')
            ax[xx, yy].set_ylabel('Intensity')

        # plt.suptitle(flnm)
        plt.tight_layout()
        plt.savefig('{sv}\\{flnm}_hkl.png'.format(sv=save_path, flnm=flnm))
