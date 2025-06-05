#En este ejercicio, tendrán total libertad para elegir la problemática y la mejor solución. 
# Cada grupo podrá decidir su propio enfoque y desarrollar el software según sus criterios. 
# El grupo que presente la mejor solución será el único en recibir los 60 puntos asignados a esta pregunta.
#¡Buena suerte!
import pyautogui as spam
from time import sleep

limitmsg = input('Número de mensajes: ')
msg = input('Mensaje: ')

if not limitmsg.isdigit():
    print("Por favor ingresa un número válido.")
    exit()

sleep(3)  

for i in range(int(limitmsg)):
    spam.typewrite(msg)
    spam.press('enter')
    sleep(0.4) 