"""
Programa para generar teoricos automaticamente

Autor: Aaron Hernandez
"""
import os # libreria que me permite dar direccion a exe
import subprocess
import pyautogui #control teclado
import pyautogui as pa #se renombra para que sea mas facil la escritura
import random
import autopy
import mouse #control mouse
import sys #mandar a llamar herramientas del sistema windows
import time # para poder dar pausas al programa
import pyperclip as clipboard #guarda en nuestros porta papeles informacion que queramos copiar
from win32api import GetSystemMetrics

pa.alert("Antes de comenzar eliminaremos el archivo SKU de la tp para no duplicar informacion en la tp")
os.startfile('C:')
clipboard.copy("Equipo/tp1/\/My Documents/Datos_TP")
time.sleep(1.5)
#precionamos la tecla f4
pa.press('f4')
#precionamos la tecla retroceso
ps.press("delete")
ps.press("Eliminar")
ps.press("Eliminar")
#precionamos el conjunto de teclas ctl + v
#enter
#precinamos el conjunto de teclas ctl + e
#precionamos la tecla suprimir
#enter



#pinche imbecil no olvides que las teclas ctl + e seleccionan todos los archivos de la carpeta para eliminarlos jajajajaja tontooooooooo
"""
#El programa realiza la carga de los archivos generados a la tp
subprocess.Popen(["C:\Program Files\Tec\Comunicacion_PDT_PC\Comunicacion_PDT_PC.exe"]) #Se envia a llamar al programa que nos permite cargar las tp con windows mobile
#realizamos una espera de opcion ya que nos debe de aparecer conectado y el tiempo dependera del usuario
pa.alert("Conectar la TP a la PC para poder realizar la tranferencia de archivos \r\n" "una vez indique que esta conectado dar clic en boton aceptar", "Conexion de TP a PC")
pa.click(x=542, y=209,duration=1.5)
time.sleep(1.0)
    #pa.click(x=524, y=202)
    #seleccionaremos los archivos txt
pa.mouseDown(x=576, y=306, button='left')
pa.mouseUp(x=584, y=200, button='left', duration=1.0)
time.sleep(1.0)
    #se confirman y se envian los archivos a las tp
pa.press("enter")
pa.press("enter")
pa.hotkey('alt', 'f4')
    #Cuestionamos si requieren gacer una carga de archivos mas
    # Botones.
OPT_YES = "Sí, Cargar una Tp"
OPT_NO_CLOSE = "Cerrar"
    # Crear el mensaje.
opt = pa.confirm(
    "¿Deses cargar una TP?",
    "Confirmación",
    [OPT_YES, OPT_NO_CLOSE]
)

#bucle de las opciones
if opt == OPT_YES:
    subprocess.Popen(["C:\Program Files\Tec\Comunicacion_PDT_PC\Comunicacion_PDT_PC.exe"])
    pa.alert("Conectar la TP a la PC para poder realizar la tranferencia de archivos \r\n" "una vez indique que esta conectado dar clic en boton aceptar", "Conexion de TP a PC")
    pa.click(x=542, y=209,duration=1.5)
    time.sleep(1.0)
    #pa.click(x=524, y=202)
    #seleccionaremos los archivos txt
    pa.mouseDown(x=576, y=306, button='left')
    pa.mouseUp(x=584, y=200, button='left', duration=1.0)
    time.sleep(1.0)
    #se confirman y se envian los archivos a las tp
    pa.press("enter")
    pa.press("enter")
    pa.hotkey('alt', 'f4')

    opt = pa.confirm(
        "¿Deses cargar otra TP?",
        "Confirmación",
        [OPT_YES, OPT_NO_CLOSE]
    )
if opt == OPT_YES:
    subprocess.Popen(["C:\Program Files\Tec\Comunicacion_PDT_PC\Comunicacion_PDT_PC.exe"])
    pa.alert("Conectar la TP a la PC para poder realizar la tranferencia de archivos \r\n" "una vez indique que esta conectado dar clic en boton aceptar", "Conexion de TP a PC")
    pa.click(x=542, y=209,duration=1.5)
    time.sleep(1.0)
    #pa.click(x=524, y=202)
    #seleccionaremos los archivos txt
    pa.mouseDown(x=576, y=306, button='left')
    pa.mouseUp(x=584, y=200, button='left', duration=1.0)
    time.sleep(1.0)
    #se confirman y se envian los archivos a las tp
    pa.press("enter")
    pa.press("enter")
    pa.hotkey('alt', 'f4')

    opt = pa.confirm(
        "¿Deses cargar otra TP?",
        "Confirmación",
        [OPT_YES, OPT_NO_CLOSE]
    )
if opt == OPT_YES:
    subprocess.Popen(["C:\Program Files\Tec\Comunicacion_PDT_PC\Comunicacion_PDT_PC.exe"])
    pa.alert("Conectar la TP a la PC para poder realizar la tranferencia de archivos \r\n" "una vez indique que esta conectado dar clic en boton aceptar", "Conexion de TP a PC")
    pa.click(x=542, y=209,duration=1.5)
    time.sleep(1.0)
    #pa.click(x=524, y=202)
    #seleccionaremos los archivos txt
    pa.mouseDown(x=576, y=306, button='left')
    pa.mouseUp(x=584, y=200, button='left', duration=1.0)
    time.sleep(1.0)
    #se confirman y se envian los archivos a las tp
    pa.press("enter")
    pa.press("enter")
    pa.hotkey('alt', 'f4')

    opt = pa.confirm(
        "¿Deses cargar otra TP?",
        "Confirmación",
        [OPT_YES, OPT_NO_CLOSE]
    )

elif opt == OPT_NO_CLOSE:
    pa.hotkey('alt', 'f4')
"""
