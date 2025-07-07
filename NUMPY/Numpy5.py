import numpy as np

Data = np.array([2, 4, 5, 8])

x = Data > 2

mp = np.where((Data % 2 == 0) & (Data > 2),Data,0)

print(mp)
