# Recorrer el diccionario e imprimir cada estudiante de la siguiente forma:

# El estudiante x reprobó con promedio y
# El estudiante x aprobó con promedio y

# La nota de aprobación la debe ingresar el usuario

user_option = float(input("Ingrese la nota de aprobación: "))

averages = {
    "Helen": 5,
    "Osman": 6.5,
    "Tamara": 7,
    "Madelin": 6.4,
    "Haldair": 6.2,
    "Felix": 4.8
}

for student in averages.keys():
    if averages[student] > user_option:
        print(f"El estudiante: {student}, aprobó con promedio: {averages[student]}")
    else:
        print(f"El estudiante: {student}, reprobó con un promedio de: {averages[student]}")     
       





