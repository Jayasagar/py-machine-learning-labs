# The Basics of NumPy Array

import numpy as np
np.random.seed(0)  # seed for reproducibility

oneDimensional = np.random.randint(10, size=10)  # One-dimensional array
twoDimensional = np.random.randint(10, size=(3, 4))  # Two-dimensional array
threeDimensional = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array


# print("threeDimensional ndim: ", threeDimensional.ndim)
# print("threeDimensional shape:", threeDimensional.shape)
# print("threeDimensional size: ", threeDimensional.size)

## Array Slicing: Accessing Subarrays

# oneDimensional[start:stop:step]
# If any of these are unspecified,
# they default to the values start=0, stop=size of dimension, step=1.
# We'll take a look at accessing sub-arrays in one dimension and in multiple dimensions.

# One Dimensional
# print(oneDimensional[:5])  # first five elements
# print(oneDimensional[5:])  # elements after index 5
# print(oneDimensional[4:7])  # middle sub-array
# print(oneDimensional[::2])  # every other element
# print(oneDimensional[1::2])  # every other element, starting at index 1
# print(oneDimensional[::-1])  # all elements, reversed
#
# ## Multi Dimensional
# print(twoDimensional[:2, :3])  # two rows, three columns
# print(twoDimensional[:3, ::2])  # all rows, every other column

# print(twoDimensional)
# print(twoDimensional[::-1, ::-1]) ## Operating on 2 dimensions
# print(twoDimensional[::-1]) ## Only dealing with  first dimension


# Sub Array and No copy of SUB ARRAYS

sub_array = threeDimensional[:2, :2, :2]
# print(sub_array)

#  Change any value will change original value
sub_array[0][0][0] = 15

# print sub_array

# Creating copies of arrays
sub_array_copy = threeDimensional[:2, :2, :2].copy()

print sub_array_copy

# Change any value, now it wont change
sub_array_copy[0][0][0] = 19

print sub_array