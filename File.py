import pygame
import random

GREEN = (0, 169, 2)
BLUE = (29, 32, 76)
YELLOW = (208, 169, 2)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, img='Men.png'):
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.change_x = 0
        self.change_y = 0
        self.walls = None

        self.coins = None
        self.collected_coins = 0

        self.enemies = pygame.sprite.Group()
        self.alive = True

    def update(self):

        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        
        self.rect.y += self.change_y
        coins_hit_list = pygame.sprite.spritecollide(self, self.coins, False)
        for coin in coins_hit_list:
            self.collected_coins += 1
            coin.kill()
        
        if pygame.sprite.spritecollideany(self, self.enemies, False):
            self.alive = False

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(BLUE)


        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect y = y


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, img='coin.png')
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, img='aligator.png')
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 
        self.start = x 
        self.stop = x + random.randint(180, 240)
        self.direction = 1

    def update(self):
        if self.rect.x >= self.stop:
            self.rect.x = self.stop
            self.direction = -1

    def update(self):
        if self.rect.x <= self.start:
            self.rect.x = self.start
            self.direction = 1
        self.rect.x += self.direction * 2



pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption('Maze')


all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

wall_coords = [
    [0, 0, 10, 600],
    [790, 0, 10, 600],
    [10, 0, 790, 10],
    [0, 200, 100, 10],
    [0, 590, 600, 10],
    [450, 400, 10, 200],
    [550, 450, 250, 10]
]

for coord in wall_coords:
    wall = Wall(coord[0], coord[1], coord[2], coord[3])
    wall_list.add(wall)
    all_sprite_list.add(wall)

coins_list = pygame.sprite.Group()
coins_coord = [[100, 140], [236, 50], [400, 234]]

for coord in enemies.coord:
    enemy = Enemy(coord[0], coord [1])
    enemies_list.add(enemy)
    all_sprite_list.add(enemy)

player = Player(50, 50)
player.walls = wall_list
all_sprite_list.add(player)

player.coins = coins_list
player.enemies = enemies_list



font = pygame.font.SysFont(Arial, 24, True)
text = font.render('Гру закінчено!', True, YELLOW)
text_win = font.render('Лабіринт пройдено, молодець!', True, YELLOW)

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_x = -3
            elif event.key == pygame.K_RIGHT:
                player.change_x = 3
            elif event.key == pygame.K_UP:
                player.change_y = -3
            elif event.key == pygame.K_DOWN:
                player.change_y = 3

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.change_x = 0
             elif event.key == pygame.K_RIGHT:
                player.change_x = 0
            elif event.key == K_UP:
                player.change_y = 0
            elif event.key == pygame.K_DOWN:
                player.change_y = 0

    screen.fill(GREEN)

    if not player.alive:
        screen.blit(text, (100, 100))
    else:
        all_sprite_list.update()
        all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit() 