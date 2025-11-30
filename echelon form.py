import numpy as np

r = int(input("Rows: "))
c = int(input("Cols: "))

A = []
for i in range(r):
    A.append(list(map(float, input().split())))

A = np.array(A)
print("Echelon Form:\n", A.astype(float))
print("Rank:", np.linalg.matrix_rank(A))
