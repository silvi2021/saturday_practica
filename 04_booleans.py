# Un tipo de valor con solo dos opciones 
# Veradero o falso

is_real = True
unreal= False


# Las comparaciones entregan o devuelven un booleano

print(10<9)

print(10>9)

print(10==9)

# Ejemplo evaluando variables

limit = 18
age = 21

if age >= limit:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

    # Todos los valores tienen una representación
    # booleana. Vamos a probarlo

zero = 0
one = 1
empty_str = ''

if zero:
    print(zero, "es verdadero")
else:
    print(zero, 'es falso')
    
if one:
    print(one, "es verdadero")
else:
    print(one, 'es falso')    

if empty_str:
    print(empty_str,"es verdadero")
else:
    print(empty_str,"es falso")    



