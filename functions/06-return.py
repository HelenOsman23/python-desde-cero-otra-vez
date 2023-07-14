# Para hacer que una función entregue un valor de retorno utilizamos la palabra return

def hero_phrase(hero_name):
    phrase = f"Soy el súper heroe {hero_name}"
    return phrase

superman = "Super Man"
aquaman = "Aqua Man"

super_phrase = hero_phrase(superman)
aquaman_phrase = hero_phrase(aquaman)

print(super_phrase)
print(aquaman_phrase)