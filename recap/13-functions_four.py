#Completar la siguiente funcion para que imprima cualquier tabla de 
#multiplicacion hasta el 12

def multiplication_table(number = 1):
   print("####################")
   for i in range(1,13):
     print(number,"x",i, "=", number *1)


# otra forma de hacerlo:
#def multiplication_table(number = 1):
   # print("#########################")
   # print(number, "x 1 =", number * 1)
   # print(number, "x 2 =", number * 2)
   # print(number, "x 3 =", number * 3)
   # print(number, "x 4 =", number * 4)
   #print(number, "x 5 =", number * 5)
   # print(number, "x 6 =", number * 6)
   # print(number, "x 7 =", number * 7)
   # print(number, "x 8 =", number * 8)
   # print(number, "x 9 =", number * 9)
   # print(number, "x 10 =", number * 10)
   #print(number, "x 11 =", number * 11)
   #print(number, "x 12 =", number * 12)
 


multiplication_table(2)
multiplication_table(8)