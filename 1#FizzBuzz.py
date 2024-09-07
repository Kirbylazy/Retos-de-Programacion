"""
 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 Múltiplos de 3 por la palabra "fizz".
 Múltiplos de 5 por la palabra "buzz".
 Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 """

# usaremos una función para poder editar cada vez los parametros a usar


def fizzbuzz(m3, m5, ri, rs):
    listado = ""  # en esta variable almacenaremos la string a imprimir

    for i in range(ri, (rs + 1)):
        # con el bucle for recorreremos todos los numero dentro de nuestro rango

        if i % 3 == 0 and i % 5 == 0:
            # una vez encontremos un numero que sea tanto multiplo de 3 como de 5
            # sustituimos este numero por la palabras correspodientes
            listado = listado + m3 + m5 + "\n"

        elif i % 3 == 0:
            # una vez encontramos un numero que es multiplo de 3
            # lo sustituimos por la palabra correspondiente
            listado = listado + m3 + "\n"

        elif i % 5 == 0:
            # una vez encontramos un numero que es multiplo de 5
            # lo sustituimos por la palabra correspondiente
            listado = listado + m5 + "\n"

        else:
            # en cualquier otro caso imprimiremos el numero correspoondiente
            listado = listado + str(i) + "\n"

    return listado


print(fizzbuzz("fizz", "buzz", 1, 100))

# m3: palabra para multiplos de 3
# m5: palabras para multiplos de 5
# ri: numero inferior en el que quieres empezar el rango
# rs: numero superior en el que quieres teminar el rango
