import numpy as np

r = int(input("Rows: "))
c = int(input("Cols: "))

A = []
for i in range(r):
    A.append(list(map(float, input().split())))

A = np.array(A, float)

for i in range(r):
    A[i] = A[i] / A[i][i]
    for j in range(r):
        if i != j:
            A[j] = A[j] - A[j][i] * A[i]

print("RREF:\n", A)
