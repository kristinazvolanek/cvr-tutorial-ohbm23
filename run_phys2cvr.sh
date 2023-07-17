#!/bin/sh


###############################################################################
##################  Define directories and phys2cvr inputs  ###################
###############################################################################

# Directories
inputdir="/Users/kzg7316/Desktop/cvr-tutorial-ohbm23/sample_data"
outputdir="/Users/kzg7316/Desktop/cvr-tutorial-ohbm23/phys2cvr_outputs"

# Phys2cvr inputs
fname_func="${inputdir}/00.sub-009_ses-02_task-breathhold_optcom_bold_native_preprocessed.nii.gz"
fname_brain_mask="${inputdir}/sub-009_brain_mask_native.nii.gz"
fname_GM_mask="${inputdir}/sub-009_GM_native.nii.gz" #to be used as the "ROI"
TR=1.5 
fname_co2="${inputdir}/sub-009_ses-02_task-breathhold_physio_co2_demean.1D"
fname_co2_pks="${inputdir}/sub-009_ses-02_task-breathhold_physio_co2_pks.1D"
freq=40 #frequency of CO2 recording
legendre_degree=4
fname_mot="${inputdir}/sub-009_ses-02_task-breathhold_echo-1_bold_mcf_demean.par"
scale_factor=0.01 # converts BOLD to %BOLD (factor that betas are DIVIDED by, so inverse of multiplying numerator by 100)
lag_max=9
lag_step=0.3


###############################################################################
###############################  Run phys2cvr  ################################
###############################################################################

phys2cvr -i ${fname_func} -o ${outputdir} -m ${fname_brain_mask} -r ${fname_GM_mask} -tr ${TR} \
-co2 ${fname_co2} -pk ${fname_co2_pks} -fr ${freq} -ldeg ${legendre_degree} -dmat ${fname_mot} \
-scale ${scale_factor} -lm ${lag_max} -ls ${lag_step}