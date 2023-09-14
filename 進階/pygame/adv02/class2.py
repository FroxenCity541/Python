######################匯入模組######################
import pygame
import sys
import math
import os


####################定義函式######################
def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = x_min < pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


####################初始化######################
os.chdir(sys.path[0])
pygame.init()
bg_img = "snow.jpg"
bg = pygame.image.load(bg_img)

bg_x = bg.get_width()
bg_y = bg.get_height()

######################建立視窗######################
screen = pygame.display.set_mode((bg_x, bg_y))
pygame.display.set_caption("Snow")

####################撥放音樂######################
mp3_path = "snow-dream.mp3"
pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play()
pygame.mixer.music.fadeout(600000000)
####################設定文字######################
tpyxeface = pygame.font.get_default_font()
font = pygame.font.Font(tpyxeface, 24)
title = font.render("Start", True, (0, 0, 0))
tit_w = title.get_width()
tit_h = title.get_height()
####################設定雪花基本參數######################

####################新增fps######################

######################循環偵測######################

paint = False
while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 0, 0, tit_w, tit_h):
                paint = not paint

    if paint:
        title = font.render("Start", True, (0, 0, 0))
    else:
        title = font.render("Stop", True, (0, 0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(title, (0, 0))
    pygame.display.update()