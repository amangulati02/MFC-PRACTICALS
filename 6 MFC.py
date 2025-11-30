import sympy as sp

r = int(input("Rows: "))
c = int(input("Cols: "))

A = []
for i in range(r):
    A.append(list(map(float, input().split())))

A = sp.Matrix(A)

print("Column Space:", A.columnspace())
print("Row Space:", A.rowspace())
print("Null Space:", A.nullspace())
print("Left Null Space:", A.T.nullspace())
