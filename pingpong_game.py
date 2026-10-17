from pygame import *
from random import randint

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Space Shoot')
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))

game = True
final = False
clock = time.Clock()
FPS = 60
speed = 7

ont.init()
style = font.SysFont('Arial', 36)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, self.rect)

  class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        
    def update(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.left > 0:
            self.rect.x -= self.speed

        if keys[K_DOWN] and self.rect.right < win_width:
            self.rect.x += self.speed

player1 = Player("Alien1.png", 150, 425, speed)
player2 = Player("Alien2.png", 150, 200, speed)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            if not final:
                window.blit(background, (0, 0))
                player1.update()
                player2.update()
                player1.reset()
                player2.reset()
    display.update()
    clock.tick(FPS)
quit()



                 
