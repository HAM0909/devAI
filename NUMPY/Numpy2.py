import numpy as np

Data = np.array([11, 12, 13, 14, 15, 16])
moyenne = np.mean(Data)
ecart_type = np.std(Data)

donnée_soustraction = Data - moyenne

print(donnée_soustraction)

ecart_division = Data / ecart_type

print(ecart_division)