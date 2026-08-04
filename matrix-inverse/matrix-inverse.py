import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I.
    Returns None if the matrix is singular (uninvertible).
    """
    try:
        # Attempt to compute the true mathematical inverse
        return np.linalg.inv(A)
    except np.linalg.LinAlgError:
        # Handle the singular matrix scenario gracefully
        return None
