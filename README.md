# MFC-PRACTICALS
[1 MFC.py](https://github.com/user-attachments/files/23840953/1.MFC.py)
import numpy as np

r = int(input("Rows: "))
c = int(input("Cols: "))

vals = list(map(float, input().split()))
A = np.array(vals).reshape(r, c)

print("Transpose:\n", A.T)
