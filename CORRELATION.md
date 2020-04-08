
## CORRELATION OF TWO TIMESERIES

Note: any confusion on how to write python, either find it in a manual or google - you will find examples

We need a  python function that can "correlate" two graphs (or timeseries). By correlation here, we want the function to return a score. 
A higher score means they correlate better, a lower score means they correlate badly. 
  
      score = Correlate(series1, series2)  # we do not need to send x-axis as long as both series1 and series2 have identical xticks
  
 Note: The following algorithm is NOT the statistically proper way of doing correlation, 
       but we will use this simpler method and correct later
 
 Note: you can create a new python file and test this with random arrays or initializaed arrays. 
 For instance, initialization could be this:
 
      import random
      import numpy as np  #not using numpy in init, but numpy initi is easier (just google it)
      
      series1 = random.sample(xrange(500), 20)
      series2 = random.sample(xrange(500), 20)
      
 This can be done in python lists with loops or it can be done by converting lists to numpy arrays. 
 With numpy, arrays are much easier to manipulate and we can later use statistical funcions like cross-correlation. 
 A python list can be converted to numpy array simply by this:  
      nSeries1 = np.array(series1)
 if np.array is slow, then try this:
      nSeries1 = np.frombuffer(series1) 
 Now, you have to use nSeries1 rather than series1. 
  
 Rest of the algorithm is described as if it is not numpy (but you can simply use numpy instead)
 
 Here is the algorithm (routines like max and sum must be figured out if they don't exist)
  
    1. Normalize values to 0-1 range as each series may have different ranges:
      a. Find max first.  
          maxS1 = max(series1) and maxS2 = max(series2)  // you have to write your own max if not using numpy
      b. divide all elements with max:  
          series1Norm = series1/maxS1 and series2Norm = series2/max
    3. Take mean of sum square of differences (proportional ratio):
      a. Square of Differences:  By squaring, you make all differences positive numbers. But you have to make the differences proportional.
            diffSeries = (1 - series2/series1)**2 // it is actually ((series1 - series2)/series1)**2
      b. Renomralize the diffSeries - the step above may take some values above 1
            diffSeriesNorm = diffSeries/max(diffSeries) // this will reduce values back to 0 to 1
      c. Sum of squares: this reduces the array to one value    
            sumDS = sum(diffSeries)  // alternatively, you can do sum of sqrts: sum(sqrt(diffseries))
      d. Mean: bringing result back between 0 to 1
            meanDS = sumDS/len(diffSeries)
    4. score = (1 - meanDS)*10
    
    So, a score of 8 or 9 out of 10 indicates both series1 and series2 are close while a score of 0 means they are far. 
    