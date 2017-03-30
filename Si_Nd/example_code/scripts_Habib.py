# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 18:57:51 2017

@author: siny
"""

tot_data = len(time)*len(lat_box)
for t  in range(len(time)):
        for k in range(len(heigh)):
                for j in range(len(lat_box)):
                        for i in range(len(lon_box)):
                            if conc_all_bin[t,k,j,i]>10 and conc_all_bin[t,k,j,i]>50:
                               count[k,i]=count[k,i]+1