# Analyse GEOtop input time series
# - obs.txt
# 
# ---
# Author: Elisa Bortoli (elisa.bortoli3@gmail.com)
# 
# Date: 09/07/2019

# Import the necessary modules
import os 
import glob 
import sys
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.pyplot as plt

# Set working paths of the simulation
try:
    sim_path = sys.argv[1]
except:
    print("Enter the absolute path of the simulation folder!")
    sys.exit(1)  # abort
    
# (a) obs*.txt
# Read in list of files
obs_path = sim_path + r"/obs/"

# Select only obs*.txt files
os.chdir(obs_path)
unsorted_obs_files = glob.glob("obs*.txt")

# Sort in alphabetical order files
obs_files = sorted(unsorted_obs_files, key=str.lower)

# Imports files into pandas dataframe
appended_data = []
for j,trace in enumerate(obs_files):
    filepath = os.path.join(obs_path, trace)
    traces_series = pd.read_csv(filepath,
                                parse_dates = ['Date12.DDMMYYYYhhmm.'], # Date format is correct
                                index_col = ['Date12.DDMMYYYYhhmm.'], # No more element indexes
                                dayfirst = True, # Coherent date format
                                na_values=['-9999']) # NaN 
    appended_data.append(traces_series)

# Plot the desired parameter
for i in range(0,len(obs_files)):
    mydata = appended_data[i]
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['rainfall_amount'], color = 'blue')
    plt.xticks(rotation=45)
    plt.ylabel("height [mm]")
    plt.title("Rainfall")
    plt.tight_layout()
    plt.savefig(os.path.join(obs_path, "%s_Rain.png" % obs_files[i]))
    # -----------------------------------------------------------------------------------------------
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['wind_speed'], color = 'orange')
    plt.xticks(rotation=45)
    plt.ylabel("wind speed [m/s]")
    plt.title("Wind speed")
    plt.tight_layout()
    plt.savefig(os.path.join(obs_path, "%s_WS.png" % obs_files[i]))
    # -----------------------------------------------------------------------------------------------
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['wind_from_direction'], color = 'green')
    plt.xticks(rotation=45)
    plt.ylabel("direction [°]")
    plt.title("Wind direction")
    plt.tight_layout()
    plt.savefig(os.path.join(obs_path, "%s_WD.png" % obs_files[i]))
    # -----------------------------------------------------------------------------------------------
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['relative_humidity'], color = 'red')
    plt.xticks(rotation=45)
    plt.ylim(-1.5,1.5)
    plt.ylabel("RH [-]")
    plt.title("Relative Humidity")
    plt.tight_layout()
    plt.savefig(os.path.join(obs_path, "%s_RH.png" % obs_files[i]))
    # -----------------------------------------------------------------------------------------------
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['air_temperature'])
    plt.xticks(rotation=45)
    plt.ylabel("Temperature [°C]")
    plt.title("Air temperature")
    plt.tight_layout()
    plt.savefig(os.path.join(obs_path, "%s_Tair.png" % obs_files[i]))
    # -----------------------------------------------------------------------------------------------
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['surface_downwelling_shortwave_flux'],color = 'magenta')
    plt.xticks(rotation=45)
    plt.ylabel("Flux [W/m2]")
    plt.title("Surface Downwelling Shortwave Flux")
    plt.tight_layout()
    plt.savefig(os.path.join(obs_path, "%s_SW.png" % obs_files[i]))
    # -----------------------------------------------------------------------------------------------
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['soil_moisture_content_50'], color='orange')
    plt.plot(mydata.index, mydata['soil_moisture_content_200'], color = 'blue')
    plt.legend(['SMC 5 cm', 'SMC 20 cm'], bbox_to_anchor=(1.1,0.7), fontsize=13)
    plt.xticks(rotation=45)
    plt.ylabel("SMC [-]")
    plt.title("Soil Moisture Content")
    plt.tight_layout()
    plt.savefig(os.path.join(obs_path, "%s_SMC.png" % obs_files[i]))
     # -----------------------------------------------------------------------------------------------
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['latent_heat_flux_in_air'], color='red')
    plt.plot(mydata.index, mydata['sensible_heat_flux_in_air'], color = 'green')
    plt.legend(['LE', 'H'], bbox_to_anchor=(1.3,0.7), fontsize=13)
    plt.xticks(rotation=45)
    plt.ylabel("Fluxes [W/m2]")
    plt.title("Heat Fluxes in air")
    plt.tight_layout()
    plt.savefig(os.path.join(obs_path, "%s_Fluxes.png" % obs_files[i]))
    # LE: energy absorbed by or released from a substance during a phase change 
    # H : energy required to change the temperature of a substance with NO phase change

