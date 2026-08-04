import numpy as np

def mean_squared_error(y_pred, y_true):
    # Converts to arrays, subtracts, squares, and calculates the average
    return np.mean((np.array(y_pred) - np.array(y_true)) ** 2)
