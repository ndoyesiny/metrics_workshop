# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 12:28:37 2017

Calcl mean diurnal T range
@author: siny
"""

import iris
#import numpy as np
#import scipy as sci
#import matplotlib.pyplot as plt
import iris.coord_categorisation

#Here we load CMIP5 data

import load_file_names
import load_data
import plot_FuncTrange #to plot map




def calc_Mean_diurnal_T_range():
    
    print "Here we calculate Mean diurnal T range (over period)"
    # Here we define some parameter and variable

    variable = 'tasmax'
    variable1 = 'tasmin'
    scenario = 'historical'
    bc_and_resolution= 'BC_0.5x0.5'
    season = 'full_year'
    region = 'SAHEL'
    outpath= '/home/siny/these/PYTHON/metrics_workshop/Si_Nd/example_code/Figures_Diurnal_T_range'


    files_good, modelID = load_file_names.load_file_names(variable,scenario,bc_and_resolution )
    files_good1, modelID1 = load_file_names.load_file_names(variable1,scenario,bc_and_resolution )
    for t in range(len(files_good)):
        
        file=files_good[t]
        cubeTmax = load_data.load_data(file,-20,20,8,20)
        print cubeTmax
        
        file1=files_good1[t]
        cubeTmin = load_data.load_data(file1,-20,20,8,20)
        print cubeTmin
        nme=modelID1[t]
        
        ncfile= outpath+'/'+ str(scenario)+'_Diurnal_Trange_'+ str(bc_and_resolution)+'_'+ str(nme)+'_'+str(season)+'_'+str(region)+'.nc'
        figpath=outpath+'/'+ str(scenario)+'_Diurnal_Trange_'+ str(bc_and_resolution)+'_'+ str(nme)+'_'+str(season)+'_'+str(region)+'/'
        iris.coord_categorisation.add_month_number(cubeTmax, 'time', name='month')
        iris.coord_categorisation.add_year(cubeTmax,'time',name='year')
        
        iris.coord_categorisation.add_day_of_year(cubeTmax,'time',name='day_of_year')
        cubeTmax.convert_units('Celsius') # convert unit
        
    
        iris.coord_categorisation.add_month_number(cubeTmin, 'time', name='month')
        iris.coord_categorisation.add_year(cubeTmin,'time',name='year')
        iris.coord_categorisation.add_day_of_year(cubeTmin,'time',name='day_of_year')
        cubeTmin.convert_units('Celsius') # convert unit    
        # Here we compute the difference between Tmax and Tmin
        Tdrange=cubeTmax-cubeTmin    
        Tmdrange = Tdrange.aggregated_by('month', iris.analysis.MEAN)
        Tyrange= Tdrange.aggregated_by('year', iris.analysis.MEAN)
        for mnth in range(0,12):
            cube2plot_mon = Tmdrange[mnth]
            title_name='monthly climatology Mean diurnal T range'+' '+str(mnth)+' '+str(scenario)+' '+ str(variable)+'-'+ str(variable1)+' '+str(bc_and_resolution)+' '+str(nme)
            print 
            #plot_Func.plot_Func(cube2plot_mon,outpath,mnth,10, xstart=-20,xend=20, ystart=8,yend=20,title_name)
            plot_FuncTrange.plot_FuncTrange(cube2plot_mon,figpath,mnth,10, -20,20, 8,20,title_name)
        #iris.save(Tdrange,ncfile)
        iris.fileformats.netcdf.save(Tdrange, ncfile, netcdf_format='NETCDF4', local_keys=None, unlimited_dimensions=[], zlib=False, complevel=4, shuffle=True, fletcher32=False, contiguous=False, chunksizes=None, endian='native', least_significant_digit=None, packing=None)
        
    return (Tdrange, Tmdrange, Tyrange)
    
    
# if __name__ == "__calc_Mean_diurnal_T_range__":
if __name__ == "__main__":
    calc_Mean_diurnal_T_range()     
  
#    calc_Mean_diurnal_T_range()   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    