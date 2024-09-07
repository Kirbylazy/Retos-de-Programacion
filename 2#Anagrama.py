"""
 Escribe una función que reciba dos palabras (String) y retorne
 verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
"""


def anagrama(p1, p2):
    # Verificamos si las dos palabras tienen la misma longitud
    if len(p1) != len(p2):
        return False

    # Ordenamos las letras de ambas palabras y las comparamos
    return sorted(p1) == sorted(p2)


# Ejemplo de palabras
palabra1 = "roma"
palabra2 = "amor"

print(anagrama(palabra1, palabra2))
