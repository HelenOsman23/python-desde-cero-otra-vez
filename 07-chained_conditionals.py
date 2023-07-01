# Podemos encontrar situaciones donde se requiere de más de una expresión booleana para determinar el flujo de ejecición del programa.

firts_number = int(input("Dame el primer número: "))
second_number = int(input("Dame el segúndo número: "))

if firts_number < second_number:
    print("El segúndo número es mayor")
elif firts_number > second_number:
    print("El primer número es mayor")
else:
    print("Son iguales")        