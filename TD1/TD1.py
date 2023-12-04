#TD1

# -*- coding:Latin-1 -*-

# #Exo1
# a = input("entrez une valeur entière :")
# val =int(a)

# if val < 10 :
#     print('inferieure à 10')

# elif val == 10:
#     print('egal à 10')

# else :
#     print('superieur à 10')

# #Exo2
# if(val%2 == 0) :
#     print('c est une valeur paire')

# if(val%2 == 1) :
#     print('c est une valeur impaire')

# print(" ")

# #Exo3
# a=0 ; mux=7

# while a<20 :
#     print(f"{a}*7={a*mux}")
#     a = a+1

# print(" ")

# #Exo4
# suite=1
# index=0

# while index<12:
#     print(suite)
#     index = index+1
#     suite=suite*3

# print(" ") 

# #Exo5
# sec=int(input("Entre la seconde: "))
# nbheure = sec // 3600
# ressec = sec%3600
# nbminutes = ressec//60
# nbseconde = ressec%60

# print(f"{nbheure} heures {nbminutes} minutes {nbseconde} secondes")

# #Exo6
# i=1
# while i<7:
#     print("*" * i)
#     i=i + 1

# print(" ")

# #Exo7
# t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin','Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
# i=0; a=0
# for i in range(0,11,1):
#     t3=[(t1[i],t2[i])]


# for a in range(0,11,1):
#     print(t3[i]
          

#Exo9
fmax=0
table =[32, 5, 12, 8, 3, 75, 2, 15, 987]

for i in range (0,9,1) :
    if fmax < table[i] :
        fmax = table[i]

print(f"la valeur plus grande est {fmax}")

#Exo10
somme = 0
table =[32, 5, 12, 8, 3, 75, 2, 15, 987]
for i in range (0,8) :

    somme=somme + table[i]
    i += 1

moyenne = somme//8

print(f"la somme cumule est {somme} et la moyenne est {moyenne}")

#Exo10

table =[32, 5, 12, 8, 3, 75, 2, 15, 987]
#n = len(table)

for i in range(0, 9, 1) :
    for j in range (i+1, 9, 1) :
        if table[i]>table[j]:
            temp=table[i]
            table[i]=table[j]
            table[j]=temp

print(f"dans l'ordre croissant la liste est {table}")
