# MetSnowDaily
## CDP_daily_data_19600801_20170731.nc
```
netcdf CDP_daily_data_19600801_20170731 {
dimensions:
	time = UNLIMITED ; // (20819 currently)
variables:
	int time(time) ;
		time:units = "seconds since 1960-8-1 00:00:00" ;
	double snow_depth_auto(time) ;
		snow_depth_auto:_FillValue = -9999999. ;
		snow_depth_auto:units = "m" ;
	double swe_auto(time) ;
		swe_auto:_FillValue = -9999999. ;
		swe_auto:units = "kg m-2" ;
	double snow_depth_pit(time) ;
		snow_depth_pit:_FillValue = -9999999. ;
		snow_depth_pit:units = "m" ;
	double snow_depth_pit_south(time) ;
		snow_depth_pit_south:_FillValue = -9999999. ;
		snow_depth_pit_south:units = "m" ;
	double snow_depth_pit_north(time) ;
		snow_depth_pit_north:_FillValue = -9999999. ;
		snow_depth_pit_north:units = "m" ;
	double swe_pit(time) ;
		swe_pit:_FillValue = -9999999. ;
		swe_pit:units = "kg m-2" ;
	double swe_pit_north(time) ;
		swe_pit_north:_FillValue = -9999999. ;
		swe_pit_north:units = "kg m-2" ;
	double swe_pit_south(time) ;
		swe_pit_south:_FillValue = -9999999. ;
		swe_pit_south:units = "kg m-2" ;
	double Tmin(time) ;
		Tmin:_FillValue = -9999999. ;
		Tmin:units = "K" ;
	double Tmax(time) ;
		Tmax:_FillValue = -9999999. ;
		Tmax:units = "K" ;
	double total_precipitation(time) ;
		total_precipitation:_FillValue = -9999999. ;
		total_precipitation:units = "kg m-2" ;
	double rain(time) ;
		rain:_FillValue = -9999999. ;
		rain:units = "kg m-2" ;
	double albedo_daily(time) ;
		albedo_daily:_FillValue = -9999999. ;
	int albedo_daily_flag(time) ;
		albedo_daily_flag:_FillValue = -9999999 ;
	double snow(time) ;
		snow:_FillValue = -9999999. ;
		snow:units = "kg m-2" ;
	double height_of_new_snow(time) ;
		height_of_new_snow:_FillValue = -9999999. ;
		height_of_new_snow:units = "m" ;
```