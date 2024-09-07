"""
 Crea un programa que cuente cuantas veces se repite cada palabra
 y que muestre el recuento final de todas ellas.
 - Los signos de puntuación no forman parte de la palabra.
 - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 - No se pueden utilizar funciones propias del lenguaje que
   lo resuelvan automáticamente.
 """
 
import string

def contar_palabras(texto):
    # Función para limpiar las palabras de signos de puntuación
    def limpiar_palabra(palabra):
        return palabra.strip(string.punctuation)

    # Convertir el texto a minúsculas
    texto = texto.lower()

    # Reemplazar signos de puntuación y dividir el texto en palabras
    palabras = texto.split()
    
    # Crear un diccionario para contar las palabras
    conteo_palabras = {}

    for palabra in palabras:
        palabra_limpia = limpiar_palabra(palabra)
        if palabra_limpia:  # Verificar que la palabra no esté vacía
            if palabra_limpia in conteo_palabras:
                conteo_palabras[palabra_limpia] += 1
            else:
                conteo_palabras[palabra_limpia] = 1

    return conteo_palabras

# Ejemplo de uso
texto = "Hola, hola mundo. Este es un ejemplo de cómo contar palabras. Mundo, hola."
conteo = contar_palabras(texto)

# Mostrar el resultado
for palabra, cantidad in conteo.items():
    print(f"La palabra '{palabra}' aparece {cantidad} veces.")