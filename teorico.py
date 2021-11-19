"""
Programa para generar teoricos automaticamente

Autor: Aaron Hernandez
"""
#librerias
import os # libreria que me permite dar direccion a exe
import subprocess
import pyautogui
import pyautogui as pa #se renombra para que sea mas facil la escritura
import random
import mouse
import sys
import remove
from win32api import GetSystemMetrics

#alerta para ejecutar el programa

pa.alert("¡Se comenzara a trabajar! \r\n\r\n Porfavor presiona boton aceptar", "¡NO INTERRUMPAS!")
#iniciamos el programa de puty
subprocess.Popen(["C:\Soporte_tda\Emuladores\Putty\putty.exe"])
pa.doubleClick(x=652, y=413, duration=0.7)
pa.PAUSE= 1
#se comenta por que no (siempre estara el programa en el mismo lugar)
#abre el primer programa
#mouse.move(x=647, y=751, absolute=True, duration=0.8)
#mouse.click('left')
#mouse.move(x=652, y=413, duration=0.8)
#ejecuta la session de genesix
#pa.doubleClick(x=652, y=413, duration=0.7)
#escribimos usuario
pa.write('gxain128' , interval=0.50)
pa.press("enter")
#escribimos contraseña
mouse.move(x=652, y=413, duration=0.8)
pa.write('Oct128sa' , interval=1.0)
pa.press("enter")
#ingresamos una opcion (inventario fisico)
pa.PAUSE= 1
pa.press('6')
pa.press("enter")
#ingresamos a segunda opcion (generar archivos para escaner)
pa.press('1',)
pa.press("enter")
#seleccionamos impresora
pa.press('down')
pa.press('down')
pa.press('down')
pa.press("f10")
pa.PAUSE= 1
#seleccionamos la tecla derecha (inventario)
pa.press(['right','enter','enter',])
pa.press(['enter','enter','enter'])
pa.write('0020')
pa.press("enter")
pa.write('0020')
pa.press("enter")
pa.press("f10")
pa.press("enter")
pa.pause= 1
#cerramos la cuenta de puty
pa.hotkey('alt', 'f4')
pa.press("enter")
pa.pause= 1

#iniciarmos el programa de inventario para correr los archivos
subprocess.Popen(["C:\Sistemas\Inventario\Inv_Rec.bat"])

pa.pause= 1


#pregunta al usuario si esta contento con lo que e hizo
pa.alert("¡Eh terminado , preciona aceptar para cerrar el programa!", button="Aceptar")
