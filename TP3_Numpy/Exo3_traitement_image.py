#-*- coding:Latin1 -*-
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimage
img = mpimage.imread('Z:/lena.png')
#img = mpimage.imread('Z:/demo_image.png')

#  4.1 L'Image
print( 'classe :', type(img) )
print( 'type :', img.dtype )
taille = img.shape
lignes = taille[0]
colonnes = taille[1]
print( 'taille :', taille )
print( 'modifiable :', img.flags.writeable )

imgGray = (img[:,:,0]+img[:,:,1]+img[:,:,2])/3
taille = imgGray.shape
lignes = taille[0]
colonnes = taille[1]
print( 'taille :', taille )

## La Convolution
## 4.3 Filtrage Moyenne

## creation de kernel
kernel_moyen = np.ones((3,3), np.float32)/9 #cre une matrcice 3*3 avec les elements que de '1/9'

#imageFiltre = np.zeros(taille) #cre une matrcice 600*800 avec les elements que de  '0'
#taillefiltre = 3
#taillebord = taillefiltre//2

### 2 boucles imbriques qui vont parcourir toute l'image en niveau de gris
#for i in range(taillebord, lignes-taillebord):
#    for j in range(taillebord, colonnes-taillebord):
#        M = imgGray[(i-taillebord):(i+taillebord+1),(j-taillebord):(j+taillebord+1)]
#        #print(f" M taille = {M.shape}, M = {M}")
#        Convolution = M * kernel_moyen
#        imageFiltre[i,j] = np.sum(Convolution)


## 4.5 utilisation de scipy() - aller plus vite
imageFiltre = signal.convolve2d(imgGray, kernel_moyen, mode='same',boundary='fill', fillvalue=0)

# # 4.4 Ajoute du bruit

imageNoisy = np.random.randn(lignes, colonnes)
#Ajout du bruit  l'image origine
imageBruit = imgGray + imageNoisy

## Filtrage Contour
### Kernel contour

kernel_contour = np.array([[0, 1, 0],
                       [1, -4, 1],
                       [0, 1, 0]])

imageContour = signal.convolve2d(imgGray,kernel_contour, mode='same',boundary='fill', fillvalue=0)

seuil = 0.002
imageBinaire = imageContour > seuil

plt.figure(4)
plt.subplot(141)
plt.title('Image Origine')
imgplot = plt.imshow(imgGray, cmap="gray")

plt.subplot(142)
plt.title('Image Filtre')
imgplot = plt.imshow(imageFiltre, cmap="gray")

plt.subplot(143)
plt.title('Image Contour')
imgplot = plt.imshow(imageContour, cmap="gray")

plt.subplot(144)
plt.title('Image Binaire')
imgplot = plt.imshow(imageBinaire, cmap="gray")
plt.show()
input()
