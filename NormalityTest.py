
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std

from scipy.stats import shapiro
from scipy.stats import normaltest
from scipy.stats import anderson

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

print('####### END of Shaipro #######')
####### D`Agostino's K2 Normality Test #######

agostino_stat, agostino_p = normaltest(data)
print('D-Agostino k2 Test: Statistics = %.3f, p-value=%.3f', stat, p)

#Interpret
agostino_alpha = 0.05
if agostino_p > agostino_alpha:
    print ('Looks like Gaussian distribution(fail to reject H0)')
else :
    print('Does not looks like Gaussian distribution(reject H0)')

print('####### END of Agostino #######')
####### Anderson- Darling Test ############

anderson_result = anderson(data, dist='norm')
print('Anderson Statistics: %.3f', anderson_result.statistic)

for i in range(len(anderson_result.critical_values)):
    significance_level, critical_values = anderson_result.significance_level[i], anderson_result.critical_values[i]
    if anderson_result.statistic < critical_values:
        print('%.3f: %.3f, looks like Gaussian distribution(Fail to reject H0)', significance_level, critical_values)

    else:
        print('%.3f: %.3f, NOT looks like Gaussian distribution(reject H0)', significance_level, critical_values)

print('####### END of Anderson #######')