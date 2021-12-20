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
import cv2
import shutil
import mouse #control mouse
import sys #mandar a llamar herramientas del sistema windows
import time # para poder dar pausas al programa
import win32com.client
import pyperclip as clipboard #guarda en nuestros porta papeles informacion que queramos copiar
from win32api import GetSystemMetrics
from win32com.client import Dispatch as comDispatch

#Antes de iniciar debe de preguntar si quieres descargar la tp
pa.alert("Antes de comenzar bajar los archivo teorico de la TP\n\nAsegurate que la TP este conectada antes de saltar este mensaje","Eliminacion de archivo SKU en TP")
os.startfile('C:') #abrimos la carpeta de la tp ya conectada
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
# Copiar el archio de la tp a inventario
r = None
while r is None:
    r = pa.locateOnScreen('images\inv06.PNG' )
pa.rightClick(r)
time.sleep(1.0)
#dar click en copiar
s = None
while s is None:
    s = pa.locateOnScreen('images\copy3.PNG' ) #busca la opcion de conectar
pa.click(s)
time.sleep(1.0)
os.startfile('C:\Inventario') #ingresa a la carpeta de inventario
time.sleep(1.0)
pa.keyDown('ctrlleft')
pa.press('v') #crontrol V para pegar el archivo
pa.keyUp('ctrlleft')
time.sleep(1.0)
pa.hotkey("alt","f4") #cerrar pantalla de la tp
time.sleep(1.0)
pa.hotkey("alt","f4")
#darle enviar a la carpeta roja
time.sleep(1.5)
m = None
while m is None:
    m = pa.locateOnScreen('images\inventario3.PNG', grayscale = True,confidence=0.5 )
pa.click(m)
time.sleep(2.0)
pa.write("128", interval = 1.0)
#dar click al boton de la carpeta roja
pa.click('images\enviar.PNG')
time.sleep(1.5)
#entrar a genesix y cargar las 2 opciones
r = None
while r is None:
    r = pa.locateOnScreen('images\putty.PNG', grayscale = True,confidence=0.5 )
pa.click(r)
time.sleep(1.0)
s = None
while s is None:
    s = pa.locateOnScreen('images\session.PNG', grayscale = True,confidence=0.5 )
pa.doubleClick(s)
time.sleep(1.5)
#escribimos el usuario
f = open ('../usuario.txt','r')
mensaje = f.read()
pa.write(mensaje, interval=0.5)

pa.press("enter")
#escribimos contraseña
time.sleep(1.5)
f = open ('../password.txt','r')
mensaje = f.read()
pa.write(mensaje, interval=0.5)
f.close()
pa.press("enter")
time.sleep(2.5)
pa.press('6')
pa.press("enter")
#ingresamos a segunda opcion (procesar informacion fisica gnx)
pa.press('3')
pa.press("enter")
time.sleep(1.0)
pa.press("enter")#ingresamos a la opcion de procsar en gnx
pa.press("f10") #Saltamos la opcion de criterios de seleccion
time.sleep(1.0)
pa.press("enter")#aceptamos los criterio
time.sleep(1.5)
time.sleep(1.5)
time.sleep(1.5)
time.sleep(1.5)
pa.press('right') #salimos de la ruta de genesix e ingresamos a otra para descargar existencias
pa.press('enter')
pa.press('5')
pa.press('enter')
time.sleep(1.0)
pa.press('down')
pa.press('down')
pa.press('down')
pa.press('down')
pa.press("f10")
time.sleep(1.0)
pa.press('right')
pa.press('enter')
pa.press('enter')
pa.press('f10')
pa.press('enter')
time.sleep(1.0)
pa.press(['right','enter'])
time.sleep(4.0)
t = None
while t is None:
    t = pa.locateOnScreen('images\gnx1.PNG',confidence=0.5 )
    print('exito')
time.sleep(1.5)
os.startfile('baja.bat') #se corre el bat de baja para tener la informacion
time.sleep(2.5)
os.startfile('..\Teorico.xlsm') #se ejecuta el archivo Teoricos
#se inicia a convertir el archivo de txt a excel (el cual esta programado con macros)

time.sleep(2.0) #se preciona el boton reset para poder eliminar informacion en caso de que haya)

r = None
while r is None:
    r = pa.locateOnScreen('images\coor.PNG' ,grayscale = True, confidence=0.5 )
pa.click(r)
time.sleep(1.5)

os.startfile('TEORICOS.TXT') #se ejecutael txt oara agregar al excel
time.sleep(1.0)
pa.hotkey("ctrlleft","e") #Seleccionamos la informacion
time.sleep(1.0)
pa.hotkey("ctrlleft","x") #se cortan todos los archivos del txt
time.sleep(1.0)
pa.keyDown('alt')
pa.press('tab')
pa.keyUp('alt') #nos cambiamos a el excel de nuevo
time.sleep(1.0)
pa.hotkey("ctrlleft","v") #se pegan todos los documentos en la primer celda
time.sleep(2.5)

r = None
while r is None:
    r = pa.locateOnScreen('images\modar.PNG') #busca el primer boton
pa.click(r)
time.sleep(1.5)
d = None
while d is None:
    d = pa.locateOnScreen('images\carac.PNG') #busca el segundo boton
pa.click(d)
time.sleep(1.5)
pa.alert("La asitencia a terminado...\n\nProximamente tendras mas actualizaciones de este sistema, Si tienes alguna sugerencia envia correo a: \n\nrst0128@sears.com.mx","MSG Informativo")
