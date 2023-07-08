# Una evaluación condicional puede estar dentro de otra. Por ejemplo:
name = input("Hola, ¿Cuál es tu nombre?: ")
age = int(input("Dime tu edad: "))

print(f"Hola {name}!")

if(age >= 18):
    drink = input("¿Quieres cerveza o vino?: ")
    if(drink) == "cerveza":
        print("Toma: ")
        print("Aqui tienes tu cerveza")
    else:
        print("Aquí esta tu vino") 
else:
    juice = input("¿Quieres jugo de frutilla o naranja?: ")  
    if(juice == "frutilla" or juice == "frutillas"):
        print("Aquí esta tu jugo de fresas")
    else:
        print("Aquí esta tu jugo de naranjas")           