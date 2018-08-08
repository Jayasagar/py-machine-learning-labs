import math
import numpy as np

# At fundamental level, Loss function is basic tool to calculate absolute difference between prediction made by teh algorithm and acua value.

def CrossEntropy(yHat, y):
    if y == 1:
      return -math.log(yHat)
    else:
      return -math.log(1 - yHat)

print(CrossEntropy(2, 1))

# Used for classification
def Hinge(yHat, y):
    return np.max(0, 1 - yHat * y)

print(Hinge(2, 1))