# generate gaussian data
import numpy as np

# seed the random number generator
np.random.seed(1)
# Generate Normal distribution data
# For random samples from N(\mu, \sigma^2), use:
# sigma * np.random.randn(...) + mu
data = 5 * np.random.randn(100) + 50

print ('data', data)
# summarize
print('mean=%.3f stdv=%.3f' % (np.mean(data), np.std(data)))
