# Hacer una función que imprima los números del 0 al n pasado como parámetro
# -- 1 -- 
# -- 2 -- etc
def print_num(number):
    print("----------")
    for num in range(number+1):
        print(f"-- {num} --")

print_num(5)
print_num(10)