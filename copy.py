import os # libreria que me permite dar direccion a exe
import subprocess
import pyautogui
import pyautogui as pa #se renombra para que sea mas facil la escritura
import mouse

from win32api import GetSystemMetrics


subprocess.Popen(["C:\Program Files\Tec\Comunicacion_PDT_PC\Comunicacion_PDT_PC.exe"])
pa.hotkey('alt', 'tab')
pa.alert("Por favor conecta la tp a la PC y espera que aparezca conectado... \r\n Cuando termine de conectar dar aceptar" ,  "Conectar la Tp a la PC")
#da click en la opcion
pa.click(x=546, y=204, duration=2.5)
pa.click(x=598, y=496, duration = 1.0)
pa.press("down")
pa.press("enter")
#pa.click(x=593, y=195, duration=1.5)
pa.mouseDown(x=561, y=291, button='left')
pa.mouseUp(x=579, y=191, button='left')
pa.press("enter")
pa.press("enter")
pa.hotkey('alt', 'f4')
