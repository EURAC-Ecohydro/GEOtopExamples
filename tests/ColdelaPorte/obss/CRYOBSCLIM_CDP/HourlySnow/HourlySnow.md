# Hourly Snow 
## CDP_hourly_19930801_20170731.nc
```
netcdf CDP_hourly_19930801_20170731 {
dimensions:
	time = UNLIMITED ; // (210384 currently)
variables:
	int time(time) ;
		time:units = "seconds since 1960-8-1 00:00:00" ;
	double Soil_temperature_10cm(time) ;
		Soil_temperature_10cm:_FillValue = -9999999. ;
		Soil_temperature_10cm:units = "K" ;
	double Soil_temperature_20cm(time) ;
		Soil_temperature_20cm:_FillValue = -9999999. ;
		Soil_temperature_20cm:units = "K" ;
	double Soil_temperature_50cm(time) ;
		Soil_temperature_50cm:_FillValue = -9999999. ;
		Soil_temperature_50cm:units = "K" ;
	double Runoff_5m2(time) ;
		Runoff_5m2:_FillValue = -9999999. ;
		Runoff_5m2:units = "Kg m-2 h-1" ;
	double Runoff_1m2(time) ;
		Runoff_1m2:_FillValue = -9999999. ;
		Runoff_1m2:units = "Kg m-2 h-1" ;
	double Snow_depth(time) ;
		Snow_depth:_FillValue = -9999999. ;
		Snow_depth:units = "cm" ;
	double Surface_temperature(time) ;
		Surface_temperature:_FillValue = -9999999. ;
		Surface_temperature:units = "K" ;
	double Ground_flux_1(time) ;
		Ground_flux_1:_FillValue = -9999999. ;
		Ground_flux_1:units = "W m-2" ;
	double Ground_flux_2(time) ;
		Ground_flux_2:_FillValue = -9999999. ;
		Ground_flux_2:units = "W m-2" ;
	double Ground_flux_3(time) ;
		Ground_flux_3:_FillValue = -9999999. ;
		Ground_flux_3:units = "W m-2" ;
	double Settling_disks_height_1(time) ;
		Settling_disks_height_1:_FillValue = -9999999. ;
		Settling_disks_height_1:units = "m" ;
	double Settling_disks_height_2(time) ;
		Settling_disks_height_2:_FillValue = -9999999. ;
		Settling_disks_height_2:units = "m" ;
	double Settling_disks_height_3(time) ;
		Settling_disks_height_3:_FillValue = -9999999. ;
		Settling_disks_height_3:units = "m" ;
	double Settling_disks_height_4(time) ;
		Settling_disks_height_4:_FillValue = -9999999. ;
		Settling_disks_height_4:units = "m" ;
	double Settling_disks_height_5(time) ;
		Settling_disks_height_5:_FillValue = -9999999. ;
		Settling_disks_height_5:units = "m" ;
	double Settling_disks_height_6(time) ;
		Settling_disks_height_6:_FillValue = -9999999. ;
		Settling_disks_height_6:units = "m" ;
	double Settling_disks_height_7(time) ;
		Settling_disks_height_7:_FillValue = -9999999. ;
		Settling_disks_height_7:units = "m" ;
	double Settling_disks_height_8(time) ;
		Settling_disks_height_8:_FillValue = -9999999. ;
		Settling_disks_height_8:units = "m" ;
	double Settling_disks_height_9(time) ;
		Settling_disks_height_9:_FillValue = -9999999. ;
		Settling_disks_height_9:units = "m" ;
	double Settling_disks_height_10(time) ;
		Settling_disks_height_10:_FillValue = -9999999. ;
		Settling_disks_height_10:units = "m" ;
	double Settling_disks_height_11(time) ;
		Settling_disks_height_11:_FillValue = -9999999. ;
		Settling_disks_height_11:units = "m" ;
	double Settling_disks_height_12(time) ;
		Settling_disks_height_12:_FillValue = -9999999. ;
		Settling_disks_height_12:units = "m" ;
	double Settling_disks_height_13(time) ;
		Settling_disks_height_13:_FillValue = -9999999. ;
		Settling_disks_height_13:units = "m" ;
	double Settling_disks_height_14(time) ;
		Settling_disks_height_14:_FillValue = -9999999. ;
		Settling_disks_height_14:units = "m" ;
	double Settling_disks_height_15(time) ;
		Settling_disks_height_15:_FillValue = -9999999. ;
		Settling_disks_height_15:units = "m" ;
	double Settling_disks_height_16(time) ;
		Settling_disks_height_16:_FillValue = -9999999. ;
		Settling_disks_height_16:units = "m" ;
	double Settling_disks_height_17(time) ;
		Settling_disks_height_17:_FillValue = -9999999. ;
		Settling_disks_height_17:units = "m" ;
	double Settling_disks_height_18(time) ;
		Settling_disks_height_18:_FillValue = -9999999. ;
		Settling_disks_height_18:units = "m" ;
	double Settling_disks_height_19(time) ;
		Settling_disks_height_19:_FillValue = -9999999. ;
		Settling_disks_height_19:units = "m" ;
	double Settling_disks_height_20(time) ;
		Settling_disks_height_20:_FillValue = -9999999. ;
		Settling_disks_height_20:units = "m" ;
	double Settling_disks_temp_1(time) ;
		Settling_disks_temp_1:_FillValue = -9999999. ;
		Settling_disks_temp_1:units = "K" ;
	double Settling_disks_temp_2(time) ;
		Settling_disks_temp_2:_FillValue = -9999999. ;
		Settling_disks_temp_2:units = "K" ;
	double Settling_disks_temp_3(time) ;
		Settling_disks_temp_3:_FillValue = -9999999. ;
		Settling_disks_temp_3:units = "K" ;
	double Settling_disks_temp_4(time) ;
		Settling_disks_temp_4:_FillValue = -9999999. ;
		Settling_disks_temp_4:units = "K" ;
	double Settling_disks_temp_5(time) ;
		Settling_disks_temp_5:_FillValue = -9999999. ;
		Settling_disks_temp_5:units = "K" ;
	double Settling_disks_temp_6(time) ;
		Settling_disks_temp_6:_FillValue = -9999999. ;
		Settling_disks_temp_6:units = "K" ;
	double Settling_disks_temp_7(time) ;
		Settling_disks_temp_7:_FillValue = -9999999. ;
		Settling_disks_temp_7:units = "K" ;
	double Settling_disks_temp_8(time) ;
		Settling_disks_temp_8:_FillValue = -9999999. ;
		Settling_disks_temp_8:units = "K" ;
	double Settling_disks_temp_9(time) ;
		Settling_disks_temp_9:_FillValue = -9999999. ;
		Settling_disks_temp_9:units = "K" ;
	double Settling_disks_temp_10(time) ;
		Settling_disks_temp_10:_FillValue = -9999999. ;
		Settling_disks_temp_10:units = "K" ;
	double Settling_disks_temp_11(time) ;
		Settling_disks_temp_11:_FillValue = -9999999. ;
		Settling_disks_temp_11:units = "K" ;
	double Settling_disks_temp_12(time) ;
		Settling_disks_temp_12:_FillValue = -9999999. ;
		Settling_disks_temp_12:units = "K" ;
	double Settling_disks_temp_13(time) ;
		Settling_disks_temp_13:_FillValue = -9999999. ;
		Settling_disks_temp_13:units = "K" ;
	double Settling_disks_temp_14(time) ;
		Settling_disks_temp_14:_FillValue = -9999999. ;
		Settling_disks_temp_14:units = "K" ;
	double Settling_disks_temp_15(time) ;
		Settling_disks_temp_15:_FillValue = -9999999. ;
		Settling_disks_temp_15:units = "K" ;
	double Settling_disks_temp_16(time) ;
		Settling_disks_temp_16:_FillValue = -9999999. ;
		Settling_disks_temp_16:units = "K" ;
	double Settling_disks_temp_17(time) ;
		Settling_disks_temp_17:_FillValue = -9999999. ;
		Settling_disks_temp_17:units = "K" ;
	double Settling_disks_temp_18(time) ;
		Settling_disks_temp_18:_FillValue = -9999999. ;
		Settling_disks_temp_18:units = "K" ;
	double Settling_disks_temp_19(time) ;
		Settling_disks_temp_19:_FillValue = -9999999. ;
		Settling_disks_temp_19:units = "K" ;
	double Settling_disks_temp_20(time) ;
		Settling_disks_temp_20:_FillValue = -9999999. ;
		Settling_disks_temp_20:units = "K" ;
	double Soil_temperature_5cm_1(time) ;
		Soil_temperature_5cm_1:_FillValue = -9999999. ;
		Soil_temperature_5cm_1:units = "K" ;
	double Soil_temperature_5cm_2(time) ;
		Soil_temperature_5cm_2:_FillValue = -9999999. ;
		Soil_temperature_5cm_2:units = "K" ;
	double Soil_temperature_5cm_3(time) ;
		Soil_temperature_5cm_3:_FillValue = -9999999. ;
		Soil_temperature_5cm_3:units = "K" ;
	double Soil_temperature_10cm_1(time) ;
		Soil_temperature_10cm_1:_FillValue = -9999999. ;
		Soil_temperature_10cm_1:units = "K" ;
	double Soil_temperature_10cm_2(time) ;
		Soil_temperature_10cm_2:_FillValue = -9999999. ;
		Soil_temperature_10cm_2:units = "K" ;
	double Soil_temperature_10cm_3(time) ;
		Soil_temperature_10cm_3:_FillValue = -9999999. ;
		Soil_temperature_10cm_3:units = "K" ;
	double Soil_temperature_20cm_1(time) ;
		Soil_temperature_20cm_1:_FillValue = -9999999. ;
		Soil_temperature_20cm_1:units = "K" ;
	double Soil_temperature_20cm_2(time) ;
		Soil_temperature_20cm_2:_FillValue = -9999999. ;
		Soil_temperature_20cm_2:units = "K" ;
	double Soil_temperature_30cm_1(time) ;
		Soil_temperature_30cm_1:_FillValue = -9999999. ;
		Soil_temperature_30cm_1:units = "K" ;
	double Soil_temperature_30cm_2(time) ;
		Soil_temperature_30cm_2:_FillValue = -9999999. ;
		Soil_temperature_30cm_2:units = "K" ;
	double Soil_moisture_5cm_1(time) ;
		Soil_moisture_5cm_1:_FillValue = -9999999. ;
		Soil_moisture_5cm_1:units = "m3 m-3" ;
	double Soil_moisture_5cm_2(time) ;
		Soil_moisture_5cm_2:_FillValue = -9999999. ;
		Soil_moisture_5cm_2:units = "m3 m-3" ;
	double Soil_moisture_5cm_3(time) ;
		Soil_moisture_5cm_3:_FillValue = -9999999. ;
		Soil_moisture_5cm_3:units = "m3 m-3" ;
	double Soil_moisture_10cm_1(time) ;
		Soil_moisture_10cm_1:_FillValue = -9999999. ;
		Soil_moisture_10cm_1:units = "m3 m-3" ;
	double Soil_moisture_10cm_2(time) ;
		Soil_moisture_10cm_2:_FillValue = -9999999. ;
		Soil_moisture_10cm_2:units = "m3 m-3" ;
	double Soil_moisture_10cm_3(time) ;
		Soil_moisture_10cm_3:_FillValue = -9999999. ;
		Soil_moisture_10cm_3:units = "m3 m-3" ;
	double Soil_moisture_20cm_1(time) ;
		Soil_moisture_20cm_1:_FillValue = -9999999. ;
		Soil_moisture_20cm_1:units = "m3 m-3" ;
	double Soil_moisture_20cm_2(time) ;
		Soil_moisture_20cm_2:_FillValue = -9999999. ;
		Soil_moisture_20cm_2:units = "m3 m-3" ;
	double Soil_moisture_30cm_1(time) ;
		Soil_moisture_30cm_1:_FillValue = -9999999. ;
		Soil_moisture_30cm_1:units = "m3 m-3" ;
	double Soil_moisture_30cm_2(time) ;
		Soil_moisture_30cm_2:_FillValue = -9999999. ;
		Soil_moisture_30cm_2:units = "m3 m-3" ;
```