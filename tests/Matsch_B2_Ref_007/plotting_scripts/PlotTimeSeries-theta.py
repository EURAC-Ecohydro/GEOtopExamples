# Analyse GEOtop output time series
# - thetaliq
# - thetaice
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

# Read in list of files
path = sim_path + r"/output-tabs/"

# (a) thetaliq0001.txt
# Select only thetaliq*.txt files
os.chdir(path)
unsorted_thetaliq_files = glob.glob("thetaliq*.txt")

# Sort in alphabetical order files
thetaliq_files = sorted(unsorted_thetaliq_files, key=str.lower)

# Imports files into pandas dataframe
appended_data = []
for j,trace in enumerate(thetaliq_files):
    filepath = os.path.join(path, trace)
    traces_series = pd.read_csv(filepath,
                                parse_dates = ['Date12[DDMMYYYYhhmm]'], # Date format is correct
                                index_col = ['Date12[DDMMYYYYhhmm]'], # No more element indexes
                                dayfirst = True) # Coherent date format
#                                na_values=['-9999']) # NaN 
    appended_data.append(traces_series)

# Plot data
for i in range(0,len(thetaliq_files)):
    mydata = appended_data[i]
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['40.000000 '], color = 'orange')
    plt.plot(mydata.index, mydata['60.000000 '], color = 'blue')
    plt.plot(mydata.index, mydata['175.000000 '], color = 'red')
    plt.plot(mydata.index, mydata['225.000000 '], color = 'green')

    # rotate tick labels
    plt.xticks(rotation=45)
    plt.ylim(0,0.6)
    plt.legend(['4.0 cm', '6.0 cm', '8.5 cm', '12.5 cm', '17.5 cm', '22.5 cm'])
    plt.ylabel("thetaliq [-]")
    plt.title("Theta liq")
    plt.tight_layout()
    plt.savefig(os.path.join(path, "%s.png" % thetaliq_files[i]))
    plt.close('all')

# (b) thetaice
# Select only thetaliq*.txt files
os.chdir(path)
unsorted_thetaice_files = glob.glob("thetaice*.txt")

# Sort in alphabetical order files
thetaice_files = sorted(unsorted_thetaice_files, key=str.lower)

# Imports files into pandas dataframe
appended_data = []
for j,trace in enumerate(thetaice_files):
    filepath = os.path.join(path, trace)
    traces_series = pd.read_csv(filepath,
                                parse_dates = ['Date12[DDMMYYYYhhmm]'], # Date format is correct
                                index_col = ['Date12[DDMMYYYYhhmm]'], # No more element indexes
                                dayfirst = True) # Coherent date format
#                                na_values=['-9999']) # NaN 
    appended_data.append(traces_series)

# Plot data
for i in range(0,len(thetaice_files)):
    mydata = appended_data[i]
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['40.000000 '], color = 'orange')
    plt.plot(mydata.index, mydata['60.000000 '], color = 'blue')
    plt.plot(mydata.index, mydata['175.000000 '], color = 'red')
    plt.plot(mydata.index, mydata['225.000000 '], color = 'green')

    # rotate tick labels
    plt.xticks(rotation=45)
    plt.ylim(0,0.6)
    plt.legend(['4.0 cm', '6.0 cm', '8.5 cm', '12.5 cm', '17.5 cm', '22.5 cm'])
    plt.ylabel("thetaice [-]")
    plt.title("Theta ice")
    plt.tight_layout()
    plt.savefig(os.path.join(path, "%s.png" % thetaice_files[i]))
    plt.close('all')

