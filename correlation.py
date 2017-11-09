#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 06:35:53 2017

@author: danielmoreno
"""

import pandas as pd
import numpy as np
from scipy.stats.stats import pearsonr

deathsTable = pd.read_table("OpioidDeaths.txt")
prescriptionsTable = pd.read_table("prescriptions.tsv")

#exclude unnecessary columns
del deathsTable ['Notes']
del deathsTable ['Year Code']
del deathsTable ['State Code']


#include year array
year = ['2006', '2007', '2008', '2009', '2010', '2011', '2012',
         '2013', '2014', '2015', '2016',]

#array containing the relevant years
years = [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]

#totals to compute averages
totalcorr = 0
totalLC = 0
totalLCD = 0
totalLCP = 0

#arrays containing the correlations for each state
cArray = []
cArrayNum = []

#arrays containing the linear coeff. for each state deaths/time
lcdArray = []
lcdArrayNum = []

#arrays containing the linear coeff. for each state prescriptions/time
lcpArray = []
lcpArrayNum = []

#arrays containing the linear coeff. for each state deaths/prescriptions
LCArray = []
LCArrayNum = []

#gathering data for each state, adding to relevant arrays
for y in range (51):

    #prescriptions array from raw data
    stateInfo = prescriptionsTable.loc[y]
    stateName = stateInfo[0]
    statePrescriptions = stateInfo[3:14]

    prescriptionsFinal = []
    for x in range(11):
        prescriptionsFinal = prescriptionsFinal + [statePrescriptions[x]]


    #deaths array
    stateDeath = deathsTable['Crude Rate']

    deathsFinal = []

    for x in range(11): 
        deathsFinal = deathsFinal + [stateDeath.loc[y + x*52]]

    x = prescriptionsFinal
    y = deathsFinal

    #correlation between deaths and prescription
    correlation = pearsonr(x,y)[0]
    
    #m is lc for deaths/prescriptions
    m,b = np.polyfit(x,y,1)
    
    #m1 is lc for deaths/year
    m1,b1 = np.polyfit(years,y,1)
    
    #m2 is lc for prescriptions/year
    m2,b2 = np.polyfit(years,x,1)
    

    
    #print relevant information
    print ("-----" + stateName + "-----")
    print("correlation:", correlation)
    print("Linear Regression Coefficient", m)
    print("LRC Deaths", m1)
    print("LRC Prescriptions", m2)

    #adding data to totals, relevant arrays
    totalcorr = totalcorr + correlation
    cArray = cArray + [[correlation, stateName]]
    cArrayNum = cArrayNum + [correlation]
    
    totalLC = totalLC + m
    LCArray = LCArray + [[m, stateName]]
    LCArrayNum = LCArrayNum + [m]
    
    totalLCD = totalLCD + m1
    lcdArray = lcdArray+[[m1, stateName]]
    lcdArrayNum = lcdArrayNum + [m1]
    
    totalLCP = totalLCP + m2
    lcpArray = lcpArray + [[m2, stateName]]
    lcpArrayNum = lcpArrayNum + [m2]    

#Average, Max, and Min correlation and linear coefficient for all series
avgC = totalcorr/51
maxC = np.nanmax(cArrayNum)
minC = np.amin(cArrayNum)

avgLC = totalLC/51
maxLC = np.nanmax(LCArrayNum)
minLC = np.amin(LCArrayNum)

avgLCD = totalLCD/51
maxLCD = np.nanmax(lcdArrayNum)
minLCD = np.amin(lcdArrayNum)

avgLCP = totalLCP/51
maxLCP = np.nanmax(lcpArrayNum)
minLCP = np.amin(lcpArrayNum)



print('Average Correlation:', avgC)
print('Average Linear Coefficient', avgLC)

#counts for how many coefficients are positive for each array
poscountC = 0
poscountLC = 0
poscountLCP = 0
poscountLCD = 0
for n in range (51):
    if cArrayNum[n] > 0:
        poscountC= poscountC+1
    if LCArrayNum[n] > 0:
        poscountLC = poscountLC + 1
    if lcpArrayNum[n]>0:
        poscountLCP = poscountLCP +1
    if lcdArrayNum[n]>0:
        poscountLCD = poscountLCD + 1
        
#creation of arrays with states with the highest death, prescription/time lcs        
highDeathArray = []
highPrescriptionArray = []
for n in range(51):
    if lcdArrayNum[n] > .5:
        highDeathArray = highDeathArray + lcdArray[n]
    if lcpArrayNum[n] > .5:
        highPrescriptionArray = highPrescriptionArray + lcpArray[n]



