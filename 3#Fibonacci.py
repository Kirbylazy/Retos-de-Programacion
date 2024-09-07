"""
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
   0, 1, 1, 2, 3, 5, 8, 13...
"""


def fibonacci(n):
    fib_sequence = [0, 1]  # Inicializamos la secuencia con los dos primeros números de Fibonacci

    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]  # Sumamos los dos últimos números para obtener el siguiente
        fib_sequence.append(next_number)  # Agregamos el siguiente número a la secuencia

    return fib_sequence


# Imprimimos los primeros 50 números de la sucesión de Fibonacci

for number in fibonacci(50):
    print(number)