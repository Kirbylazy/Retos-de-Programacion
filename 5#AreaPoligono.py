"""
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""


def calcula_poligono(poligono, unidades):

    if poligono == 1:

        dato1 = int(input("Dime cual es la Base de tu triangulo\n"))
        dato2 = int(input("Dime cual es la Altura de tu triangulo\n"))

        resultado = str((dato1*dato2)/2)

        respuesta = "Tu triangulo tiene un area de " + resultado + unidades + "2"

    else:

        dato1 = int(input("Dime la medida de uno de los lados\n"))
        dato2 = int(input("Dime la medida del otro lado\n"))
        resultado = str(dato1 * dato2)

        if poligono == 2:

            respuesta = "Tu cuadrado tiene un area de " + resultado + unidades + "2"

        else:

            respuesta = "Tu rectangulo tiene un area de " + resultado + unidades + "2"

    return respuesta


polygon = int(input("Dime que tipo de Poligono tienes\n"
                    "[1] Triangulo\n"
                    "[2] Cuadrado\n"
                    "[3] Rectangulo\n"))

unit = input("Dime en que unidades vas a darme todos los datos\n")

print(calcula_poligono(polygon, unit))
