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

pa.alert("Antes de comenzar eliminaremos el archivo SKU de la TP\n\nAsegurate que la TP este conectada antes de saltar este mensaje","Eliminacion de archivo SKU en TP")
os.startfile('C:')
clipboard.copy("Equipo/tp1/\/My Documents/Datos_TP")
time.sleep(1.5)
pa.press('f4')#precionamos la tecla f4
time.sleep(1.0)
pa.press("esc")#precionamos la tecla escape
time.sleep(1.0)#precionamos el conjunto de teclas ctl + v
pa.hotkey("ctrlleft","v")
time.sleep(1.0)
pa.press("enter")#enter
time.sleep(1.0)
pa.hotkey("ctrlleft","e")#precinamos el conjunto de teclas ctl + e
pa.press("delete")#precionamos la tecla suprimir
pa.press("enter")#enter
time.sleep(1.0)
os.startfile('C:\Inventario')
time.sleep(1.0)
pa.hotkey("ctrlleft","e")#precinamos el conjunto de teclas ctl + e
time.sleep(1.0)
#dar click derecho sobre los archivos
r = None
while r is None:
    r = pa.locateOnScreen('images\copy.PNG', grayscale = True,confidence=0.5 )
pa.rightClick(r)
time.sleep(1.0)
#dar click en copiar
s = None
while s is None:
    s = pa.locateOnScreen('images\copy3.PNG' )
pa.click(s)
time.sleep(1.0)
pa.keyDown('alt')
pa.press('tab')
pa.keyUp('alt')
#pa.hotkey("altleft","tab")
time.sleep(1.0)
pa.keyDown('ctrlleft')
pa.press('v')
pa.keyUp('ctrlleft')
time.sleep(1.0)
pa.hotkey("alt","f4") #cerrar pantalla de la tp
pa.hotkey("alt","f4") #cerrar pantalla de la tp
#El programa realiza la carga de los archivos generados a la tp
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
    pa.alert("Antes de comenzar conecta la nueva Tp para poder eliminar y cargar su informacion")
    os.startfile('C:')
    clipboard.copy("Equipo/tp1/\/My Documents/Datos_TP")
    time.sleep(1.5)
    pa.press('f4')#precionamos la tecla f4
    time.sleep(1.0)
    pa.press("esc")#precionamos la tecla escape
    time.sleep(1.0)#precionamos el conjunto de teclas ctl + v
    pa.hotkey("ctrlleft","v")
    time.sleep(1.0)
    pa.press("enter")#enter
    time.sleep(1.0)
    pa.hotkey("ctrlleft","e")#precinamos el conjunto de teclas ctl + e
    pa.press("delete")#precionamos la tecla suprimir
    pa.press("enter")#enter
    time.sleep(1.0)
    os.startfile('C:\Inventario')
    time.sleep(1.0)
    pa.hotkey("ctrlleft","e")#precinamos el conjunto de teclas ctl + e
    time.sleep(1.0)
    #dar click derecho sobre los archivos
    r = None
    while r is None:
        r = pa.locateOnScreen('images\copy.PNG', grayscale = True,confidence=0.5 )
    pa.rightClick(r)
    time.sleep(1.0)
    #dar click en copiar
    s = None
    while s is None:
        s = pa.locateOnScreen('images\copy3.PNG' )
    pa.click(s)
    time.sleep(1.0)
    pa.keyDown('alt')
    pa.press('tab')
    pa.keyUp('alt')
    #pa.hotkey("altleft","tab")
    time.sleep(1.0)
    pa.keyDown('ctrlleft')
    pa.press('v')
    pa.keyUp('ctrlleft')
    time.sleep(1.0)
    pa.hotkey("alt","f4") #cerrar pantalla de la tp
    pa.hotkey("alt","f4") #cerrar pantalla de la tp
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
    pa.alert("Antes de comenzar conecta la nueva Tp para poder eliminar y cargar su informacion")
    os.startfile('C:')
    clipboard.copy("Equipo/tp1/\/My Documents/Datos_TP")
    time.sleep(1.5)
    pa.press('f4')#precionamos la tecla f4
    time.sleep(1.0)
    pa.press("esc")#precionamos la tecla escape
    time.sleep(1.0)#precionamos el conjunto de teclas ctl + v
    pa.hotkey("ctrlleft","v")
    time.sleep(1.0)
    pa.press("enter")#enter
    time.sleep(1.0)
    pa.hotkey("ctrlleft","e")#precinamos el conjunto de teclas ctl + e
    pa.press("delete")#precionamos la tecla suprimir
    pa.press("enter")#enter
    time.sleep(1.0)
    os.startfile('C:\Inventario')
    time.sleep(1.0)
    pa.hotkey("ctrlleft","e")#precinamos el conjunto de teclas ctl + e
    time.sleep(1.0)
    #dar click derecho sobre los archivos
    r = None
    while r is None:
        r = pa.locateOnScreen('images\copy.PNG', grayscale = True,confidence=0.5 )
    pa.rightClick(r)
    time.sleep(1.0)
    #dar click en copiar
    s = None
    while s is None:
        s = pa.locateOnScreen('images\copy3.PNG' )
    pa.click(s)
    time.sleep(1.0)
    pa.keyDown('alt')
    pa.press('tab')
    pa.keyUp('alt')
    #pa.hotkey("altleft","tab")
    time.sleep(1.0)
    pa.keyDown('ctrlleft')
    pa.press('v')
    pa.keyUp('ctrlleft')
    time.sleep(1.0)
    pa.hotkey("alt","f4") #cerrar pantalla de la tp
    pa.hotkey("alt","f4") #cerrar pantalla de la tp
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
    pa.alert("Antes de comenzar conecta la nueva Tp para poder eliminar y cargar su informacion")
    os.startfile('C:')
    clipboard.copy("Equipo/tp1/\/My Documents/Datos_TP")
    time.sleep(1.5)
    pa.press('f4')#precionamos la tecla f4
    time.sleep(1.0)
    pa.press("esc")#precionamos la tecla escape
    time.sleep(1.0)#precionamos el conjunto de teclas ctl + v
    pa.hotkey("ctrlleft","v")
    time.sleep(1.0)
    pa.press("enter")#enter
    time.sleep(1.0)
    pa.hotkey("ctrlleft","e")#precinamos el conjunto de teclas ctl + e
    pa.press("delete")#precionamos la tecla suprimir
    pa.press("enter")#enter
    time.sleep(1.0)
    os.startfile('C:\Inventario')
    time.sleep(1.0)
    pa.hotkey("ctrlleft","e")#precinamos el conjunto de teclas ctl + e
    time.sleep(1.0)
    #dar click derecho sobre los archivos
    r = None
    while r is None:
        r = pa.locateOnScreen('images\copy.PNG', grayscale = True,confidence=0.5 )
    pa.rightClick(r)
    time.sleep(1.0)
    #dar click en copiar
    s = None
    while s is None:
        s = pa.locateOnScreen('images\copy3.PNG' )
    pa.click(s)
    time.sleep(1.0)
    pa.keyDown('alt')
    pa.press('tab')
    pa.keyUp('alt')
    #pa.hotkey("altleft","tab")
    time.sleep(1.0)
    pa.keyDown('ctrlleft')
    pa.press('v')
    pa.keyUp('ctrlleft')
    time.sleep(1.0)
    pa.hotkey("alt","f4") #cerrar pantalla de la tp
    pa.hotkey("alt","f4") #cerrar pantalla de la tp
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
    pa.alert("Antes de comenzar conecta la nueva Tp para poder eliminar y cargar su informacion")
    os.startfile('C:')
    clipboard.copy("Equipo/tp1/\/My Documents/Datos_TP")
    time.sleep(1.5)
    pa.press('f4')#precionamos la tecla f4
    time.sleep(1.0)
    pa.press("esc")#precionamos la tecla escape
    time.sleep(1.0)#precionamos el conjunto de teclas ctl + v
    pa.hotkey("ctrlleft","v")
    time.sleep(1.0)
    pa.press("enter")#enter
    time.sleep(1.0)
    pa.hotkey("ctrlleft","e")#precinamos el conjunto de teclas ctl + e
    pa.press("delete")#precionamos la tecla suprimir
    pa.press("enter")#enter
    time.sleep(1.0)
    os.startfile('C:\Inventario')
    time.sleep(1.0)
    pa.hotkey("ctrlleft","e")#precinamos el conjunto de teclas ctl + e
    time.sleep(1.0)
    #dar click derecho sobre los archivos
    r = None
    while r is None:
        r = pa.locateOnScreen('images\copy.PNG', grayscale = True,confidence=0.5 )
    pa.rightClick(r)
    time.sleep(1.0)
    #dar click en copiar
    s = None
    while s is None:
        s = pa.locateOnScreen('images\copy3.PNG' )
    pa.click(s)
    time.sleep(1.0)
    pa.keyDown('alt')
    pa.press('tab')
    pa.keyUp('alt')
    #pa.hotkey("altleft","tab")
    time.sleep(1.0)
    pa.keyDown('ctrlleft')
    pa.press('v')
    pa.keyUp('ctrlleft')
    time.sleep(1.0)
    pa.hotkey("alt","f4") #cerrar pantalla de la tp
    pa.hotkey("alt","f4") #cerrar pantalla de la tp
elif opt == OPT_NO_CLOSE:
    pa.hotkey('alt', 'f4')
