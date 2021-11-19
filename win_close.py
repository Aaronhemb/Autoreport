import mouse
from win32api import GetSystemMetrics

## Obtenemos el ancho de la pantalla
ancho_de_pantalla = GetSystemMetrics(0)
print("Ancho de pantalla =", GetSystemMetrics(0))

## Movemos el mouse al extremo superior derecho
mouse.move(x = ancho_de_pantalla, y = 5, absolute=True, duration=0.3)
## Cerramos la ventana al dar click en el boton de cerrar
mouse.click('left')
