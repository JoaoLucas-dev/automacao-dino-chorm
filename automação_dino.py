import pyautogui as pygui
import time 

pygui.PAUSE = 0.3
time.sleep(1)

print("Começando jogo automatizado")

# Abrir o Chrome
pygui.press("win")
time.sleep(0.5)
pygui.write("chrome")
time.sleep(0.5)
pygui.press("enter")
time.sleep(0.5)
pygui.click(x=739,y= 592)               



time.sleep(2)

# Abrir jogo do Dino
pygui.write("chrome://dino")
pygui.press("enter")

time.sleep(2)
pygui.press("space")  # iniciar jogo

# Bot do jogo
while True:
    recarga_img = pygui.screenshot(region=(744, 304, 80, 80))
    pixels = recarga_img.getcolors()

    for pixel in pixels:
        if pixel[1][0] < 100:
            pygui.press("space")
            break
                   