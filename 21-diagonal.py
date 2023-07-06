size = int(input("¿De qué tamaño quieres el cuadrante?: "))

for y in range(size):
    line = ""
    for x in range(size):
        if (x == y or x + y == size-1):
            line += "*"
        else:
            line += " "
    print(line) 
    