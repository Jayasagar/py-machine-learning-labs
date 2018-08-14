import numpy as np

# Regressive loss functions
# Mean Square Error
# Absolute Error measures
# Smooth Absolute Error

# Reference: https://stackoverflow.com/questions/17197492/root-mean-square-error-in-python

# RMSE: (Root mean squared error), MSE: (Mean Squared Error) and RMS: (Root Mean Squared),

def rootMeanSquaredError(predictions, actuals):
    # Difference
    difference = predictions - actuals

    # Squared Differnece
    difference_squared = difference ** 2

    # Mean of the squared difference
    mean_of_difference_squared = difference_squared.mean()

    # Square root
    square_root_of_mean_result = np.sqrt(mean_of_difference_squared)

    return square_root_of_mean_result


def meanAbsoluteError(predictions, actuals):
    # return np.sum(np.absolute(predictions - actuals))
    return np.absolute(predictions - actuals).mean()

actuals = [0.000, 0.254, 0.998]
predictions = [0.000, 0.166, 0.333]


error = rootMeanSquaredError(np.array(predictions), np.array(actuals))
print('RMSE Error:', error)

print('MAE Error:', meanAbsoluteError(np.array(predictions), np.array(actuals)))

# Outlier scenario

actuals = [0.000, 0.254, 0.998]
predictions = [0.000, 0.166, 15]

print('Outlier RMSE Error:', rootMeanSquaredError(np.array(predictions), np.array(actuals)))

print('Outlier MAE Error:', meanAbsoluteError(np.array(predictions), np.array(actuals)))