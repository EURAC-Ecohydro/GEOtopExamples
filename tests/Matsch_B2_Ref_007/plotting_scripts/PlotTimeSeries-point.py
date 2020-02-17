# Analyse GEOtop output time series
# - point*.txt
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

# Set working paths of the simulation
try:
    sim_path = sys.argv[1]
except:
    print("Enter the absolute path of the simulation folder!")
    sys.exit(1)  # abort
    
# Read in list of files
point_path = sim_path + r"/output-tabs/"

# Select only point0*.txt files
os.chdir(point_path)
unsorted_point_files = glob.glob("point0*.txt")

# Sort in alphabetical order files
point_files = sorted(unsorted_point_files, key=str.lower)

# Imports files into pandas dataframe
appended_data = []
for j,trace in enumerate(point_files):
    filepath = os.path.join(point_path, trace)
    traces_series = pd.read_csv(filepath,
                                parse_dates = ['Date12[DDMMYYYYhhmm]'], # Date format is correct
                                index_col = ['Date12[DDMMYYYYhhmm]'], # No more element indexes
                                dayfirst = True, # Coherent date format
                                na_values=['-9999']) # NaN 
    appended_data.append(traces_series)

# Plot the desired parameter
for i in range(0,len(point_files)):
    mydata = appended_data[i]
# LE 
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['LE[W/m2]'], color = 'black')
    plt.plot(mydata.index, mydata['LEv[W/m2]'], color = 'green')
    plt.plot(mydata.index, mydata['LEup[W/m2]'], color = 'blue')
    plt.plot(mydata.index, mydata['LEg_veg[W/m2]'], color = 'orange')
    plt.plot(mydata.index, mydata['LEg_unveg[W/m2]'], color = 'magenta')
    plt.xticks(rotation=45)
    plt.ylim(-100,700)
    plt.legend(['LE', 'LEv', 'LEup', 'LEg_veg','LEg_unveg'])
    plt.ylabel("Flux [W/m2]")
    plt.title("Latent Heat fluxes")
    plt.tight_layout()
    plt.savefig(os.path.join(point_path, "%s_LE.png" % point_files[i]))
    
# Temperatures
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['Tair[C]'], color = 'black')
    plt.plot(mydata.index, mydata['Tsurface[C]'], color = 'green')
    plt.plot(mydata.index, mydata['Tvegetation[C]'], color = 'blue')
    plt.plot(mydata.index, mydata['Tcanopyair[C]'], color = 'red')
    plt.xticks(rotation=45)
    plt.ylim(-30,50)
    plt.legend(['Tair', 'Tsurface', 'Tvegetation', 'Tcanopyair'])
    plt.ylabel("T [°C]")
    plt.title("Temperatures")
    plt.tight_layout()
    plt.savefig(os.path.join(point_path, "%s_Tall.png" % point_files[i]))

# Meteo Input
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['Tair[C]'], color = 'black')
    plt.plot(mydata.index, mydata['Tdew[C]'], color = 'green')
    plt.xticks(rotation=45)
    plt.ylim(-30,50)
    plt.legend(['Tair', 'Tdew'])
    plt.ylabel("T [°C]")
    plt.title("Temperatures")
    plt.tight_layout()
    plt.savefig(os.path.join(point_path, "%s_TairTdew.png" % point_files[i]))
    # -----------------------------------------------------------------------------------------------
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['Wind_speed[m/s]'], color = 'blue')
    plt.xticks(rotation=45)
    plt.ylim(-1,20)
    plt.ylabel("Wind Speed [m/s]")
    plt.title("Wind Speed")
    plt.tight_layout()
    plt.savefig(os.path.join(point_path, "%s_WindSpeed.png" % point_files[i]))
    # -----------------------------------------------------------------------------------------------
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['Relative_Humidity[-]'], color = 'orange')
    plt.xticks(rotation=45)
    plt.ylim(-0.05,1.35)
    plt.ylabel("Relative Humidity [-]")
    plt.title("Relative Humidity")
    plt.tight_layout()
    plt.savefig(os.path.join(point_path, "%s_RH.png" % point_files[i]))

# Short Wave Radiation
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['SWin[W/m2]'], color = 'black')
    plt.plot(mydata.index, mydata['SWv[W/m2]'], color = 'green')
    plt.plot(mydata.index, mydata['SWnet[W/m2]'], color = 'orange')
    plt.plot(mydata.index, mydata['SWup[W/m2]'], color = 'blue')
    plt.xticks(rotation=45)
    plt.ylim(-100,1000)
    plt.legend(['SWin', 'SWv','SWnet','SWup']) 
    plt.ylabel("SW [W/m2]")
    plt.title("Short Wave radiation")
    plt.tight_layout()
    plt.savefig(os.path.join(point_path, "%s_SW.png" % point_files[i]))

# SWin partitioning
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['SWin[W/m2]'], color = 'black')
    plt.plot(mydata.index, mydata['SWbeam[W/m2]'], color = 'green')
    plt.plot(mydata.index, mydata['SWdiff[W/m2]'], color = 'orange')
    plt.xticks(rotation=45)
    plt.ylim(-100,1000)
    plt.legend(['SWin', 'SWbeam','SWdiff'])
    plt.ylabel("SW [W/m2]")
    plt.title("SWin partitioning")
    plt.tight_layout()
    plt.savefig(os.path.join(point_path, "%s_SWin_partitioning.png" % point_files[i]))

# Long Wave radiation
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['LWup[W/m2]'], color = 'black')
    plt.plot(mydata.index, mydata['LWin[W/m2]'], color = 'blue')
    plt.plot(mydata.index, mydata['LWnet[W/m2]'], color = 'orange')
    plt.plot(mydata.index, mydata['LWv[W/m2]'], color = 'green')
    plt.plot(mydata.index, mydata['LWin[W/m2]']-mydata['LWup[W/m2]'], color = 'red')
    plt.xticks(rotation=45)
    plt.ylim(-300,700)
    plt.legend(['LWup', 'LWin','LWnet','LWv','LWin-LWup'])
    plt.ylabel("LW [W/m2]")
    plt.title("Long Wave radiation")
    plt.tight_layout()
    plt.savefig(os.path.join(point_path, "%s_LW.png" % point_files[i]))

# Energy balance at the soil/snow surface
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['SWnet[W/m2]'], color = 'black')
    plt.plot(mydata.index, mydata['LE[W/m2]'], color = 'green')
    plt.plot(mydata.index, mydata['H[W/m2]'], color = 'orange')
    plt.plot(mydata.index, mydata['LWnet[W/m2]'], color = 'blue')
    plt.xticks(rotation=45)
    plt.ylim(-200,500)
    plt.legend(['SWnet', 'LE','H','LWnet'])
    plt.ylabel("Energy balance fluxes [W/m2]")
    plt.title("Energy balance fluxes")
    plt.tight_layout()
    plt.savefig(os.path.join(point_path, "%s_Ebalance.png" % point_files[i]))
    # -----------------------------------------------------------------------------------------------
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['Surface_Energy_balance[W/m2]'], color = 'red')
    plt.xticks(rotation=45)
    plt.ylim(-200,400)
    plt.title("Energy balance at the soil/snow surface")
    plt.ylabel("Surface Energy balance [W/m2]")
    plt.title("Surface Energy balance")
    plt.tight_layout()
    plt.savefig(os.path.join(point_path, "%s_EbalanceSurface.png" % point_files[i]))
    # -----------------------------------------------------------------------------------------------

# Water tables
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, mydata['lowest_water_table_depth[mm]'], color = 'green')
    plt.plot(mydata.index, mydata['highest_water_table_depth[mm]'], color = 'black')
    plt.xticks(rotation=45)
    plt.ylim(-100,1100)
    plt.legend(['lowest_water_table_depth', 'highest_water_table_depth'])
    plt.title("Water table depth")
    plt.ylabel("Depth [mm]")
    plt.title("Water tables")
    plt.tight_layout()
    plt.savefig(os.path.join(point_path, "%s_WaterTable.png" % point_files[i]))

# Input/Output fluxes
    plt.figure(figsize = (10,3))
    plt.plot(mydata.index, (mydata['Prain_over_canopy[mm]']+mydata['Psnow_over_canopy[mm]']).cumsum(),
             color = 'blue')
    plt.plot(mydata.index, mydata['Evap_surface[mm]']+mydata['Trasp_canopy[mm]'].cumsum(), 
             color = 'red')
    plt.xticks(rotation=45)
    plt.ylim(-10,4000)
    plt.legend(['(Prain+Psnow) above canopy','Evap+Transp'])
    plt.title("Fluxes")
    plt.ylabel("Height [mm]")
    plt.title("Precipitation vs ET")
    plt.tight_layout()
    plt.savefig(os.path.join(point_path, "%s_Prec-ET.png" % point_files[i]))
    plt.close('all')
