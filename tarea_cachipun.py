print("Hola,juguemos cachipun")

print ("ingresa su opción")
print ("piedra")
print ("tijera")
print ("papel")
mano1 =input("jugador1\n")

print ("ingresa tu opción")
print ("piedra")
print ("tijera")
print ("papel")
mano2 =input("jugador2\n")

  
if mano1==mano2:
    print("Empatan jugadores")
else:
    if mano1=="piedra":
        if mano2=="papel":
           print ("Gana jugador2")
        else:
            print ("gana jugador1")
    else:              
        if mano1=="tijera":
            if mano2=="piedra":
               print ("Gana jugador2")
            else:
                print("gana jugador1")
        else:
            if mano2=="piedra":
               print("gana jugador1")
            else:
                print("gana jugador2")           


