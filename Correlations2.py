import random
import numpy as np  #not using numpy in init, but numpy initi is easier (just google it)

#series1 = random.sample(xrange(500), 20)
#series2 = random.sample(xrange(500), 20)
series1 = np.random.rand(20)
series2 = np.random.rand(20)

def Correlate(series1, series2):
    score = Correlate(series1, series2)  # we do not need to send x-axis as long as both series1 and series2

maxS1 = max(series1) 
maxS2 = max(series2)

series1Norm = series1/maxS1 
series2Norm = series2/maxS2

diffSeries = (1 - series2/series1)**2 
# or ((series1 - series2)/series1)**2

diffSeriesNorm = diffSeries/max(diffSeries)

sumDS = sum(diffSeriesNorm)

meanDS = sumDS/len(diffSeries)

score = (1 - meanDS)*10

print(score)
print("The sum is ", sumDS)
print("The mean is ", meanDS)
print("The square of differences are ", diffSeries)
print("The remoralized version for the square of differences are ", diffSeriesNorm)
print("The max of series one is ", maxS1)
print("The max of series two is ", maxS2)
print("Series one is ", series1Norm)
print("Series two is ", series2Norm)

