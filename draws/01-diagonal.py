# didujar una diagonal de 7 x 9

for i in range(1,8):
    row = ""
    for j in range(1,10) or (j == i):
        row += "*"
    print(row)
       