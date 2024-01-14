from pygame import *


class Object(sprite.Sprite):
    def __init__(self,player_image,x,y,w,h,speed):
      super().__init__()
      self.image = transform.scale(image.load(player_image),(w,h))
      self.speed=speed  
      self.rect =self.image.get_rect()
      self.rect.x = x 
      self.rect.y = y

    def reset (self):
        window.blit(self.image,(self.rect.x,self.rect.y))

    def move(self):
        keys = key.get_pressed()
        if keys[K_a]and self.rect.x >0 :
            self.rect.x -= self.speed
            for w in walls:
                if sprite.collide_rect(hamster1,w):
                    self.rect.x += self.speed
        if  keys[K_w]and self.rect.y >0 :
            self.rect.y -= self.speed
            for w in walls:
                if sprite.collide_rect(hamster1,w):
                    self.rect.y += self.speed
        if keys[K_d]and self.rect.x <700 :
            self.rect.x += self.speed
            for w in walls:
                if sprite.collide_rect(hamster1,w):
                    self.rect.x -= self.speed
        if  keys[K_s]and self.rect.y <500 :
            self.rect.y += self.speed
            for w in walls:
                if sprite.collide_rect(hamster1,w):
                    self.rect.y -= self.speed

    direction = "right"
    def move2(self):
        if self.rect.x > 500:
            self.direction ="left"
        if self.rect.x < 100:
            self.direction ="right"  

        if self.direction == "right" :
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed 

    direction = "down"
    def move3(self):
        if self.rect.y > 500:
            self.direction ="down"
        if self.rect.y < 100:
            self.direction ="up"  

        if self.direction == "up" :
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed       

    def fire(self):
        bullet = Bullet('fire.png',self.rect.centerx,self.rect.centery,15,15,10)
        bullets.add(bullet)    




class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        # картинка стіни - прямокутник потрібних розмірів і кольору
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
        # кожен спрайт має зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

bullets = sprite.Group()

class Bullet(Object):
    def update(self): #функція пострілу праворуч
        self.rect.x += 10
        if self.rect.x > 1000:
            self.kill()



menu = display.set_mode((400,400))
display.set_caption("")

start_button=Rect(150,100,100,50)
exit_button=Rect(150,200,100,50)

font.init()
menu_font=font.Font( None,18)


mg = True
while mg:
    for e in event.get():
        if e.type == QUIT:
            mg = False
            game = False
        elif e.type == MOUSEBUTTONDOWN and e. button ==1:
            if exit_button.collidepoint(mouse.get_pos()):
                mg = False 
                game = False
            if start_button.collidepoint(mouse.get_pos()):
                mg = False 
                game = True
 
    menu.fill ((236,2,120))
    draw.rect(menu,(166,137,217),start_button)
    draw.rect(menu,(166,137,217),exit_button)

    start_text=menu_font.render("Почати гру", True, (0,0,0))
    exit_text=menu_font.render("Завершити гру", True, (0,0,0))
    menu.blit(start_text,(start_button.x+10, start_button.y+10))
    menu.blit(exit_text,(exit_button.x+10, exit_button.y+10))

    display.update()

display.quit()
display.init()


window =display.set_mode((800,600))
picture =transform.scale(image.load("images.jpg"),(800,600))

#створення персонажів
hamster1 =Object('hamter1.png',600,400,100,80,10)
hamster2 =Object('hamster2.png',100,200,100,70,5)
hamster3 =Object("hamster2.png",300,100,100,70,5)
hamster4 =Object("hamster2.png",500,100,100,70,5)
money=Object("money.png",600,100,100,80,80)

#створення стін
wall1 = Wall (186,85,211,0,100,800,10)
wall2 = Wall (255,182,193,50,100,10,800)
wall4 = Wall (186,85,211,700,100,10,200)
wall3 = Wall (255,182,193,250,300,600,10)

walls = []
walls.append(wall1)
walls.append(wall2)
walls.append(wall3)
walls.append(wall4)


clock = time.Clock()

x1,y1 = 100,100
x2,y2 = 100,200


lvl1 = True
lvl2 = False
while game:
    if lvl1:
        for e in event.get():
            if e.type == QUIT:
                game = False
            elif e.type == KEYDOWN:
                if e.key == K_SPACE:
                    hamster1.fire()

        window.blit(picture,(0,0))
        bullets.update()
        bullets.draw(window)
        hamster1.reset()
        hamster2.reset()
        hamster3.reset()
        hamster4.reset()
        money.reset()
        hamster1.move()
        hamster2.move2()
        hamster3.move3()
        hamster4.move3()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
    

        if sprite.collide_rect(hamster1,hamster2):
            game = False
        if sprite.spritecollide(hamster2,bullets,False): 
            hamster2.rect.y = -100
        if sprite.spritecollide(hamster3,bullets,False): 
            hamster3.rect.y = -100
        if sprite.spritecollide(hamster4,bullets,False): 
            hamster4.rect.y = -100
        ###############################
        if sprite.collide_rect(hamster1,money):
            lvl1 = False
            lvl2 = True 
            image2 =Object("images2.jpg",0,0,600,600,350)
            hamster1 =Object('hamter1.png',600,400,100,80,10)
            money2=Object("money2.png",550,100,300,300,300)

        ###############################


    
    if lvl2:
        for e in event.get():
            if e.type == QUIT:
                game = False
            elif e.type == KEYDOWN:
                if e.key == K_SPACE:
                    hamster1.fire()

        window.blit(picture,(0,0))
        bullets.update()
        bullets.draw(window)
        hamster1.reset()
        money2.reset()
        image2.reset()
        hamster1.move()


    
    
    display.update()
    clock.tick(60)
