import numpy as np
import math

#  Ref: https://www.mathsisfun.com/data/standard-deviation.html
def standard_deviation():
    """
    SQRT of variance is the standard deviation!
    :return:
    """
    # Example: Input: height of dogs
    #  Outout : Standard Deviation

    dog_heights_mm = [600, 470, 170, 430, 300]

    np_dog_heights_mm = np.array(dog_heights_mm)

    # Forst calculate Mean
    mean = np_dog_heights_mm.mean()
    print('Mean of dog height:', mean)

    variance = 0;
    for height in np_dog_heights_mm :
        # Square each difference
        variance = variance + (height - mean)**2

    variance_mean = variance / len(np_dog_heights_mm)
    print('Variance Mean value:', variance_mean)

    standard_deviation = math.sqrt(variance_mean)
    print('Standard Deviation:', standard_deviation)

standard_deviation()
