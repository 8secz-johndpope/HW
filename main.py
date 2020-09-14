import numpy as np


def decorator(func):

    def wrapper():
        result = func()
        return  np.linalg.matrix_rank(result)
    return wrapper

@decorator
def rank():
    matrix = [[1,0,0],[0,1,0],[0,0,0]]
    return matrix

result = rank()
print (result)


