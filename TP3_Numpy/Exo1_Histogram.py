
# -*- coding:Latin-1 -*-
import numpy as np
import matplotlib.pyplot as plt

# print(f"{np.pi:.4f}")
# a = np.array([1, 2, 3, 4])
# print(f"a={a} de type {type(a)}")

# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(f"b={b}")

# #fonction arange()
# #paramètres : la valeur de départ la valeur d'arrivée
# # et le pas d'incrément

# m = np.arange(3, 15, 2)
# print(f"m={m}")

# #la fonction linspace()
# #paramètres : la valeur de départ la valeur d'arrivée
# # et le nombre de valeurs
# x = np.linspace(-np.pi/2, np.pi/2, 10)
# y = np.sin(x)
# print(f"y = {y}")

#nombres aléatoires
x1 = np.random.random()
print(f"x1={x1}")
#arrondis 2 chiffre après la virgule
print(f"x1={np.around(x1,2)}")
#tableau aléatoire 2D
x2 = np.random.random((2,3))
print(f"x2 = {x2}")
print(f"x2={np.around(x2,2)}")


# Exercice 1(tracer l'histogram)

mu, sigma = 10, 2 # mean and standard deviation
x = mu + sigma * np.random.randn(10000)
n, bins, patches = plt.hist(x, bins=50, density=False, edgecolor='white', facecolor='green', alpha=0.75 )
