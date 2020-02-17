# Analyse GEOtop output time series
# - basin.txt
# - discharge.txt
# ---
# Author: Elisa Bortoli (elisa.bortoli3@gmail.com)
# 
# Date: 08/07/2019

# Import the necessary modules
import os
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

tabs_path = sim_path + r"/output-tabs/"

# # (a) basin.txt
# basin_path = tabs_path + "basin.txt"

# # Import file into pandas dataframe, identifying the date column to be converted to datetime
# basin_df_datetime = pd.read_csv(basin_path,
#                                 parse_dates = ['Date12[DDMMYYYYhhmm]'], # Date format is correct
#                                 index_col = ['Date12[DDMMYYYYhhmm]'], # No more element indexes
#                                 dayfirst = True, # Coherent date format
#                                 na_values=['-9999']) # NaN 

# # Plot the desired parameter

# # Temperatures
# fig, ax = plt.subplots(figsize = (10,3))
# mydata = basin_df_datetime
# plt.plot(mydata.index, mydata['Tair[C]'], color = 'black')
# plt.plot(mydata.index, mydata['Tsurface[C]'], color = 'green')
# plt.plot(mydata.index, mydata['Tvegetation[C]'], color = 'blue')
# plt.setp(ax.get_xticklabels(), rotation=45)
# plt.legend(['Tair', 'Tsurface', 'Tvegetation'])
# ax.set(ylabel = "T [°C]", title = "Temperatures"); # to avoid text before the pic
# plt.tight_layout()
# plt.savefig(os.path.join(tabs_path, "basin_T.png"))
    
# # Short Wave Radiation
# fig, ax = plt.subplots(figsize = (10,3))
# mydata = basin_df_datetime
# plt.plot(mydata.index, mydata['SWin[W/m2]'], color = 'black')
# plt.plot(mydata.index, mydata['SWv[W/m2]'], color = 'green')
# plt.plot(mydata.index, mydata['SW[W/m2]'], color = 'blue')
# plt.xticks(rotation=45)
# plt.legend(['SWin', 'SWv','SW'], loc='upper right')
# plt.ylabel("SW [W/m2]")
# plt.title("Short Wave Radiation")
# plt.tight_layout()
# plt.savefig(os.path.join(tabs_path, "basin_SW.png"))

# # Long Wave radiation
# fig, ax = plt.subplots(figsize = (10,3))
# mydata = basin_df_datetime
# plt.plot(mydata.index, mydata['LWin[W/m2]'], color = 'blue')
# plt.plot(mydata.index, mydata['LWv[W/m2]'], color = 'green')
# plt.plot(mydata.index, mydata['LW[W/m2]'], color = 'orange')
# plt.xticks(rotation=45)
# plt.legend(['LWin', 'LWv','LW'])
# plt.ylabel("LW [W/m2]")
# plt.title("Long Wave Radiation")
# plt.tight_layout()
# plt.savefig(os.path.join(tabs_path, "basin_LW.png"))

# # Energy balance at the soil/snow surface
# mydata = basin_df_datetime
# plt.figure(figsize = (10,3))
# plt.plot(mydata.index, mydata['LE[W/m2]'], color = 'green')
# plt.plot(mydata.index, mydata['H[W/m2]'], color = 'orange')
# plt.xticks(rotation=45)
# plt.legend(['LE','H'])
# plt.ylabel("Fluxes [W/m2]")
# plt.title("Energy balance at the soil/snow surface")
# plt.tight_layout()
# plt.savefig(os.path.join(tabs_path, "basin_EB-fluxes.png"))
# # -----------------------------------------------------------------------------------------------
# plt.figure(figsize = (10,3))
# plt.plot(mydata.index, mydata['Mass_balance_error[mm]'], color = 'red')
# plt.xticks(rotation=45)
# plt.ylabel("Error [mm]")
# plt.title("Mass balance error")
# plt.tight_layout()
# plt.savefig(os.path.join(tabs_path, "basin_WB-error.png"))

# # Input/Output fluxes
# mydata = basin_df_datetime
# plt.figure(figsize = (10,3))
# plt.plot(mydata.index,
#          (mydata['Prain_above_canopy[mm]']+mydata['Prain_above_canopy[mm].1']).cumsum(),color = 'blue')
# plt.plot(mydata.index,
#          (mydata['Evap_surface[mm]']+mydata['Transpiration_canopy[mm]']).cumsum(), color = 'red')
# plt.xticks(rotation=45)
# plt.ylabel("Fluxes [mm]")
# plt.legend(['(Prain+Psnow) above canopy','Evap+Transp'])
# plt.title("Fluxes")
# plt.tight_layout()
# plt.savefig(os.path.join(tabs_path, "basin_Prec-ET.png"))

# (b) discharge.txt
# Read in list of files
discharge_path = tabs_path + "discharge.txt"

# Import file into pandas dataframe, identifying the date column to be converted to datetime
discharge_df_datetime = pd.read_csv(discharge_path,
                                    parse_dates = ['DATE[day/month/year hour:min]'], 
                                    index_col = ['DATE[day/month/year hour:min]'], 
                                    dayfirst = True, 
                                    na_values=['-9999'])

# Plot the desired parameter

# Discharges
mydata = discharge_df_datetime
plt.figure(figsize = (10,3))
plt.plot(mydata.index, mydata['Qtot[m3/s]'], color = 'black')
plt.plot(mydata.index, mydata['Qoutlandsup[m3/s]'], color = 'green')
plt.plot(mydata.index, mydata['Qoutlandsub[m3/s]'], color = 'blue')
plt.plot(mydata.index, mydata['Qoutbottom[m3/s]'], color = 'orange')
plt.xticks(rotation=45)
plt.legend(['Qtot', 'Qoutlandsup', 'Qoutlandsub', 'Qoutbottom'])
plt.ylabel("Q [m3/s]")
plt.tight_layout()
plt.savefig(os.path.join(tabs_path, "discharge_Q.png"))

# # Input/Output fluxes
# # Basin area
# A = 1703*10**6 # [m2]

# # Specific discharge
# q = (mydata['Qtot[m3/s]']/A)*1000
# q.head() # [m/s]

# mydata = basin_df_datetime
# plt.figure(figsize = (10,3))
# plt.plot(mydata.index, (mydata['Prain_above_canopy[mm]']+mydata['Prain_above_canopy[mm].1']).cumsum(),
#          color = 'blue')
# plt.plot(mydata.index, -((mydata['Evap_surface[mm]']+mydata['Transpiration_canopy[mm]']).cumsum()),
#          color = 'red')
# plt.plot(mydata.index, -((q*3600).cumsum()), color = 'green')
# plt.plot(mydata.index, 
#          (mydata['Prain_above_canopy[mm]']+mydata['Prain_above_canopy[mm].1']).cumsum()
#          -((mydata['Evap_surface[mm]']+mydata['Transpiration_canopy[mm]']).cumsum())
#          -((q*3600).cumsum()),
#          color = 'black')
# plt.xticks(rotation=45)
# plt.legend(['(Prain+Psnow) above canopy','Evap+Transp','Q', 'delta'])
# plt.ylabel("Height [mm]")
# plt.title("Fluxes")
# plt.tight_layout()
# plt.savefig(os.path.join(tabs_path, "discharge_Prec-ET-Q.png"))
