"""
Programa para generar teoricos automaticamente

Autor: Aaron Hernandez
"""
#librerias
import os # libreria que me permite dar direccion a exe
import subprocess
import pyautogui #control teclado
import pyautogui as pa #se renombra para que sea mas facil la escritura
import random
import autopy
import cv2
import mouse #control mouse
import sys #mandar a llamar herramientas del sistema windows
import time # para poder dar pausas al programa
from win32api import GetSystemMetrics
    #Cuestionamos si requieren gacer una carga de archivos mas
    # Botones.
OPT_YES = "Sí, estoy seguro"
OPT_NO_CLOSE = "No, Salir"
    # Crear el mensaje.
opt = pa.confirm(
    "¿Estas seguro que quieres descargar archivos para la tp?",
    "Confirmación",
    [OPT_YES, OPT_NO_CLOSE]
)
if opt == OPT_YES:
    #alerta para ejecutar el programa
    #pa.alert("¡Se comenzara a trabajar! \r\n\r\n Porfavor presiona boton aceptar", "¡NO INTERRUMPAS!")
    #iniciamos el programa de puty
    subprocess.Popen(["C:\delete\delete.bat"])
    time.sleep(1.0)
    #subprocess.Popen(["C:\Soporte_tda\Emuladores\Putty\putty.exe"])
    r = None
    while r is None:
        r = pa.locateOnScreen('images\putty.PNG', grayscale = True,confidence=0.5 )
    pa.click(r)
    time.sleep(1.0)
    s = None
    while s is None:
        s = pa.locateOnScreen('images\session.PNG', grayscale = True,confidence=0.5 )
    pa.doubleClick(s)
    #pa.locateOnScreen('session.PNG')
    #pa.doubleClick('session.PNG')
    time.sleep(1.5)
    #se comenta por que no (siempre estara el programa en el mismo lugar)
    #abre el primer programa
    #mouse.move(x=647, y=751, absolute=True, duration=0.8)
    #mouse.click('left')
    #mouse.move(x=652, y=413, duration=0.8)
    #ejecuta la session de genesix
    #pa.doubleClick(x=652, y=413, duration=0.7)
    #escribimos usuario
    f = open ('../usuario.txt','r')
    mensaje = f.read()
    pa.write(mensaje, interval=0.5)
    f.close()
    pa.press("enter")
    #escribimos contraseña
    #mouse.move(x=652, y=413, duration=0.8)
    time.sleep(1.5)
    time.sleep(1.5)
    f = open ('..\password.txt','r')
    mensaje = f.read()
    pa.write(mensaje , interval=0.5)
    f.close()
    pa.press("enter")
    #ingresamos una opcion (inventario fisico)
    time.sleep(2.5)
    pa.press('6')
    pa.press("enter")
    #ingresamos a segunda opcion (generar archivos para escaner)
    pa.press('1',)
    pa.press("enter")
    #seleccionamos impresora
    time.sleep(1.0)
    pa.press('down')
    pa.press('down')
    pa.press('down')
    pa.press("f10")
    time.sleep(1.0)
    #seleccionamos la tecla derecha (inventario)
    pa.press(['right','enter','enter',])
    pa.press(['enter','enter','enter'])
    pa.write('0020')
    pa.press("enter")
    pa.write('0020')
    pa.press("enter")
    pa.press("f10")
    pa.press("enter")
    time.sleep(4.5)
    #cerramos la cuenta de puty
    pa.hotkey('alt','f4')
    time.sleep(3.5)
    pa.press("enter")
    #ejecutamos el archivo bat que elimina los archivos antenieriores
    subprocess.Popen(["C:\delete\delete.bat"])
    #iniciarmos el programa de inventario para correr los archivos
    time.sleep(1.5)
    m = None
    while m is None:
        m = pa.locateOnScreen('images\inventario3.PNG', grayscale = True,confidence=0.5 )
    pa.click(m)
    #pa.locateOnScreen('inventario.PNG')
    #pa.click('inventario.PNG')
    time.sleep(2.0)
    pa.write("128", interval = 1.0)
    #pa.locateOnScreen('recibi_inv.PNG')
    r = None
    while r is None:
        r = pa.locateOnScreen('images\dar.PNG' )
    pa.click(r)
    time.sleep(1.5)
    #abrimos el programa de comunicacion de la pc a una tp
    pa.alert("¡Eh terminado , preciona aceptar para cerrar el programa!", button="Aceptar")#pregunta al usuario si esta contento con lo que e hizo

elif opt == OPT_NO_CLOSE:
    pa.hotkey('alt', 'f4')
