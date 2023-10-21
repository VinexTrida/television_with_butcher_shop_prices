import time
import webbrowser
import pyautogui

# Aguarda 20 segundos
time.sleep(20)

# Abre o Google
webbrowser.open("http://localhost:8000/programaAcougue.html")

# Espera um momento para o navegador abrir completamente
time.sleep(5)

# Simula a tecla F11
pyautogui.press('f11')
