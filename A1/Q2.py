import numpy as np

A = np.zeros((2, 2))
print("Enter the elements of the 2x2 matrix A:")
for i in range(2):
    for j in range(2):
        A[i][j] = float(input())

try:
    Ainv = np.linalg.inv(A)
except np.linalg.LinAlgError:
    print("Error: Matrix A is not invertible.")
    exit()

prod = np.dot(A, Ainv)

pass_test = np.allclose(prod, np.eye(2), atol=1e-6)

if pass_test:
    print("PASS: A*Ainv = I")
else:
    print("FAIL: A*Ainv != I")
