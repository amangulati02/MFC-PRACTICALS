import numpy as np

n = int(input("Enter n: "))
A = []

for i in range(n):
    A.append(list(map(float, input().split())))

A = np.array(A)
print("Matrix A:\n", A)

det = np.linalg.det(A)
print("Determinant:", det)

if det != 0:
    adj = np.linalg.inv(A).T * det
    print("Adjoint:\n", adj)
    print("Inverse:\n", np.linalg.inv(A))
else:
    print("Inverse does not exist.")
