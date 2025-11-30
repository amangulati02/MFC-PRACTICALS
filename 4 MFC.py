import numpy as np

r = int(input("Rows:"))
c = int(input("Columns:"))

a = []
print("Enter elements : ")
for i in range (r):
    a.append(list(map(float, input().split())))

a = np.array(a,float)
b = np.zeros(r)

try :
    x = np.linalg(a,b)
    print("Solution :", x)
except:
    print("No unique solution :")
