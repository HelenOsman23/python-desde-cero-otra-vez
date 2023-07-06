Como resumen podemos decir que Python al igual que casi todos los lenguajes de programación modernos manipulan valores, los cuales pertencen a cierto tipo o clase.

- in, float, str, bool, list, dict, tubla Y sets

Lo que se puede hacer con estos valores, depende de su tipo.

Además de los valores, Python, al igual que casi todos los lenguajes modernos, tiene operadores.

-+, -, %, /, *

Observación no podemos utilizar todos los operados con todos los tipos de valores. 
Por ejemplo, no es posible sumar un texto, con un número (int, float), pero curiosamente si es posible multiplicar un texto por un número.

``` Python
"Hola" + 4 # Error
"Hola" * 4 # Funciona
```

Por lo tanto es fundamental y muy necesario ejercitar con los diferentes tipo de valores.
Además tenemos las variables , permiten asociar un nombre con el valor para luego mediante el nombre utilizar o manipular el valor.

``` Python
some_var = "Hola Mundo"
print(some_var)
```

Para controlar la ejecución del programa dependiendo del valor de una condición, tenemos las estructuras del control como el `if`, `elif` y `else`.

Además Python tiene loops o iteración para ejecutar varias sentencias en cada vuelta o iteración. Python tiene 2 loops el `while` y `for`. 

Finalmente mencionar que Python también trae algunas funciones predefinidos para hacer tareas comunes y frecuentes como la función `print()`

-input(), int(), float(), len(), range(), print(), etc. 