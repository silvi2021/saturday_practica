# diagonal de 10 x 10

for i in range(1,11): 
    line = ""
    for j in range(1,11):
      if(j == i):
        line += '*'
      else:
        line +="-"
    print(line)


       