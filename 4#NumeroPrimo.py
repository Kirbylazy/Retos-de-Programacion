"""
 Escribe un programa que se encargue de comprobar si un número es o no primo.
 Hecho esto, imprime los números primos entre 1 y 100.
"""

# Función para comprobar si un numero es primo
def es_primo(numero):

    for i in range(2, int(numero)):  # Comprobaremos si es divisible por cada uno de los numero que tiene por debajo
        if numero % i == 0:  # Si encontramos que es divisible ya podemos dejar de comprobar
            return False
    return True  # En caso de no encontrar nigún divisor definimos que es primo

#  Funcion para recorrer el rango de numeros que decidamos
def rango_primos(rango):
    primos = []  # Aqui almacenaremos nuestro numero primos
    # Recorremos todos los numeros dentro de nuestro rango
    # evitando el 1 que no es primo
    for numero in range(2, rango + 1):
        # usamos nuestra función para comprobar,
        # en caso de recibir True lo almacenamos en unestra lista
        if es_primo(numero):
            primos.append(numero)
    return primos


# Imprimimos todos los números primos del 1 al 100
print(rango_primos(100))