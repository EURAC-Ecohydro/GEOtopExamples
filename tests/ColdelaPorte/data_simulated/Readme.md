# Simulations of Col de la Porte test site

- GEOtop v3.0 simulations for paper GEotop v3.0
- Authors: E Bortoli G Bertoldi
- Date: July 2019

Simulations to replicate Col de la Porte Test case of Paper Endrizzi 2014.

Base simulations: test case Col de la Porte

Meteo data and observations: updated with data frm paper: Morin, S., Lejeune, Y., Lesaffre, B., Panel, J.-M., Poncet, D., David, P., Sudul, M., 2012. A 18-yr long (1993–2011) snow and meteorological dataset from a mid-altitude mountain site (Col de Porte, France, 1325 m alt.) for driving and evaluating snowpack models. Earth Syst. Sci. Data Discuss. 5, 29–45. https://doi.org/10.5194/essdd-5-29-2012

## sim_1
- Purpose: fix snow depth
- corrected snow correction factor =1
- corrected latitude and longitude

### Results
-   the snow height is too low

--------------------------------------------------------------------------------
## sim_2
- changed the following soil parameters (previously all equal to 0):
```
VegHeight      = 400
LSAI           = 4
CanopyFraction = 1
RootDepth      = 150
```

### Results
- the snow height is too low

--------------------------------------------------------------------------------
## sim_3
- as sim_2 but different start and end date of the simulation to initialize the model
```
InitDateDDMMYYYYhhmm   = 01/01/1997 00:00
EndDateDDMMYYYYhhmm    = 01/01/2003 00:00
```
- corrected the NaN value in meteo data (previously -9999999, now -9999)

### Results
- the snow height is too low

--------------------------------------------------------------------------------
## sim_4
- as sim_3 but
  - input data from Morin paper (2012, essd)
  - shorter simulated period
  ```
  InitDateDDMMYYYYhhmm   = 21/09/2001 00:00
  EndDateDDMMYYYYhhmm    = 10/04/2002 00:00
  ```
  
### Results
- the simulated value are reasonable and ~ in according to the observed ones
- maybe a spin up is needed for the soil temperature (first values are too low)

--------------------------------------------------------------------------------
## sim_5
- as sim_4 but ```TimeStepEnergyAndWater = 900```

### Results
- better results than sim_4 (reference case)

--------------------------------------------------------------------------------
## sim_6
- as sim_5 but ```TimeStepEnergyAndWater = 300```

### Results
- worse than sim_5, ~ sim_4

--------------------------------------------------------------------------------
## sim_7
- as sim_5 but
```
ThresTempRain           =  1
ThresTempSnow           =  0
```

### Results
- lower Hsnow and SWE than sim_5

--------------------------------------------------------------------------------
## sim_8
- as sim_5 but commented keyword
```
!SnowDensityCutoff      = 100
```

### Results
- nothing changes compared to sim_5
--------------------------------------------------------------------------------