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
pa.PAUSE=1
#seleccionamos la tecla derecha (inventario)
pa.press(['right','enter','enter',])
pa.press(['enter','enter','enter'])
pa.write('0020')
pa.press("enter")
pa.write('0020')
pa.press("enter")
pa.press("f10")
pa.press("enter")
pa.pause=4.0
#cerramos la cuenta de puty
pa.hotkey('alt', 'f4',)
pa.pause=4.0
pa.press("enter")
#ejecutamos el archivo bat que elimina los archivos antenieriores
subprocess.Popen(["C:\Inventario\delete.bat"])
#iniciarmos el programa de inventario para correr los archivos
pa.pause=1
subprocess.Popen(["C:\Sistemas\Inventario\Inv_Rec.bat"])
pa.pause=5
#abrimos el programa de comunicacion de la pc a una tp
subprocess.Popen(["C:\Program Files\Tec\Comunicacion_PDT_PC\Comunicacion_PDT_PC.exe"])
pa.pause=5
pa.hotkey('alt', 'tab')
pa.hotkey('alt', 'tab')
pa.alert("Por favor conecta la tp a la PC y espera que aparezca conectado... \r\n Cuando termine de conectar dar aceptar" ,  "Conectar la Tp a la PC")
#da click en la opcion
pa.click(x=546, y=204, duration=1.5)
pa.click(x=598, y=496, duration = 1.0)
pa.press("down")
pa.press("enter")
pa.PAUSE=2
#pa.click(x=593, y=195, duration=1.5)
pa.mouseDown(x=561, y=291, button='left', duration=1.0)
pa.mouseUp(x=579, y=191, button='left')
pa.press("enter")
pa.press("enter")
pa.hotkey('alt', 'f4')
#pregunta para volver a cargar otra tp
pregunta = print("¿Quieres volver a cargar otra tp ?")
print("s.Si n.NO")
primera = input("  Elija una opcion (s o n): ")
if primera == "s":
    #abrimos el programa de comunicacion de la pc a una tp
    subprocess.Popen(["C:\Program Files\Tec\Comunicacion_PDT_PC\Comunicacion_PDT_PC.exe"])
    pa.pause=5
    pa.hotkey('alt', 'tab')
    pa.hotkey('alt', 'tab')
    pa.alert("Por favor conecta la tp a la PC y espera que aparezca conectado... \r\n Cuando termine de conectar dar aceptar" ,  "Conectar la Tp a la PC")
    #da click en la opcion
    pa.click(x=546, y=204, duration=1.5)
    pa.click(x=598, y=496, duration = 1.0)
    pa.press("down")
    pa.press("enter")
    pa.PAUSE=2
    #pa.click(x=593, y=195, duration=1.5)
    pa.mouseDown(x=561, y=291, button='left', duration=1.0)
    pa.mouseUp(x=579, y=191, button='left')
    pa.press("enter")
    pa.press("enter")
    pa.hotkey('alt', 'f4')
    #pregunta para volver a cargar otra tp
    pregunta = print("¿Quieres volver a cargar otra tp ?")
    print("s.Si n.NO")
    primera = input("  Elija una opcion (s o n): ")
if primera == "s":
    #abrimos el programa de comunicacion de la pc a una tp
    subprocess.Popen(["C:\Program Files\Tec\Comunicacion_PDT_PC\Comunicacion_PDT_PC.exe"])
    pa.pause=5
    pa.hotkey('alt', 'tab')
    pa.hotkey('alt', 'tab')
    pa.alert("Por favor conecta la tp a la PC y espera que aparezca conectado... \r\n Cuando termine de conectar dar aceptar" ,  "Conectar la Tp a la PC")
    #da click en la opcion
    pa.click(x=546, y=204, duration=1.5)
    pa.click(x=598, y=496, duration = 1.0)
    pa.press("down")
    pa.press("enter")
    pa.PAUSE=2
    #pa.click(x=593, y=195, duration=1.5)
    pa.mouseDown(x=561, y=291, button='left', duration=1.0)
    pa.mouseUp(x=579, y=191, button='left')
    pa.press("enter")
    pa.press("enter")
    pa.hotkey('alt', 'f4')
    #pregunta para volver a cargar otra tp
    pregunta = print("¿Quieres volver a cargar otra tp ?")
    print("s.Si n.NO")
    primera = input("  Elija una opcion (s o n): ")
if primera == "s":
    #abrimos el programa de comunicacion de la pc a una tp
    subprocess.Popen(["C:\Program Files\Tec\Comunicacion_PDT_PC\Comunicacion_PDT_PC.exe"])
    pa.pause=5
    pa.hotkey('alt', 'tab')
    pa.hotkey('alt', 'tab')
    pa.alert("Por favor conecta la tp a la PC y espera que aparezca conectado... \r\n Cuando termine de conectar dar aceptar" ,  "Conectar la Tp a la PC")
    #da click en la opcion
    pa.click(x=546, y=204, duration=1.5)
    pa.click(x=598, y=496, duration = 1.0)
    pa.press("down")
    pa.press("enter")
    pa.PAUSE=2
    #pa.click(x=593, y=195, duration=1.5)
    pa.mouseDown(x=561, y=291, button='left', duration=1.0)
    pa.mouseUp(x=579, y=191, button='left')
    pa.press("enter")
    pa.press("enter")
    pa.hotkey('alt', 'f4')
    #pregunta para volver a cargar otra tp
    pregunta = print("¿Quieres volver a cargar otra tp ?")
    print("s.Si n.NO")
    primera = input("  Elija una opcion (s o n): ")
if primera == "s":
    #abrimos el programa de comunicacion de la pc a una tp
    subprocess.Popen(["C:\Program Files\Tec\Comunicacion_PDT_PC\Comunicacion_PDT_PC.exe"])
    pa.pause=5
    pa.hotkey('alt', 'tab')
    pa.hotkey('alt', 'tab')
    pa.alert("Por favor conecta la tp a la PC y espera que aparezca conectado... \r\n Cuando termine de conectar dar aceptar" ,  "Conectar la Tp a la PC")
    #da click en la opcion
    pa.click(x=546, y=204, duration=1.5)
    pa.click(x=598, y=496, duration = 1.0)
    pa.press("down")
    pa.press("enter")
    pa.PAUSE=2
    #pa.click(x=593, y=195, duration=1.5)
    pa.mouseDown(x=561, y=291, button='left', duration=1.0)
    pa.mouseUp(x=579, y=191, button='left')
    pa.press("enter")
    pa.press("enter")
    pa.hotkey('alt', 'f4')
    #pregunta para volver a cargar otra tp
    pregunta = print("¿Quieres volver a cargar otra tp ?")
    print("s.Si n.NO")
    primera = input("  Elija una opcion (s o n): ")
if primera == "s":
    #abrimos el programa de comunicacion de la pc a una tp
    subprocess.Popen(["C:\Program Files\Tec\Comunicacion_PDT_PC\Comunicacion_PDT_PC.exe"])
    pa.pause=5
    pa.hotkey('alt', 'tab')
    pa.hotkey('alt', 'tab')
    pa.alert("Por favor conecta la tp a la PC y espera que aparezca conectado... \r\n Cuando termine de conectar dar aceptar" ,  "Conectar la Tp a la PC")
    #da click en la opcion
    pa.click(x=546, y=204, duration=1.5)
    pa.click(x=598, y=496, duration = 1.0)
    pa.press("down")
    pa.press("enter")
    pa.PAUSE=2
    #pa.click(x=593, y=195, duration=1.5)
    pa.mouseDown(x=561, y=291, button='left', duration=1.0)
    pa.mouseUp(x=579, y=191, button='left')
    pa.press("enter")
    pa.press("enter")
    pa.hotkey('alt', 'f4')
    #pregunta para volver a cargar otra tp
    pregunta = print("¿Quieres volver a cargar otra tp ?")
    print("s.Si n.NO")
    primera = input("  Elija una opcion (s o n): ")
#cierre de la pregunta
if primera == "n":
    pa.alert("¡Eh terminado , preciona aceptar para cerrar el programa!", button="Aceptar")#pregunta al usuario si esta contento con lo que e hizo
