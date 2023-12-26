
while(True):
    a = int(input("saisir [a :"))
    b = int(input("saisir b]:"))
    val = int(input("saisir une valeur :"))
    if a <= val <= b:
        print(val, "appartient a l'intervalle [",a,",",b,"]")
        print('')
    else:
        print(val, "n'appartient pas a l'intervalle [",a,",",b,"]")
        print('')