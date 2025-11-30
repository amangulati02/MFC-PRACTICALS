import sympy as sp

x, y, z = sp.symbols('x y z')

f = sp.sympify(input("Enter f(x,y,z): "))

dfx = sp.diff(f, x)
dfy = sp.diff(f, y)
dfz = sp.diff(f, z)

print("\nGradient =", [dfx, dfy, dfz])
