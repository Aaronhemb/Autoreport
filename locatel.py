import pyautogui as pa
import cv2
import time

"""r = None
while r is None:
    r = pa.locateOnScreen('inventario4.PNG', grayscale = True,confidence=0.5 )
    print (r)"""
"""time.sleep(1.0)
pa.write("128", interval = 1.0)
#print(pa.locateOnScreen('enviar.PNG'))
pa.click('recibi_inv.PNG')"""

r = None
while r is None:
    r = pa.locateOnScreen('putty.PNG', grayscale = True,confidence=0.5 )
    print(r)
    pa.click(r)
