import numpy as np
import sympy as sp

rows = int(input("Rows: "))
cols = int(input("Cols: "))

print("Enter the matrix values:")
vals = list(map(float, input().split()))

A = sp.Matrix(np.array(vals).reshape(rows, cols))

print("\nMatrix A:")
sp.pprint(A)

rank = A.rank()
print("\nRank:", rank)

if rank == cols:
    print("\nVectors are linearly independent")
else:
    print("\nVectors are linearly dependent")

    ns = A.nullspace()
    print("\nA linear combination is:")

    for v in ns:
        for i in range(cols):
            print(f"{v[i]} * v{i+1}", end=" + ")
        print(" = 0\n")
