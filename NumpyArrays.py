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