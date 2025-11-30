import numpy as np

print("Enter vector dimension:")
n = int(input())

print("Enter 3 vectors:")
v1 = np.array(list(map(float, input().split())))
v2 = np.array(list(map(float, input().split())))
v3 = np.array(list(map(float, input().split())))

# Step 1
u1 = v1

# Step 2
u2 = v2 - (np.dot(v2, u1) / np.dot(u1, u1)) * u1

# Step 3
u3 = v3 \
     - (np.dot(v3, u1) / np.dot(u1, u1)) * u1 \
     - (np.dot(v3, u2) / np.dot(u2, u2)) * u2

# Normalize
e1 = u1 / np.linalg.norm(u1)
e2 = u2 / np.linalg.norm(u2)
e3 = u3 / np.linalg.norm(u3)

print("\nOrthonormal basis:")
print("e1 =", np.round(e1, 4))
print("e2 =", np.round(e2, 4))
print("e3 =", np.round(e3, 4))
