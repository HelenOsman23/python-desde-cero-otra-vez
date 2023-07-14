# Las funciones pueden definir variables en su interior, pero estas variables son parte de ese ámbito y no son accesibles desde fuera de la función 

def print_fullname(firtsname,lastname):
    fullname = f"{firtsname} {lastname}"
    print(f"-----{fullname}-----")

print_fullname("sebas", "jmnz")   

# Desde afuera no podemos acceder a las variables internas de la función
print(fullname)