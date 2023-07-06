size = int(input("¿De qué tamaño quieres el cuadrante?: "))

for row in range(size):
    line = " "
    for col in range(size):
        if(row == 0 or row == size-1 or col + row == size-1):
            line += "*"
        else:
            line += " "    
    print(line)    