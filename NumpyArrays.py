import numpy as np

# rerefence: https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/AccessingDataAlongMultipleDimensions.html

# using a 2-dimensional array to store the grades
grades = np.array([
    [93,  95],
    [84, 100],
    [99,  87]
])


print(grades[1,0])
print(grades[-1,0])

#First column of each entry

print(grades[:, :1])

# Supplying Fewer Indices Than Dimensions
print(grades[0])

d3_array = np.array([[[0, 1],
    [2, 3]],
    [[4, 5],
    [6, 7]]])

print ('No of Dimensions', d3_array.ndim)

print('d3_array[1]:', d3_array[1]) # which recall is shorthand for d3_array[1, :, :]