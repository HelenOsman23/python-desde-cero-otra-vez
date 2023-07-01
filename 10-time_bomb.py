import time
# Ejercicio, hacer un programa que contando regresivamente desde 10 y que al llegar a cero diga "Boooom"
# Tip: esperar un segundo entre cada iteración utilizando time.sleep(1)

num = 10
while num >= 0:
    print(num)
    num = num - 1
    time.sleep(1)

print("Booooom")
print(num)