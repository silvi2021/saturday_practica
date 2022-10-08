import time

# Este programa ayuda a saber si podemos hacer un triangulo
# Dadas tres longitudes

print("Hola. te voy a ayudar con eso")
l1=int(input("Ingresa la longitud uno\n"))
l2=int(input("Ingresa la longitud dos\n"))
l3=int(input("Ingresa la longitud tres\n"))

print("Las longitudes entregadas hasta el momento son:")

print(l1,l2,l3)

if (l1 <=l2+l3):
    print("vamos bien,revisemos los otros casos")
    time.sleep(0.5)
    if(l2<=l1+l3):
      print("seguimos bien,veamos el tercero")
      time.sleep(0.5)      
      if(l3<=l2+l1): 
        print("si es posible el triangulo")
        time.sleep(0.5)
      else:
        print("si es posible el triangulo")
    else:
        print("si es posible el triangulo")
else:
     print("no es posible el triangulo:",l1,"no es menor que",l2,"+",l3)









