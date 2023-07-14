# Crear una función que retorne la suma de todos los números hasta el número number pasado como parámetro

# sum_up(5) => 1+2+3+4+5 = 15
user_option = int(input("Escribe un número: "))

def sum_up(number):
    total = 0
    for num in range(1, number+1):
        total += num
    return total

print(sum_up(user_option))
    