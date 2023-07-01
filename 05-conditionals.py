# Asignación y reasignación 
# La asignación es dar un nombre a un valor, es decir, asignar una variable a un valor.
# Ejemplos:

fruit = "Chocolate"
veggie = "Papas fritas"
tables = 5

# Mientras que la reasignacón es tomar una variable ya existente y darle un valor completamente diferente.
# Ejemplo:

name = "Helen"
name = "HelenRamirez"

# Ejecución condicional 
# Todos los programas hacen evaluaciones condicionales según el valor de sus variables y expresiones. por lo tanto no todas las lineas de código se ejecuta 
# Para esto está el concepto de Expresión Booleana 
# Ejemplo:
print("----------Expresiones Booleanas----------")
print(5 < 4)# False
print(5 > 4)# True
print(4 != 4)# False 
print(4 == 4)# True

# Cuando queremos comparar menor o igual el operador es <= 
print( 4 <= 6)
#El mayor igual es >=
print( 5 >= 3)
# No existe el => ni =<


# Podemos tener expresiones booleanas más complejas utilizando los operadores and, or y not
print("----------Expresiones Booleanas----------")
print( 4 < 5 or 6 > 8) # True or False => True  
print( 4 < 5 and 6 > 8) # True and False => True
print(not True) # => False 