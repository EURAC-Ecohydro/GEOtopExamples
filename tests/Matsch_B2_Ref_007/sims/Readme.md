# Simulations of B2 test site

## sim_1
- input meteo data found at: https://raw.githubusercontent.com/geotopmodel/geotop/master/tests/1D/Matsch_B2_Ref_007/meteo0001.txt

### Results
- Htot:     sim > obs (diff ~ 300 W/m2 => 50%)
- LEtot:    sim > obs (diff ~ 100 W/m2 => 17%)
- Pcum:     sim < obs (diff ~ 666 mm/6y = 111 mm/y => 15%)
- RH:       sim ~ obs (except error in obs => very negative value)
- SWC_5cm:  sim < obs (diff ~ 0.2 => 50%)
- SWC_20cm: sim < obs (diff ~ 0.2 => 50%)
- SWin:     sim > obs (diff ~ 50-100 W/m2 => 5-10%)
- Tair:     sim ~ obs (except missing data in obs)
- Wd: 	    sim ~ obs (except that 360° in sim = 0° in obs)
- Ws: 	    sim ~ obs 

## To do
- check the obs values (they are shifted + missing data)

----------------------------------------------------------------------------------------------------------------------------------
## sim_2
- input meteo data (theoretically modified by Michele Bottazzi) found at: https://github.com/EURAC-Ecohydro/MonaLisa/blob/master/geotop/1D/Matsch_B2_Optim_001/meteoB2_irr_0001.txt
- observed values backward shifted of 1 day and 1 hour
  - start before: 02/10/2009 01:00
  - start now:    01/10/2009 00:00
  
### Results
- Htot:     sim > obs (diff ~ 200 W/m2 => 30%) => better than sim_1
- LEtot:    sim > obs (diff ~ 100 W/m2 => 17% but strange peaks in the sim) => as sim_1
- Pcum:     sim < obs (diff ~ 250 mm/6y = 42 mm/y => 6%) => better than sim_1
- RH:       sim ~ obs (except error in sim (peaks)) => better than sim_1
- SWC_5cm:  sim < obs (diff ~ 0.2 => 50%) => slightly better than sim_1 BUT problems
- SWC_20cm: sim < obs (diff ~ 0.2 => 50%) => worse than sim_1 BUT problems
- SWin:     sim > obs (diff ~ 200 W/m2 => 15%) => better than sim_1
- Tair:     sim ~ obs  => better than sim_1
- Wd: 	    sim ~ obs (except that 360° in sim = 0° in obs) => better than sim_1
- Ws: 	    sim ~ obs => better than sim_1

----------------------------------------------------------------------------------------------------------------------------------
## sim_3
- same input meteo of the post-lauream trainee found in hpcgeo01 at: /shared/data2/Simulations/Muntatschini_Elisa/1D/Matsch_B2_Ref_007.zip
- plot only on the period:
  - start: 10/04/2014 
  - end:   31/12/2015
  
### Results
- SWC values are too LOW but similar to the  previous ones
----------------------------------------------------------------------------------------------------------------------------------
## sim_4
- same as sim_3 but with dynamic vegetation file

### Results
- higher SWC values

----------------------------------------------------------------------------------------------------------------------------------
## sim_5
- same as sim_2 (input meteo corrected) but with dynamic vegetation file

### Results
- even higher SWC values (better match with the measured values)

----------------------------------------------------------------------------------------------------------------------------------
## sim_6
- same as sim_5 but RootDepth = 15 cm (set in dynamic vegetation file)

### Results
- ..
- nothing changes (image comparison checked at command line)
----------------------------------------------------------------------------------------------------------------------------------
