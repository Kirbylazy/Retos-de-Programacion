"""
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

texto = "Hola mundo"
texto_invertido = ""

for char in texto:
    texto_invertido = char + texto_invertido
    
print(texto_invertido)