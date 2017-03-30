# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 18:25:01 2017
number of day Tmax superior than Threshold
@author: siny
"""


import iris
import numpy as np
#import scipy as sci
#import matplotlib.pyplot as plt
import iris.coord_categorisation

#Here we load CMIP5 data

import load_file_names_CMIP5
import load_data
import plot_FuncNd #to plot map

def calc_number_day_Tmax_sup_Ts():
    
    print "Here we calculate Mean diurnal T range (over period)"
    # Here we define some parameter and variable

    variable = 'tasmax'
    #scenario = 'historical'
    scenario = 'rcp26'
    bc_and_resolution= 'BC_0.5x0.5'
    season = 'full_year'
    region = 'SAHEL'
    outpath= '/home/siny/these/PYTHON/metrics_workshop/Si_Nd/example_code/Figures_CMIP5'


    files_good, modelID = load_file_names_CMIP5.load_file_names_CMIP5(variable,scenario,bc_and_resolution )
    
    file=files_good[2]
    cubeTmax = load_data.load_data(file,-20,20,8,20)
    print cubeTmax
    
    nme=modelID[2]

    ncfile= outpath+'/'+ str(scenario)+'_'+ str(variable)+'_'+ str(bc_and_resolution)+'_'+ str(nme)+'_'+str(season)+'_'+str(region)+'Nbr_of_days.nc'
    figpath=outpath+'_/'+ str(scenario)+'_'+ str(variable)+'_'+ str(bc_and_resolution)+'_'+ str(nme)+'_'+str(season)+'_'+str(region)+'/'
    iris.coord_categorisation.add_month_number(cubeTmax, 'time', name='month')
    iris.coord_categorisation.add_year(cubeTmax,'time',name='year')
    iris.coord_categorisation.add_day_of_year(cubeTmax,'time',name='day_of_year')
    cubeTmax.convert_units('Celsius') # convert unit
    cubeTmax.coord('latitude').guess_bounds()
    cubeTmax.coord('longitude').guess_bounds()    
    cubeplot=cubeTmax

    Temp = cubeplot.aggregated_by('year',iris.analysis.MEAN)
    tmptemp = Temp.data
    years = Temp.coord('year').points
    Nbr_of_day = np.zeros((tmptemp.shape[0],tmptemp.shape[1],tmptemp.shape[2]),float)
    for yr in years:
        yrslice = iris.Constraint(year = lambda cell: cell == yr)
        holdr = cubeplot.extract(yrslice)
        holdr = holdr.data
        Thr=34
        for x in range(0,holdr.shape[2]):
            for y in range(0,holdr.shape[1]):
                count=0
                #Here we compute the number day Tmax > Thr=34            
                for t in xrange(0, holdr.shape[0]):
                    if holdr[t,y,x] >Thr:
                        count=count+1
                print count # verify count value
                Nbr_of_day[yr-years[0],y,x]=count
                if count==0:
                 Nbr_of_day[yr-years[0],y,x]=float('NaN')
                         
    print Nbr_of_day
    Temp.data=Nbr_of_day[:]
    print Temp.data
    Nb_day=Temp
    iris.save(Nb_day,ncfile)

    for mnth in range(0,56):
        
        cube2plot_mon = Nb_day[mnth]
        title_name='Number of days / year Tmax superior at Threshold'+' '+str(scenario)+' '+ str(variable)+' '+str(bc_and_resolution)+' '+str(nme)
        print 
            #plot_Func.plot_Func(cube2plot_mon,outpath,mnth,10, xstart=-20,xend=20, ystart=8,yend=20,title_name)
        plot_FuncNd.plot_FuncNd(cube2plot_mon,figpath,mnth,10, -20,20, 8,20,title_name)
        
    print Nb_day
    iris.save(Nb_day,ncfile)

if __name__ == "__main__":
    calc_number_day_Tmax_sup_Ts()                
      
    
    
    