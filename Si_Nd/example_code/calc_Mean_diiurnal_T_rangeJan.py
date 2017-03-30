# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 12:28:37 2017

Number of days Tmax > threshold (for period). Set threshold at 34 degrees C
@author: siny
"""

import iris
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import iris.coord_categorisation


#import file
import load_file_names_CMIP5
import load_data



def variable_setter(string):

	if string == 'var':
           string = 'pr'
	if string == 'plot_type':
	   string = 'contourf_map'
	if string == 'seas':
	   string = 'mjjas'
	return(string)



if "__name__" == "__variable_setter__":
	variable_setter(string)

def main(cubeTmax,cubeTmin,season,ncfile):
    print "Here we calculate Mean diurnal T range (over period)"
    
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    