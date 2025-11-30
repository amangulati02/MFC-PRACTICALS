import numpy as np
import sympy as sp

r = int(input("Rows: "))
c = int(input("Cols: "))

vals = list(map(float, input("Enter values: ").split()))
A = sp.Matrix(np.array(vals).reshape(r, c))

print("\nMatrix A:")
sp.pprint(A)

try:
    P, D = A.diagonalize()
    print("\nMatrix is diagonalizable.\n")

    print("P (Eigenvectors):")
    sp.pprint(P)

    print("\nD (Diagonal of Eigenvalues):")
    sp.pprint(D)

except:
    print("\nMatrix is NOT diagonalizable.\n")

    cp = A.charpoly()
    print("Characteristic Polynomial:")
    sp.pprint(cp.as_expr())

    print("\nCayley-Hamilton Check:")
    result = cp.eval(A)
    sp.pprint(result)

    if result == sp.zeros(r, c):
        print("\nCayley-Hamilton Verified.")
    else:
        print("\nCayley-Hamilton Not Verified.")
