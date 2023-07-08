# Ejercicio, utilizando for y range, crear un algoritmo que imprima en la terminal las tablas de multiplicar desde el 1 al 12.

# La tabla del 1 es:
for table in range(1,13):
    print()
    print(f"La tabla del {table}")
    for step in range(1,13):
        print(f" {table} x {step} = {table*step}")





