
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std

from scipy.stats import shapiro

from statsmodels.graphics.gofplots import qqplot

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot

# Reference: https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/

# seed the random number generator
seed(1)
# Generate Normal distribution data
# For random samples from N(\mu, \sigma^2), use:
# sigma * np.random.randn(...) + mu
data = 5 * randn(100) + 50

print ('data', data)
# summarize
print('mean=%.3f stdv=%.3f' % (mean(data), std(data)))

######### Histogram plot ##########

# pyplot.hist(data)
# pyplot.show()

####### Quantile-Quantile Plo t###########
#  Q-Q plot, or QQ plot
# qqplot(data, line='s')
# pyplot.show()

####### Sharipo-Wilk Normality Test #######

stat, p = shapiro(data)

print('Statistics=%.3f, p-value=%.3f', stat, p)
# Interpret
alpha = 0.05
if p > alpha:
    print('Sample looks Gaussian (fail to reject H0(null-hypothesis))')
else:
    print('Sample doesnot look like Gaussian(reject H0)')