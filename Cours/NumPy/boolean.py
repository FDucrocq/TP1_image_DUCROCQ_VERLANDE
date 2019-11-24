import numpy as np

arr = np.array([
 [1.2, 2.3, 4.0],
 [1.2, 3.4, 5.2],
 [0.0, 1.0, 1.3],
 [0.0, 1.0, 2e-1]])
print(arr)

is_greater_one = (arr >= 1.)
print(is_greater_one)

# Nous pouvons utiliser l'opérateur [ ] de Python pour découper le tableau:
print(arr[0, 0])  # First row, first column
print(arr[1])  # The whole second row
print(arr[:, 2])  # The third column

# Les tranches sont des vues, qui partagent la mémoire avec le tableau d'origine!
print("Before: {}".format(arr[1, 0]))
view = arr[1]
view[0] += 100
print("After: {}".format(arr[1, 0]))
