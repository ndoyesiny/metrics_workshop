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

def getSeasConstr(name):

    sncon = {'ann': iris.Constraint(month_number=lambda cell: 1 <= cell <= 12),
            'mj' : iris.Constraint(month_number=lambda cell: 5 <= cell <= 6),
            'jj' : iris.Constraint(month_number=lambda cell: 6 <= cell <= 7),
            'ja' : iris.Constraint(month_number=lambda cell: 7 <= cell <= 8),
            'as' : iris.Constraint(month_number=lambda cell: 8 <= cell <= 9),
            'so' : iris.Constraint(month_number=lambda cell: 9 <= cell <= 10),
            'jan' :  iris.Constraint(month_number=lambda cell: cell == 1),
            'feb' :  iris.Constraint(month_number=lambda cell: cell == 2),
            'mar' :  iris.Constraint(month_number=lambda cell: cell == 3),
            'apr' :  iris.Constraint(month_number=lambda cell: cell == 4),
            'may' :  iris.Constraint(month_number=lambda cell: cell == 5),
            'jun' :  iris.Constraint(month_number=lambda cell: cell == 6),
            'jul' :  iris.Constraint(month_number=lambda cell: cell == 7),
            'aug' :  iris.Constraint(month_number=lambda cell: cell == 8),
            'sep' :  iris.Constraint(month_number=lambda cell: cell == 9),
            'oct' :  iris.Constraint(month_number=lambda cell: cell == 10),
            'nov' :  iris.Constraint(month_number=lambda cell: cell == 11),
            'dec' :  iris.Constraint(month_number=lambda cell: cell == 12),
            'djf': iris.Constraint(month_number=lambda cell: (cell == 12) | (1 <= cell <= 2)),
            'mam': iris.Constraint(month_number=lambda cell: 3 <= cell <= 5),
            'jja': iris.Constraint(month_number=lambda cell: 6 <= cell <= 8),
            'jas': iris.Constraint(month_number=lambda cell: 7 <= cell <= 9),
            'jjas': iris.Constraint(month_number=lambda cell: 6 <= cell <= 9),
            'mjjas': iris.Constraint(month_number=lambda cell: 5<= cell<=9),		
            'son': iris.Constraint(month_number=lambda cell: 9 <= cell <= 11)
            }

    return(sncon[name])




if __name__ == "__getSeasConstr__":
   getSeasConstr(season)




def main(cubein,season,ncfile):
    print "Here we calculate the number of day Tmax > Ts"
    iris.coord_categorisation.add_month_number(cubein, 'time', name='month_number')
    iris.coord_categorisation.add_year(cubein,'time',name='year')
    iris.coord_categorisation.add_day_of_year(cubein,'time',name='day_of_year')
    cubein.convert_units('Celsius') # convert unit
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    