#Correlations by Risheeth

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import yfinance as yf



import math

import random

def Correlation(ticks, xlist1, xlist2):
    
    diffSeries = []

    maxl1 = max(xlist1)
    maxl2 = max(xlist2)
    print("xlist1 is ", xlist1)
    print("max of xlist1 is ", maxl1)
    xlist1Norm = [x/ maxl1 for x in xlist1]
    print("Normalized xlist1 is ", xlist1Norm)
    print("xlist2 is ", xlist2)
    print("max of xlist2 is ", maxl2)
    xlist2Norm = [x/ maxl2 for x in xlist2]
    print("Normalized xlist2 is ", xlist2Norm) 

    sumDS = 0
    for i in range(len(xlist1Norm)): 
        diffSeries.append((xlist1Norm[i] - xlist2Norm[i])**2) #squares of differences
        sumDS += math.sqrt(diffSeries[i])

    print("diffSeries is ", diffSeries) 
    meanDS = sumDS/len(diffSeries)
    print("The mean of the squares is ", meanDS)
    score = (1 - meanDS)*10
    print("The sum of squares is ", sumDS)
   
    print("The score is ", score)

    


def PlotLines(ticks, xlist1, xlist2):
    fig, ax1 = plt.subplots(figsize=(12,6))

    ax1.set_xlabel('ticks')
    ax1.set_ylabel('value')
    ax1.plot(range(ticks), xlist1, xlist2)
    ax1.tick_params(axis='y')
    plt.show()

# Main function for testing
def main():
    ticks = 20
    xlist1 = []
    xlist2 = []
    for i in range(ticks):
        xlist1.append(random.randint(0,10))
        xlist2.append(random.randint(0,10))
        #j = i + 10
        #k = i + 100  
        #k = 1000 - i
        #xlist1.append(j)
        #xlist2.append(k)

    #Correlation(ticks, xlist1, xlist2) # this is main correlation test
    #Correlation(ticks, xlist1, xlist1)  # identical graph correlation test
    PlotLines(ticks, xlist1, xlist2)

if __name__=="__main__":
    main()

