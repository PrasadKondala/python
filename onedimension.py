import numpy as np
A = np.array([[2,3,5],[1,5,8],[6,9,4]])
B = np.eye(N=3, dtype=int)

add = A + B
print("The addition of two matrices is: \n",add)

multiplication = A * B
print("The multipication of two matrices is: \n",multiplication)