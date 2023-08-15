import numpy as np
from numpy.linalg import inv, det

class MatrixTools:
    def inverse(A):
        a = np.matrix(A)
        return inv(a).tolist()
    
    def determinant(A):
        return det(np.matrix(A))