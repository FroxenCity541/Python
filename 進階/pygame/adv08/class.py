######################匯入模組######################
import pygame
import sys
import os
from pygame.locals import *


####################定義函式######################
def bg_update():
    global bg_roll_x

    bg_roll_x = (bg_roll_x - 10) % bg_x
    screen.blit(img, (bg_roll_x - bg_x, 0))
    screen.blit(img, (bg_roll_x, 0))


def move_dino():
    global ds_y, jumpState, jumpValue, ds_index
    if jumpState:
        if ds_y >= LIMIT_LOW:
            jumpValue = -jump_height
        if ds_y <= 0:
            jumpValue = jump_height
        ds_y += jumpValue

        if jumpValue < 0:
            jumpValue += 1
        else:
            jumpValue += 1

        if ds_y >= LIMIT_LOW:
            jumpState = False
            ds_y = LIMIT_LOW

    ds_index = (ds_index - 1) % len(img_dinosaur)
    screen.blit(img_dinosaur[ds_index], (ds_x, ds_y))


def move_cacti():
    global cacti_x, score

    cacti_x = (cacti_x - cacti_shift) % (bg_x - 100)
    screen.blit(img_cacti, (cacti_x, cacti_y))

    if cacti_x == 0:
        score += 1


def score_update():
    score_sur = score_font.render(str(score), True, RED)
    screen.blit(score_sur, [10, 10])


####################初始化######################
os.chdir(sys.path[0])

pygame.init()
LIMIT_LOW = 140
clock = pygame.time.Clock()
RED = (255, 0, 0)

####################載入圖片物件######################
img = pygame.image.load("bg.png")
img_dinosaur = [pygame.image.load("小恐龍1.png"), pygame.image.load("小恐龍2.png")]
img_cacti = pygame.image.load("cacti.png")
bg_x = img.get_width()
bg_y = img.get_height()
bg_roll_x = 0

######################建立視窗######################
screen = pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption("Dinosaur")
######################分數物件######################
score = 0
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 36)
######################恐龍物件######################
ds_x = 50
ds_y = LIMIT_LOW
ds_index = 0
jumpState = False
jumpValue = 0
jump_height = 13

######################仙人掌物件######################
cacti_x = bg_x - 100
cacti_y = LIMIT_LOW
cacti_shift = 10

######################循環偵測######################
while True:
    clock.tick(20)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and ds_y <= LIMIT_LOW:
                jumpState = True

    bg_update()
    move_dino()
    move_cacti()
    score_update()
    pygame.display.update()