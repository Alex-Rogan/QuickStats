from histogramData import tempData
import matplotlib.pyplot as plt
import numpy as np

tempC=[]

for i in range(len(tempData)):
    tempC.append((tempData[i]-32)*5/9)
 

# Plot a histogram of the imported data
      
plt.hist(tempC, density=False, bins=10)
plt.show()

# Determine the ideal number of bins for a histogram

# q25, q75 = np.percentile(tempC, [0.25, 0.75])
# bin_width = 2 * (q75 - q25) * len(tempC) ** (-1/3)
# bins = round((tempC.max() - tempC.min()) / bin_width)
# print("Freedman–Diaconis number of bins:", bins)
# plt.hist(tempC, bins=bins);
