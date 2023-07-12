# Hacer un diccionario que tenga tres items 
# Python: Lenguaje moderno utilizado para todo tipo de aplicaciones
# Ruby: Lenguaje completamente orientado a objetos 
# js: Lenguaje para la web

lenguaje = input("Que lenguaje quieres conocer?: ")
lenguajes = {}

lenguajes["python"] = "Lenguaje moderno utilizado para todo tipo de aplicaciones"
lenguajes["ruby"] = "Lenguaje completamente orientado a objetos"
lenguajes["javascript"] = "Lenguaje para la web y los servidores"

if lenguaje in lenguajes:
    print(f"Si está {lenguaje}")
    print(f"Su valor es {lenguajes[lenguaje]}")
else:
    print(f"No conozco el lenguaje {lenguaje}")    