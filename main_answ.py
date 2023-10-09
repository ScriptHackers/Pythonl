from pygame import *
'''Необхідні класи'''
 
#клас-батько для спрайтів
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        #кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (150, 80))
        self.speed = player_speed
        #кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
class Enemy(GameSprite):
    direction = "left"


    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"


        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
#Ігрова сцена:
win_width = 700
win_height = 500


window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("C:\\Users\\111\\Desktop\\prog\\папка\\Flag_of_Israel.svg.png"), (win_width, win_height))
 
#Персонажі гри:
player = Player('C:\\Users\\111\\Desktop\\prog\\папка\\Picsart_23-09-11_17-06-52-568.png', 5, win_height - 80, 4)
monster = Enemy('C:\\Users\\111\\Desktop\\prog\\папка\\Untitled2_20230911180737-removebg-preview.png', win_width - 80, 280, 2)
final = GameSprite('папка\\Picsart_23-09-11_17-12-17-750.png', win_width - 120, win_height - 80, 0)


player.update()
monster.update()

game = True
clock = time.Clock()
FPS = 60


#музика
mixer.init()
mixer.music.load('C:\\Users\\111\\Desktop\\prog\\папка\\jungles.ogg')
mixer.music.play()
 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    window.blit(background,(0, 0))
    player.reset()
    player.update()

    monster.reset()
    monster.update()
    final.reset()




    display.update()
    clock.tick(FPS)
