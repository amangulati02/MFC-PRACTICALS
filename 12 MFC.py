import sympy as sp

x, y, z = sp.symbols('x y z')

P = input("P(x,y,z): ").strip() or "x*y"
Q = input("Q(x,y,z): ").strip() or "y*z"
R = input("R(x,y,z): ").strip() or "z*x"

P, Q, R = sp.sympify(P), sp.sympify(Q), sp.sympify(R)

div = sp.diff(P, x) + sp.diff(Q, y) + sp.diff(R, z)

print("\nDivergence =", div)
