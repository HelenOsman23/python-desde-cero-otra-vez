# Escribir un programa que imprima una lista de los estudiantes con promedio superior a 6.

averages = {
    "Helen": 5,
    "Osman": 6.5,
    "Tamara": 7,
    "Madelin": 6.4,
    "Haldair": 6.2,
    "Felix": 4.8
}

approved_students = []

for student in averages.keys(): # => ["Helen","Osman","Tamara"...]
    if averages[student] > 6:
        approved_students.append(student)
        
print(approved_students)        