######################匯入模組######################
import pygame
import sys
import math
import os
import random


####################定義函式######################
def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = x_min < pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


def snow_fall():
    """下雪"""
    for snow in snow_list:
        # 畫出雪花
        pygame.draw.circle(screen, WHITE, (snow["x_site"], snow["y_site"]),
                           snow["radius"])

        # 計算雪花下次顯示的座標
        snow["x_site"] += snow["x_shift"]
        snow["y_site"] += snow["radius"]

        # 如果雪花落出畫面，重設位置
        if snow["y_site"] > bg_y or snow["x_site"] > bg_x:
            y_site = random.randint(-bg_y, -1)
            x_site = random.randint(0, bg_x)


####################初始化######################
os.chdir(sys.path[0])
pygame.init()
bg_img = "snow.jpg"
bg = pygame.image.load(bg_img)

bg_x = bg.get_width()
bg_y = bg.get_height()
WHITE = (255, 255, 255)

######################建立視窗######################
screen = pygame.display.set_mode((bg_x, bg_y))
pygame.display.set_caption("Snow")

####################撥放音樂######################
mp3_path = "snow-dream.mp3"
pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play()
pygame.mixer.music.fadeout(600000000)
pygame.mixer.music.pause()

####################設定文字######################
tpyxeface = pygame.font.get_default_font()
font = pygame.font.Font(tpyxeface, 24)
title = font.render("Start", True, (0, 0, 0))
tit_w = title.get_width()
tit_h = title.get_height()
####################設定雪花基本參數######################
snow_list = []
for i in range(150):
    x_site = random.randrange(0, bg_x)
    y_site = random.randrange(-bg_y, -1)
    x_shift = random.randint(-1, 1)
    radius = random.randint(4, 6)
    snow_list.append({
        "x_site": x_site,
        "y_site": y_site,
        "x_shift": x_shift,
        "radius": radius
    })
####################新增fps######################
clock = pygame.time.Clock()

######################循環偵測######################

paint = False
cnt = 0

while True:
    clock.tick(20)  # 設定每秒20幀執行
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_click(mouse_pos, 0, 0, tit_w, tit_h):
                paint = not paint
    if cnt > 10:
        cnt = 0
        for snow in snow_list:
            snow["x_shift"] = random.randint(-3, 3)

    else:
        cnt += 1
    screen.blit(bg, (0, 0))
    screen.blit(title, (0, 0))
    if paint:
        title = font.render("Start", True, (0, 0, 0))
        pygame.mixer.music.unpause()
        snow_fall()
    else:
        title = font.render("Stop", True, (0, 0, 0))
        pygame.mixer.music.pause()

    pygame.display.update()
