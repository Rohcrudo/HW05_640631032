# -*- coding: utf-8 -*-
"""

@author: Nattapat Tangniyom 640631032
"""

import numpy as np
from scipy.linalg import solve
C = np.array([2, 3])
A = np.array([[0.5, 0.2], [1, 1]])
b = np.array([10, 30])
x = solve(A, b)
print(x)
#[13.33333333 16.66666667]
MAX = 2*(13) + 3*(17)
print(MAX)
#77