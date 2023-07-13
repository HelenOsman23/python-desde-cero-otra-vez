# Imprime una lista con todos los valores 

averages = {
    "Helen": 5,
    "Osman": 6.5,
    "Tamara": 7,
    "Madelin": 6.4,
    "Haldair": 6.2,
    "Felix": 4.8
}

grades = averages.values()
vals = []

for grade in grades:
    vals.append(grade)
print(vals)    
