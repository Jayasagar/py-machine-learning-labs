# generate gaussian data
import numpy as np

# seed the random number generator
np.random.seed(1)
# generate univariate observations
data = 5 * np.random.randn(100) + 50
# summarize
print('mean=%.3f stdv=%.3f' % (np.mean(data), np.std(data)))
