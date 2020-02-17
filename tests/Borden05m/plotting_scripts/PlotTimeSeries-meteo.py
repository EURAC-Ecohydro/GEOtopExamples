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
                                na_values=['-9999']) # NaN 
    appended_data.append(traces_series)
    
# Plot the desired parameter
# Date,JDfrom0,Iprec,WindSp,WindDir,RelHum,AirT,SWglobal,CloudTrans
for i in range(0,len(meteo_files)):
    mydata = appended_data[i]
    # mydata = appended_data[i].dropna() # to delete all the lines containing NaN
    # -----------------------------------------------------------------------------------------------
    if 'Iprec' in mydata.columns:
        plt.figure(figsize = (10,3))
        plt.plot(mydata.index, mydata['Iprec'], color = 'blue')
        plt.xticks(rotation=45)
        plt.title("Precipitation Intensity")
        plt.ylabel("Iprec [mm/h]")
        plt.tight_layout()
        plt.savefig(os.path.join(meteo_path, "%s_Iprec.png" % meteo_files[i]))
    # -----------------------------------------------------------------------------------------------
    if 'WindSp' in mydata.columns:
        plt.figure(figsize = (10,3))
        plt.plot(mydata.index, mydata['WindSp'], color = 'magenta')
        plt.xticks(rotation=45)
        plt.title("Wind Speed")
        plt.ylabel("Wind Speed [m/s]")
        plt.tight_layout()
        plt.savefig(os.path.join(meteo_path, "%s_WindSp.png" % meteo_files[i]))
    # -----------------------------------------------------------------------------------------------
    if 'WindDir' in mydata.columns:
        plt.figure(figsize = (10,3))
        plt.plot(mydata.index, mydata['WindDir'])
        plt.xticks(rotation=45)
        plt.title("Wind Direction")
        plt.ylabel("Wind Direction [°]")
        plt.tight_layout()
        plt.savefig(os.path.join(meteo_path, "%s_WindDir.png" % meteo_files[i]))
    # -----------------------------------------------------------------------------------------------
    if 'RelHum' in mydata.columns:
        plt.figure(figsize = (10,3))
        plt.plot(mydata.index, mydata['RelHum'], color = 'orange')
        plt.xticks(rotation=45)
        plt.title("Relative Humidity")
        plt.ylabel("RH [-]")
        plt.tight_layout()
        plt.savefig(os.path.join(meteo_path, "%s_RH.png" % meteo_files[i]))
    # -----------------------------------------------------------------------------------------------
    if 'AirT' in mydata.columns:
        plt.figure(figsize = (10,3))
        plt.plot(mydata.index, mydata['AirT'], color = 'red')
        plt.xticks(rotation=45)
        plt.title("Air Temperature")
        plt.ylabel("AirT [°C]")
        plt.tight_layout()
        plt.savefig(os.path.join(meteo_path, "%s_AirT.png" % meteo_files[i]))
    # -----------------------------------------------------------------------------------------------
    if 'Swglobal' in mydata.columns:
        plt.figure(figsize = (10,3))
        plt.plot(mydata.index, mydata['Swglobal'], color = 'green')
        plt.xticks(rotation=45)
        plt.title("Global Short Wave Radiation")
        plt.ylabel("Swglob [W/m2]")
        plt.tight_layout()
        plt.savefig(os.path.join(meteo_path, "%s_Swglob.png" % meteo_files[i]))
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
