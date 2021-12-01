import time

print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")





"""#Para el inicio o la confirmacion de las cosas
# Botones.
OPT_CLOSE = "Sí, cerrar"
OPT_SAVE_AND_CLOSE = "Guardar todo y cerrar"
OPT_KEEP_WORKING = "No, seguir trabajando"
# Crear el mensaje.
opt = pyautogui.confirm(
    "¿Desea cerrar el programa?",
    "Confirmación",
    [OPT_CLOSE, OPT_SAVE_AND_CLOSE, OPT_KEEP_WORKING]
)
# Tomar decisión en base al botón presionado.
if opt == OPT_CLOSE:
    # ...
elif opt == OPT_SAVE_AND_CLOSE:
    # ...
elif opt == OPT_KEEP_WORKING:
    # ..."""
