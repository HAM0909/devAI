import numpy as np
temperature = np.array([11, 12, 9, 11, 10])

moyenne = np.mean(temperature)
mediane = np.median(temperature)
ecart_type = np.std(temperature)

print(f"la moyenne de temperature: {moyenne} °C")
print(f"la mediane de temperature: {mediane} °C")
print(f"l'ecart type est: {ecart_type} ")


