# En python algunos tipos de valores son considerados colecciones como las listas, diccionarios, strings, tuplas y sets. Estas colecciones se pueden recorrer.
# Con el for loop podemos ejecutar un conjunto de sentencias, una por cada elemento de la colección.

word = 'banana'
index = 0
while index < (len(word)):
    print(word[index])
    index += 1

print("-----------------------")

for letter in 'banana':
    print(letter) 