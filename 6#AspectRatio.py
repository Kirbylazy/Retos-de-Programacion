import requests
from PIL import Image
from io import BytesIO
import math

def aspect_ratio(url):
    try:
        # Descargar la imagen desde la URL
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))

        # Obtener dimensiones de la imagen
        width, height = image.size

        # Calcular el aspect ratio
        aspect_ratio = reducir_aspect_ratio(height, width)
        aspect_ratio_str = f"{aspect_ratio[1]}:{aspect_ratio[0]}"

        print(f"El aspect ratio es {aspect_ratio_str}")
    except Exception as e:
        print(f"No se ha podido calcular el aspect ratio: {e}")

def reducir_aspect_ratio(height, weidth):

    # Usamos la biblioteca de math para reducir el aspect ratio
    
    numerador = height
    denominador = weidth

    mcd = math.gcd(numerador, denominador)  # encontramos el minimo comun divisor de los dos numeros
    
    # Reducimos la fracción al minimo posible
    
    numerador = int(numerador/mcd)
    denominador = int(denominador/mcd)

    return [numerador, denominador]

# Ejemplo de uso
url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
aspect_ratio(url)