######################匯入模組######################
import pygame
import sys
import os


####################定義函式######################
def bg_update():
    global bg_roll_x

    bg_roll_x = (bg_roll_x - 10) % bg_x
    screen.blit(img, (bg_roll_x - bg_x, 0))
    screen.blit(img, (bg_roll_x, 0))


def move_dino():
    global ds_y, ds_index
    ds_index = (ds_index - 1) % len(img_dinosaur)
    screen.blit(img_dinosaur[ds_index], (ds_x, ds_y))


####################初始化######################
os.chdir(sys.path[0])

pygame.init()
LIMIT_LOW = 140
clock = pygame.time.Clock()

####################載入圖片物件######################
img = pygame.image.load("bg.png")
img_dinosaur = [pygame.image.load("小恐龍1.png"), pygame.image.load("小恐龍2.png")]

bg_x = img.get_width()
bg_y = img.get_height()
bg_roll_x = 0

######################建立視窗######################
screen = pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption("Dinosaur")
######################分數物件######################

######################恐龍物件######################
ds_x = 50
ds_y = LIMIT_LOW
ds_index = 0
jumpState = False
jumpValue = 0
jump_height = 13

######################仙人掌物件######################

######################循環偵測######################
while True:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    bg_update()
    move_dino()
    pygame.display.update()