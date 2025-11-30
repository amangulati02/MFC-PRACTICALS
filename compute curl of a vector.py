import sympy as sp

x, y, z = sp.symbols('x y z')

P = input("P(x,y,z): ").strip()
Q = input("Q(x,y,z): ").strip()
R = input("R(x,y,z): ").strip()

P, Q, R = sp.sympify(P), sp.sympify(Q), sp.sympify(R)

curl_x = sp.diff(R, y) - sp.diff(Q, z)
curl_y = sp.diff(P, z) - sp.diff(R, x)
curl_z = sp.diff(Q, x) - sp.diff(P, y)

print("\nCurl =", [curl_x, curl_y, curl_z])
