from pygame import *

window =display.set_mode((800,600))
picture =transform.scale(image.load("images.jpg"),(800,600))
hamter1 =transform.scale(image.load("hamter1.png"),(180,160))
hamster2 =transform.scale(image.load("hamster2.png"),(180,160))

clock = time.Clock()
x1,y1 = 100,100
x2,y2 = 100,200
game=True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    window.blit(picture,(0,0))
    window.blit(hamter1,(x1,y1))
    window.blit(hamster2,(x2,y2))

    key_pressed = key.get_pressed()
    if key_pressed[K_LEFT]:
        x1-= 5 
    if key_pressed[K_RIGHT]:
        x1+= 5 
    if key_pressed[K_DOWN]:
        y1-= 5 
    if key_pressed[K_UP]:
        y1+= 5 

    if key_pressed[K_1]:
        x2-= 5 
    if key_pressed[K_2]:
        x2+= 5 
    if key_pressed[K_3]:
        y2-= 5 
    if key_pressed[K_4]:
        y2+= 5

    display.update()
    clock.tick(60)
