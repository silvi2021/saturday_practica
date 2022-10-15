#crear una funcion que imprima los numeros divisibles por 3 hasta el numero n


def divisibles_by_three(n):
    print("################")
    for number in range(1,n + 1):
        if number % 3 == 0:      
           print(number)

 
              
divisibles_by_three(50)





















