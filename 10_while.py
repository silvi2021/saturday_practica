import time
# While es otra estructura de controls que repite pasos
#similar al for.Podemos entenderla como "mientras"
#ejemplo

counter = 0
while counter < 5:
    print(counter)
    time.sleep(0.5)
    counter = counter + 1
    