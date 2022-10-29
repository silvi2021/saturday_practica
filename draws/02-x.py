for i in range(1,11): 
    line = ""
    for j in range(1,11):
      if(j== i) or (j + i == 11):
        line += '*'
      else:
        line +="-"
    print(line)


       