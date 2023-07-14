# Crea una función que imprima cada elemento de las lista fruits
# de la siguiente forma I like apple

fruits = ["apple", "orange", "kiwi", "banana"]
more_fruits = ["watermelonn","mango", "pineapple", "pear"]
def print_fruits(fruits_list):
    for fruit in fruits_list:
        print(f"I like {fruit}")

print_fruits(fruits)
print_fruits(more_fruits)
