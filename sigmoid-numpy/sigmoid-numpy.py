import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.asarray(x)  # Converts lists or nested lists to a NumPy array
    return 1 / (1 + np.exp(-x))
