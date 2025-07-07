import numpy as np

Matrice1 = np.array([[1, 2],[4, 5]])
Matrice2 = np.array([[5, 6],[7, 8]])

Matrice_total = Matrice1 * Matrice2

print(Matrice_total)

Matrice_Transposé = np.transpose(Matrice_total)

print(Matrice_Transposé)

Matrice_Inverse = np.linalg.inv(Matrice_total)

print(Matrice_Inverse)
