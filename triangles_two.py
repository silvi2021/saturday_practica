import time

# Este programa ayuda a saber si podemos hacer un triangulo
# Dadas tres longitudes

print("Hola. te voy a ayudar con eso")
l1=int(input("Ingresa la longitud uno\n"))
l2=int(input("Ingresa la longitud dos\n"))
l3=int(input("Ingresa la longitud tres\n"))

print("Las longitudes entregadas hasta el momento son:")

print(l1,l2,l3)

if (l1 <=l2+l3) and (l2 <=l1+l3) and (l3 <=l2+l1):
    print("Si es posible el triangulo con",l1,l2,l3)
else:
     print("no es posible el triangulo:",l1,l2,l3,"no cumplen la condicion")
