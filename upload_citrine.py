"""
Created on 12/13/16

@author: fangren
"""

from pypif import pif
from pypif.obj import *
from citrination_client import CitrinationClient
import numpy as np


def file_index(index):
    """
    formatting the index of each file
    """
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)


master_file_path = '..\\..\\data\\Masterfiles\\'
master_file_name = 'Sample3_24x24_t30_master_metadata.csv'
master_file = master_file_path + master_file_name

data = np.genfromtxt(master_file, delimiter=',', skip_header = 1)

# use ROI to filter bad data
ROI = data[:, 15]
data = data[ROI > 20000]

Co = data[:,57]
Fe = data[:,58]
Zr = data[:,59]
peak_position = data[:,60]
peak_width = data[:,61]
scan_num = data[:,52].astype(int)

spectra_file_path = '..\\..\\data\\raw_1D\\'
spectra_basename = 'Sample3_24x24_t30_'
save_path = '..\\..\\data\\Json_files\\'

# one dataset
alloys = []
for i in range(len(Co)):
# for i in range(1):
    alloy = ChemicalSystem()
    spectrum_file = spectra_file_path + spectra_basename + file_index(scan_num[i]) + '_1D.csv'
    print 'Importing', spectrum_file
    spectrum = np.genfromtxt(spectrum_file, delimiter=',')
    IntAve = spectrum[:950,1]
    Qlist = spectrum[:950,0]
    IntAve = IntAve.astype(float)
    Qlist = Qlist.astype(float)
    IntAve = list(IntAve)
    Qlist = list(Qlist)
    # print IntAve, Qlist
    alloy.chemical_formula = 'Co'+str(round(Co[i],2))+'Fe'+str(round(Fe[i],2))+'Zr'+str(round(Zr[i],2))
    alloy.composition = [Composition(element='Co',ideal_atomic_percent=Co[i]),
                                   Composition(element='Fe',ideal_atomic_percent=Fe[i]),
                                   Composition(element='Zr',ideal_atomic_percent=Zr[i])]

    alloy.preparation = [ProcessStep(name = 'high power sputtering (>0.25 Angstrom/s)')]
    #alloy.preparation = [ProcessStep(name='low power sputtering (<0.07 Angstrom/s)')]

    alloy.source = Source(producer='Hattrick-Simplers Group (The University of South Carolina)')

    alloy.properties = [Property(name = 'Qchi', files = FileReference(relative_path= '/' + spectra_basename + file_index(scan_num[i]) + '_Qchi.png')),
                        Property(name = 'XRD Intensity', scalars = IntAve,
                                 conditions=[Value(name = 'Q, (Angstrom$^{-1}$)', scalars = Qlist),
                                             Value(name='Temperature', scalars='25', units='$^\\circ$C'),
                                             Value(name='Exposure time', scalars='30', units='seconds')],
                                 method = Method(instruments=(Instrument(name = 'MARCCD, 2048 pixels x 2048 pixels, 79 microns')))),
                        Property(name='Maximum intensity/average intensity', scalars= round(np.nanmax(IntAve)/np.nanmean(IntAve),2)),
                        Property(name = 'Full width half maximum (FWHM) of FSDP', scalars = round(peak_width[i],2)),
                        Property(name = 'First sharp diffraction peak (FSDP) position', scalars = round(peak_position[i],2)),
                        Property(name = 'Textured', scalars = 0)]

    # specify a unique uid for each sample
    alloy.uid = 'Co'+str(int(Co[i]))+'Fe'+str(int(Fe[i]))+'Zr'+str(int(Zr[i])) + 'high_power' + str(scan_num[i])

    #print pif.dumps(alloy, indent=4)
    alloys += [alloy]
pif.dump(alloys, open(save_path+'HiTp.json','w'))


    # # to let the system assign an ID automatically
    # response = client.create_data_set()
    # client.upload_file('temp.json',data_set_id = response.json()['id'])  # id is the dataset id
    # ID = response.json()['id']
    # IDs.append(ID)
    # print ID


    # to specify an ID to the sample:
    #client.upload_file('HiTp.json',data_set_id = ID)  # id is the folder id, each folder for 1 sample
    #print alloy.uid

