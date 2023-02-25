#%%
#========= Import Packages =======#

# OS = Operating System
import os
# Data Handling
import pandas as pd
# Plotting
import matplotlib.pyplot as plt

#%%

#====== Select Directory =========#
hfr_dir = f'../Demo-Repository/Example_HFR_Data'
for i in os.listdir(hfr_dir):
    print(i)

# %%

#====== Loop through Folder ======#
for i, file in enumerate(os.listdir(hfr_dir)):
    
    #======== Load HFR Data ==========#
    temp_hfr_df = pd.read_csv(f'{hfr_dir}/{file}')

    #======= Define Variables ========#
    J = temp_hfr_df['Current Density (A/cm2)']
    V = temp_hfr_df['Potential (V)']
    HFR = temp_hfr_df['HFR (Ωcm2)']

    #====== Perform Calculation ======#
    V_HFR_free = V - J * HFR

    #====== Plot Calculation =========#
    plt.semilogx(J, V_HFR_free, 'o', mfc='none', label = file)
    plt.xlabel('HFR-free Voltage (V)')
    plt.ylabel('Current Density (A/cm$^2$)')
    plt.grid(alpha=0.35)
    plt.legend()
# %%
