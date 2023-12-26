

def Volume(L=100,l=80,h=10):
    
    return L*l*h

L = input('entrer la longueur L :')
L=int(L)
l = input('entrer la largeur l :')
l=int(l)
h = input('entrer la longueur h :')
h=int(h)

vol = Volume(L,l,h)
print(f"Volume = {vol}")

Vol = Volume()
print(f'Volume 0 arguments = {Vol}')

Vol = Volume(L=L)
print(f'Volume 1 arguments = {Vol}')

Vol = Volume(L=L, l=l)
print(f'Volume 2 arguments = {Vol}')

    
