#%%
#========= Import Packages =======#

# OS = Operating System
import os
# Data Handling
import pandas as pd
# Plotting
import matplotlib.pyplot as plt

#======== Define Formatting =======#
markers = ['v', 's', 'd', 'h', 'o']

#%%

#====== Select Directory =========#
exp_dir = f'../Demo-Repository/HFR_Data'
for i in os.listdir(exp_dir):
    print(i)


#%%

#====== Select Directory =========#
hfr_dir = f'../Demo-Repository/HFR_Data'
for i in os.listdir(hfr_dir):
    print(i)

# %%

for j, experiment in enumerate(os.listdir(exp_dir)):
    #====== Select HFR Directory ====#
    hfr_dir = f'{exp_dir}/{experiment}'

    #====== Loop through Folder ======#
    for i, hfr_file in enumerate(os.listdir(hfr_dir)):
        
        #======== Load HFR Data ==========#
        temp_hfr_df = pd.read_csv(f'{hfr_dir}/{hfr_file}')

        #======= Define Variables ========#
        J = temp_hfr_df['Current Density (A/cm2)']
        V = temp_hfr_df['Potential (V)']
        HFR = temp_hfr_df['HFR (Ωcm2)']

        #====== Perform Calculation ======#
        V_HFR_free = V - J * HFR

        #====== Plot Calculation =========#
        plt.figure(experiment)
        plt.semilogx(J, V_HFR_free, ls = 'none', marker = markers[i], mfc='none', label = hfr_file)
        plt.xlabel('HFR-free Voltage (V)')
        plt.ylabel('Current Density (A/cm$^2$)')
        plt.title(experiment)
        plt.grid(alpha=0.35)
        plt.legend()