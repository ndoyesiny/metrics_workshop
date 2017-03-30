# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 17:54:19 2017
Seasonal average Tmin
@author: siny
"""



import iris
#import numpy as np
#import scipy as sci
#import matplotlib.pyplot as plt
import iris.coord_categorisation

#Here we load CMIP5 data

import load_file_names_CMIP5
import load_data
import plot_FuncTrange #to plot map




def calc_Mean_diurnal_T_range():
    
    print "Here we calculate Mean diurnal T range (over period)"
    # Here we define some parameter and variable
    variable = 'tasmin'
    scenario = 'historical'
    bc_and_resolution= 'BC_0.5x0.5'
    season = 'full_year'
    region = 'SAHEL'
    outpath= '/home/siny/these/PYTHON/metrics_workshop/Si_Nd/example_code/Figures_CMIP5'


    files_good, modelID = load_file_names_CMIP5.load_file_names_CMIP5(variable,scenario,bc_and_resolution )    
    file=files_good[1]
    cubeTmin = load_data.load_data(file,-20,20,8,20)
    print cubeTmin


    nme=modelID[1]

    ncfile= outpath+'/'+ str(scenario)+'_'+ str(variable)+'_'+ str(bc_and_resolution)+'_'+ str(nme)+'_'+str(season)+'_'+str(region)+'.nc'
    figpath=outpath+'/'+ str(scenario)+'_'+ str(variable)+'_'+ str(bc_and_resolution)+'_'+ str(nme)+'_'+str(season)+'_'+str(region)+'/'
    
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
        iris.save(Tdrange,ncfile)
        
    return (Tdrange, Tmdrange, Tyrange)
    
    
# if __name__ == "__calc_Mean_diurnal_T_range__":
if __name__ == "__main__":
    calc_Mean_diurnal_T_range()     
  
#    calc_Mean_diurnal_T_range()   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    