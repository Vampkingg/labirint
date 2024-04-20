from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (80, 80))
        self.speed = player_speed
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
        if keys[K_DOWN] and self.rect.y < win_heigth - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= - 10:
            self.direction = 'right'
        if self.rect.x >= win_width - 10:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2,  color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))        
win_width = 700
win_heigth = 700
window = display.set_mode(
    (win_heigth, win_width)
)
display.set_caption('Maze')
background = transform.scale(image.load('дотафон.jpg'), (win_heigth, win_width))

player = Player('images.png', 5, win_heigth - 100, 10)
enemy = Enemy('download.png', win_width - 500, 250, 15)
final = GameSprite('aa (1).png', win_width - 150, win_heigth - 680, 0)


w1 = Wall(154, 205, 50, 260, 340, 20, 350)
w2 = Wall(154, 205, 50, 100, 220, 20, 350)
w3 = Wall(154, 205, 50, 100, 220, 450, 20)
w4 = Wall(154, 205, 50, 10, 550, 100, 20)
w5 = Wall(154, 205, 50, 260, 340, 100, 20)
w6 = Wall(154, 205, 50, 360, 340, 20, 350)
w7 = Wall(154, 205, 50, 530, 90, 20, 500)
w8 = Wall(154, 205, 50, 530, 0, 20, 90)



font.init()
font = font.Font(None, 70)
win = font.render('U ARE A FK GOD<3!!', True, (225, 215, 0))
lose = font.render('WATAHEL???', True, (180, 0, 0))



mixer.init() 
mixer.music.load('jungles.ogg')
mixer.music.play()

speed = 1
game = True 
clock = time.Clock()
FPS = 1000
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        enemy.update()

        player.reset()
        enemy.reset()
        final.reset()
            

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()


    if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()

    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))
        money.play()

    display.update()
    clock.tick(FPS)