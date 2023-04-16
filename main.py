from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image) , (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed


hero1 = Player("rocet.jpg", 5, 50, 5, 30, 100)
hero2 = Player("rocet.jpg", 675, 450, 5, 30, 100)
ball =GameSprite("shar.jpg", 300,300, 5,15, 15)
speed_x = 3
speed_y = 3

clock = time.Clock()
window = display.set_mode((700, 500))

game = True
while game:
    ball.rect.y += speed_y
    ball.rect.x += speed_x


    window.fill((200,255,255))

    hero1.update_l()
    hero1.reset()
    hero2.update_r()
    hero2.reset()
    ball.update()
    ball.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False



    display.update()
    clock.tick(60)
