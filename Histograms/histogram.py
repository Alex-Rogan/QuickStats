#import required libraries
import matplotlib.pyplot as plt
import numpy as np

#import data file (can use pandas for .csv files)
from histogramData import tempData #import data file from

#initialize list for celsius temperatures
tempC=[]

#convert fahrenheit data to celsius and send it to tempC list
for i in range(len(tempData)):
    tempC.append((tempData[i]-32)*5/9)
 
# Determine the ideal number of bins for a histogram (Freedman-Diaconis number)
q25, q75 = np.percentile(tempC, [25, 75])
bin_width = (2 * (q75 - q25)) * len(tempC) ** (-1/3)
binNum = (max(tempC)-min(tempC))/bin_width
print('Freedman–Diaconis number of bins:', round(binNum,None))

# Plot a histogram of the imported data
plt.hist(tempC, density=False, bins=binNum.astype(int)) #density is # vs relative, bins must be integers 
plt.show()