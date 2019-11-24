import numpy as np

arr = np.array([
 [1.2, 2.3, 4.0],
 [1.2, 3.4, 5.2],
 [0.0, 1.0, 1.3],
 [0.0, 1.0, 2e-1]])
print(arr)

# Inspection des propriétés du tableau:
print(arr.dtype)
print(arr.ndim)
print(arr.shape)

# Lors de la construction d'un tableau, nous pouvons spécifier explicitement le type
iarr = np.array([1,2,3], np.uint8)

# Les opérations arithmétiques sur la matrice respectent le type et peuvent inclure
# l'arrondi et le débordement
arr *= 2.5
iarr *= 2
print(arr)
print(iarr)