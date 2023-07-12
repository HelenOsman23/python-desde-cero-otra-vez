english_to_spanish = {"one": "uno","two": "dos"}

# Podemos obtener una lista de todos los valores con el método .values()

vals = english_to_spanish.values() # => Nos entrega ["uno", "dos"] (valores del diccionario)

for val in vals:
    print(val)