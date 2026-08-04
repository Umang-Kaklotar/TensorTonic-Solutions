import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x=np.asarray(x)
    for i in x:
        return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
    pass