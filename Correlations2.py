import random
import numpy as np  #not using numpy in init, but numpy initi is easier (just google it)


def Correlate(series1, series2):
    #score = Correlate(series1, series2)  # we do not need to send x-axis as long as both series1 and series2
    maxS1 = max(series1) 
    maxS2 = max(series2)
    series1Norm = series1/maxS1 
    series2Norm = series2/maxS2
    
    diffSeriesN = (1 - series2Norm/series1Norm)**2 
    # or ((series1 - series2)/series1)**2

    diffSeriesNorm = diffSeriesN/max(diffSeriesN)

    sumDS = sum(diffSeriesNorm)

    meanDS = sumDS/len(diffSeriesNorm)

    score = (1 - meanDS)*10
    return score

#series1 = np.arange(1,20)
#series2 = series1
#series2 = 20 - np.arange(1,20)
#series1 = np.random.rand(20)
#series2 = np.random.rand(20)
#score = Correlate(series1, series2)

#print(score)


