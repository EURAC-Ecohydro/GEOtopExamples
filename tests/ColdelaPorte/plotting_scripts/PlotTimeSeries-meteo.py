# Analyse GEOtop input meteo time series
# - meteo*.txt
# 
# ---
# Author: Elisa Bortoli (elisa.bortoli3@gmail.com)
# 
# Date: 08/07/2019

# Import the necessary modules
import os 
import glob
import sys
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.pyplot as plt
import numpy as np

# Set working paths of the simulation
try:
    sim_path = sys.argv[1]
except:
    print("Enter the absolute path of the simulation folder!")
    sys.exit(1)  # abort
    
# Read in list of files
meteo_path = sim_path + r"/meteo/"

# Select only point0*.txt files
os.chdir(meteo_path)
unsorted_meteo_files = glob.glob("meteo*.txt")

# Sort in alphabetical order files
meteo_files = sorted(unsorted_meteo_files, key=str.lower)

# Imports files into pandas dataframe
appended_data = []
for j,trace in enumerate(meteo_files):
    filepath = os.path.join(meteo_path, trace)
    traces_series = pd.read_csv(filepath,
                                parse_dates = ['Date'], # Date format is correct
                                index_col = ['Date'], # No more element indexes
                                dayfirst = True, # Coherent date format
                                na_values=['-9999999']) # NaN 
    appended_data.append(traces_series)
    
# Plot the desired parameter
# Date,JDfrom0,Iprec,WindSp,WindDir,RelHum,AirT,SWglobal,CloudTrans
for i in range(0,len(meteo_files)):
    mydata = appended_data[i]
    # mydata = appended_data[i].dropna() # to delete all the lines containing NaN
    # -----------------------------------------------------------------------------------------------
    if 'Prec' in mydata.columns:
        plt.figure(figsize = (10,3))
        plt.plot(mydata.index, mydata['Prec'], color = 'blue')
        plt.xticks(rotation=45)
        plt.title("Precipitation Intensity")
        plt.ylabel("Prec [mm/h]")
        plt.tight_layout()
        plt.savefig(os.path.join(meteo_path, "%s_Prec.png" % meteo_files[i]))
    # -----------------------------------------------------------------------------------------------
    if 'Ws' in mydata.columns:
        plt.figure(figsize = (10,3))
        plt.plot(mydata.index, mydata['Ws'], color = 'magenta')
        plt.xticks(rotation=45)
        plt.title("Wind Speed")
        plt.ylabel("Wind Speed [m/s]")
        plt.tight_layout()
        plt.savefig(os.path.join(meteo_path, "%s_Ws.png" % meteo_files[i]))
    # -----------------------------------------------------------------------------------------------
    if 'Wd' in mydata.columns:
        plt.figure(figsize = (10,3))
        plt.plot(mydata.index, mydata['Wd'])
        plt.xticks(rotation=45)
        plt.title("Wind Direction")
        plt.ylabel("Wind Direction [°]")
        plt.tight_layout()
        plt.savefig(os.path.join(meteo_path, "%s_Wd.png" % meteo_files[i]))
    # -----------------------------------------------------------------------------------------------
    if 'RH' in mydata.columns:
        plt.figure(figsize = (10,3))
        plt.plot(mydata.index, mydata['RH'], color = 'orange')
        plt.xticks(rotation=45)
        plt.title("Relative Humidity")
        plt.ylabel("RH [-]")
        plt.tight_layout()
        plt.savefig(os.path.join(meteo_path, "%s_RH.png" % meteo_files[i]))
    # -----------------------------------------------------------------------------------------------
    if 'Tair' in mydata.columns:
        plt.figure(figsize = (10,3))
        plt.plot(mydata.index, mydata['Tair'], color = 'red')
        plt.xticks(rotation=45)
        plt.title("Air Temperature")
        plt.ylabel("AirT [°C]")
        plt.tight_layout()
        plt.savefig(os.path.join(meteo_path, "%s_Tair.png" % meteo_files[i]))
    # -----------------------------------------------------------------------------------------------
    if 'SW' in mydata.columns:
        plt.figure(figsize = (10,3))
        plt.plot(mydata.index, mydata['SW'], color = 'green')
        plt.xticks(rotation=45)
        plt.title("Short Wave Radiation")
        plt.ylabel("SW [W/m2]")
        plt.tight_layout()
        plt.savefig(os.path.join(meteo_path, "%s_SW.png" % meteo_files[i]))
    # -----------------------------------------------------------------------------------------------
    if 'LW' in mydata.columns:
        plt.figure(figsize = (10,3))
        plt.plot(mydata.index, mydata['LW'], color = 'green')
        plt.xticks(rotation=45)
        plt.title("Long Wave Radiation")
        plt.ylabel("LW [W/m2]")
        plt.tight_layout()
        plt.savefig(os.path.join(meteo_path, "%s_LW.png" % meteo_files[i]))
    # -----------------------------------------------------------------------------------------------
    # # All data are NaN
    # if 'CloudTrans' in mydata.columns:
    #     plt.figure(figsize = (10,3))
    #     plt.plot(mydata.index, mydata['CloudTrans'], color = 'black')
    #     plt.xticks(rotation=45)
    #     plt.ylim(0,1)
    #     plt.title("Cloud Transmissivity")
    #     plt.ylabel("CloudTrans [-]")
    #     plt.tight_layout()
    #     plt.savefig(os.path.join(meteo_path, "%s_CloudTrans.png" % meteo_files[i]))
    plt.close('all')
