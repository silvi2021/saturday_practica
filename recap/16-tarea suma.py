#crear una funcion que sume los numeros hasta el numero n


def sum_up_to(n):
    acc = 0     

    print("##################")  
    for number in range(1, n + 1):
        acc += number
    print(acc)

sum_up_to(10)

