from PPlay.window import *
from PPlay.sprite import *
from PPlay.collision import *
from PPlay.keyboard import *
import os
import ctypes
janela = Window(1920,1080)
janela.set_title("pong")
#janela.set_fps(60)
ctypes.windll.user32.SetProcessDPIAware()

#bola = Sprite("bola.png")
#barra1 = Sprite("Barra.png")
#barra2 = Sprite("Barra.png")
import sys
if getattr(sys, 'frozen', False):
    base = sys._MEIPASS
else:
    base = os.path.dirname(os.path.abspath(__file__))



bola = Sprite(os.path.join(base, "bola.png"))
barra1 = Sprite(os.path.join(base, "barra.png"))
barra2 = Sprite(os.path.join(base, "barra.png"))
barra1.set_position(barra1.width,janela.height/2 - (barra1.height)/2)
barra2.set_position(janela.width - 2*barra2.width,janela.height/2 - barra2.height/2)
x = janela.width/2-(bola.width)/2
y = (janela.height)/2 - (bola.height)/2
vel_x = 400
vel_y = 200
cont1 = 0
cont2 = 0
fps = 0
frames = 0
tempo_fps = 0
teclado = Window.get_keyboard()


def movimento():
    global x,y,dt,vel_x,vel_y
    x += vel_x*dt
    y += vel_y*dt
    
def colisão():
    global x,y,janela,bola,barra1,barra2,vel_x,vel_y
    if y <= 0 or y >= janela.height - bola.height :
        vel_y *= 1.05
        vel_y *= -1
    if Collision.collided_perfect(bola,barra1):
        vel_x *= 1.05
        vel_x *= -1
        x = barra1.x + barra1.width + 1
    if Collision.collided_perfect(bola,barra2):
        vel_x *= (1.05)
        vel_x *= -1
        x = barra2.x - barra2.width - 1
def pontuação():
    global cont1,cont2,bola,x,y,janela
    if bola.x <= 0:
        cont2 +=1
        restart()
    if bola.x > janela.width - bola.width:
        cont1 +=1
        restart()
    
def restart():
    global x,y,vel_x,vel_y
    x = janela.width/2-(bola.width)/2
    y = (janela.height)/2 - (bola.height)/2
    barra1.set_position(barra1.width,janela.height/2 - (barra1.height)/2)
    barra2.set_position(janela.width - 2*barra2.width,janela.height/2 - barra2.height/2)

    vel_x = 200
    vel_y = 200
def inp():
    global teclado,vel_barra,barra1,y,janela
    if teclado.key_pressed("W") and barra1.y >= 0:
        barra1.y -= vel_barra
    elif teclado.key_pressed("S") and barra1.y <= janela.height - barra1.height:
        barra1.y += vel_barra
def iabarra():
    global y
    vel_barra2 = 400*dt
    centro_barra2 = barra2.y + (barra2.height/2)
    centro_bola = y + (bola.height / 2)
    if barra2.y <= janela.height - barra2.height or barra2.y >= 0 :
        if centro_barra2 < centro_bola:
            barra2.y += vel_barra2
        elif centro_barra2 > centro_bola:
            barra2.y -= vel_barra2
    

while True:
    janela.set_background_color((20,20,20))
    dt = janela.delta_time()
    tempo_fps += dt
    frames += 1

    if tempo_fps >= 1:
        fps = frames
        frames = 0
        tempo_fps = 0
    vel_barra = 600*dt
    movimento()
    bola.set_position(x,y)
    if y <= 0 or y >= janela.height - bola.height :
        vel_y *= 1.05
        vel_y *= -1
    if bola.collided(barra1) or bola.collided(barra2):
        vel_x *= -1
        
        if bola.collided(barra1):
            bola.x = barra1.x + barra1.width + 1
        else:
            bola.x = barra2.x - barra2.width - 1

    iabarra()
    pontuação()
    inp()
    if teclado.key_pressed("SPACE"):
        break
    janela.draw_text(str(cont1), janela.width/4, 50, size=60, color=(255, 255, 255))
    janela.draw_text(str(cont2), (janela.width/4)*3, 50, size=60, color=(255, 255, 255))
    bola.draw()
    barra1.draw()
    barra2.draw()
    janela.draw_text(
    f"FPS: {fps}",
    10,
    10,
    size=30,
    color=(255,255,255),
    font_name="Arial",
    bold=True
)
    janela.update()