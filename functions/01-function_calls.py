# En la programación una función es un conjunto de sentencias que tiene un nombre.
# Cuando definimos una función, se especifica el nombre y las lineas de código que le pertenecen 
# Luego se puede llamar, ejecutar e invocar a la función

# Las funciones tienen su propio tipo
# builtin_function_or_method
print(type(print))

# Para ejecutar una función sí o sí hay que terminarla con ()
print("Hola!")
print(int(3.9999))

from random import choice, randint

print(choice([1,2,3]))
print(randint(1,5))