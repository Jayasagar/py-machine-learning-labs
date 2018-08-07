import math

def CrossEntropy(yHat, y):
    if y == 1:
      return -math.log(yHat)
    else:
      return -math.log(1 - yHat)

print(CrossEntropy(2, 1))