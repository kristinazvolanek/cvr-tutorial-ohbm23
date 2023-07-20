# -*- coding: utf-8 -*-

import numpy as np
import peakdet as pk
from matplotlib import pyplot as plt

#%% ###################################
# Change path to your local directory
######################################
# Path to sample data from CVR tutorial download. Outputs from this script will be saved here too.
path = '/Users/kzg7316/Desktop/cvr-tutorial-ohbm23/sample_data/'

#%% Import unprocessed physiological data
data = np.genfromtxt(path + 'sub-009_ses-02_task-breathhold_physio_dec.tsv.gz')

# Plot CO2 data
co2_orig = data[:,4]
plt.plot(co2_orig)
#plt.show()

# Change scale from Volts to mmHg (see https://doi.org/10.1016/j.neuroimage.2021.117914)
co2=co2_orig*71.2

# Load CO2 data (in column 4) to a peakdet Physio object
phys = pk.Physio(co2,fs=40)

# Automatically find end-tidal CO2 peaks with peakdet
# Can edit thresh or dist values for better peak detection
    # thresh: Relative height threshold (between 0 and 1) a data point must surpass to be classified as a peak. 
    #          Default: 0.2
    # dist: Distance in indices that peaks must be separated by. If None, this is estimated. 
    #          Default: None
peaks = pk.operations.peakfind_physio(phys,thresh=0.02,dist=200)

# Open GUI to manually edit peaks
peaks = pk.operations.edit_physio(peaks)

#%% Save the array of peak indices as a separate file
export_peaks = peaks.peaks
fname_pks='sub-009_ses-02_task-breathhold_physio_co2_pks.1D'
np.savetxt(path + fname_pks, export_peaks, fmt='%.18f')

# You can also save the array trough indices, but this is not needed to create end-tidal CO2 regressor
export_troughs = peaks.troughs

# Demean CO2 and save it as separate file
co2_demean = co2 - co2.mean()
fname_co2 = 'sub-009_ses-02_task-breathhold_physio_co2_demean.1D'
np.savetxt(path + fname_co2, co2_demean, fmt='%.18f')

# Save Physio object to re-load manual edits in the future
fname_physio = 'sub-009_ses-02_task-breathhold_physio_co2_manualedits'
pk.save_physio(path + fname_physio, peaks)

#%% Check re-load of peaks)
pk_check = pk.load_physio('/Users/kzg7316/Desktop/cvr-tutorial/sub-009_ses-02_task-breathhold_physio_co2_manualedits.phys', fs=40,allow_pickle=True)
pk_check.peaks
