import numpy as np

arr = np.array([
 [1.2, 2.3, 4.0],
 [1.2, 3.4, 5.2],
 [0.0, 1.0, 1.3],
 [0.0, 1.0, 2e-1]])
print(arr)

# Moyenne d'un tableau
# Également disponible : max, min, sum, ptp (point à point, c'est-à-dire différence entre
# les valeurs maximales et minimales)
print(arr.mean())

# Ces fonctions peuvent également fonctionner selon les axes:
print(arr.mean(axis=0))

# Une astuce importante consiste à combiner des opérations logiques avec A
is_greater_one = (arr > 1)
print(is_greater_one.mean())
