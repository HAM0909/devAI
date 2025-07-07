import numpy as np

Data = np.array([10, 6, 9, 17, 8])

Josh = np.array([10, 16, 9, 20, 10])

find1 = np.where(Data != Josh)[0]


print(Data[find1])
print(Josh[find1])




