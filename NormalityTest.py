
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import std

from matplotlib import pyplot

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

pyplot.hist(data)
pyplot.show()

