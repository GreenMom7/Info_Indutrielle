# -*- coding:Latin-1 -*-s
import numpy as np
import matplotlib.pyplot as plt

# Exercice 2(calcul moyenne et l'cart type de tirage)
mu, sigma = 10, 2 # mean and standard deviation
x = mu + sigma * np.random.randn(10000)

mu_n = x.mean() #calcul de la moyenne de tirage alatoire
sigma_n = x.std() #calcul de l'cart type de tirage alatoire

print(f"moyenne={np.around(mu_n,2)}   ecart type ={np.around(sigma_n,2)}")
n, bins, patches = plt.hist(x, bins=50, density=False, facecolor='green', alpha=0.75 )

plt.ylabel('Nombre d''apparitions')
plt.title('Histogram')

plt.text(mu, 1000, r'$\mu=$' + str(np.around(mu_n,2)) + ' $\\sigma=$' + str(np.around(sigma_n,2)))
plt.grid(True)

#les lignes verticales
plt.vlines(mu_n, 0, 1000, colors='red', linestyles='solid')
plt.vlines(mu_n+sigma_n, 0, 1000, colors='red', linestyles='dashed', linewidth=1)
plt.vlines(mu_n-sigma_n, 0, 1000, colors='red', linestyles='dashed', linewidth=1)

plt.show()
plt.close(1) # on ferme le figure
