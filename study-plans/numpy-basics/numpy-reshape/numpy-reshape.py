import numpy as np

def reshape_array(data, operation):
    """
    Returns: ndarray of float64 with shape determined by the operation
    """

    arr = np.array(data, dtype=np.float64)
    # i have a 2D list and need to convert it to an fliat64 array and transform it
    if operation == "flatten":
        return arr.flatten()
    if operation == "transpose":
        return arr.transpose()
    if operation == "add_batch":
        return np.expand_dims(arr,axis=0)