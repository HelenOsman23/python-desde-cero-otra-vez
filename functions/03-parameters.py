# Algunas funciones que hemos visto reciben parametros.
# Por ejemplo print recibe como parámetro lo que va a mostrar en la terminal

def print_hero(hero_name):
    print(f"Soy el súper heroe {hero_name}")

print_hero("Mega Man")

hero = "Chapulín colorado"

print_hero(hero)

# Las funciones que reciben parámetros, estos son obligatorios 
# La siguiente sentencia da error porque falta el parametro hero_name
print_hero()