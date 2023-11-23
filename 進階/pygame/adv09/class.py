######################匯入模組######################
import pygame
import sys
import os
from pygame.locals import *
import random


####################定義函式######################
def bg_update():
    """更新背景"""
    global bg_roll_x

    bg_roll_x = (bg_roll_x - 10) % bg_x  # 背景移動
    screen.blit(img, (bg_roll_x - bg_x, 0))  # 背景圖左移
    screen.blit(img, (bg_roll_x, 0))  # 背景圖接續顯示


def move_cacti():
    """移動仙人掌"""
    global cacti_x, score, cacti_center_x, cacti_center_y,enemy_random

    cacti_x = (cacti_x - cacti_shift) % (bg_x - 100)  # 仙人掌移動
    cacti_center_x = cacti_x + img_cacti.get_width() / 2  # 仙人掌中心x位置
    cacti_center_y = cacti_y + img_cacti.get_height() / 2  # 仙人掌中心y位置
    screen.blit(img_cacti, (cacti_x, cacti_y))

    if cacti_x <= 0:
        score += 1
        enemy_random = random.randint(0, 1)


def move_dinosaur():
    """移動恐龍"""
    global ds_y, jumpState, jumpValue, ds_index, ds_center_x, ds_center_y

    if jumpState:  # 可以起跳
        if ds_y >= LIMIT_LOW:
            jumpValue = -jump_height
        if ds_y <= 0:
            jumpValue = jump_height
        ds_y += jumpValue

        # 平滑跳躍（可選）
        if jumpValue < 0:
            jumpValue += 1  # 上升速度逐漸減小
        else:
            jumpValue += 1  # 下降速度逐漸增大

        if ds_y >= LIMIT_LOW:
            jumpState = False
            ds_y = LIMIT_LOW  # 確保恐龍回到地面

    # 計算恐龍圖片編號
    ds_index = (ds_index - 1) % len(img_dinosaur)
    # 計算恐龍中心點
    ds_center_x = ds_x + img_dinosaur[ds_index].get_width() / 2
    ds_center_y = ds_y + img_dinosaur[ds_index].get_height() / 2
    # 繪製恐龍
    screen.blit(img_dinosaur[ds_index], (ds_x, ds_y))


def score_update():
    """更新分數"""
    score_sur = score_font.render(str(score), True, RED)
    screen.blit(score_sur, [10, 10])


def is_hit(x1, y1, x2, y2, r):
    """圓形碰撞偵測"""
    # 原理:兩點距離公式，兩點距離小於半徑，則碰撞
    if ((x1 - x2) ** 2 + (y1 - y2) ** 2) < (r * r):
        return True
    else:
        return False


def game_over():
    """遊戲結束"""
    screen.blit(img_gg, ((bg_x - gg_w) / 2, (bg_y - gg_h) / 2))


def move_ptera():
    """移動翼龍"""
    global ptera_x, ptera_index, score, ptera_center_x, ptera_center_y, enemy_random

    ptera_x = (ptera_x - ptera_shift) % (bg_x - 100)  # 翼龍移動
    ptera_index = (ptera_index - 1) % len(img_ptera)
    ptera_center_x = ptera_x + img_ptera[ptera_index].get_width() / 2
    ptera_center_y = ptera_y + img_ptera[ptera_index].get_height() / 2
    screen.blit(img_ptera[ptera_index], (ptera_x, ptera_y))
    if ptera_x <= 0:
        score += 1
        enemy_random = random.randint(0, 1)


####################初始化######################
os.chdir(sys.path[0])
pygame.init()
LIMIT_LOW = 140  # 地面高度
PTERA_LIMIT_LOW = 110  # 翼龍高度
clock = pygame.time.Clock()
RED = (255, 0, 0)  # 紅色
enemy_random = 0

####################載入圖片物件######################
img = pygame.image.load("bg.png")  # 加載背景
img_dinosaur = [  # 加載恐龍
    pygame.image.load("小恐龍1.png"),
    pygame.image.load("小恐龍2.png"),
]
img_cacti = pygame.image.load("cacti.png")  # 加載仙人掌
img_gg = pygame.image.load("gameover.png")  # 加載遊戲結束畫面

# 加載翼龍
img_ptera = [pygame.image.load("翼龍飛飛1.png"), pygame.image.load("翼龍飛飛2.png")]
img_bend_down = [pygame.image.load("小恐龍蹲下1.png"), pygame.image.load("小恐龍蹲下2.png")]
bg_x = img.get_width()
bg_y = img.get_height()
bg_roll_x = 0  # 背景圖片滾動位置


######################建立視窗######################
screen = pygame.display.set_mode([bg_x, bg_y])  # 設定窗口
pygame.display.set_caption("Dinosaur")

######################分數物件######################
score = 0  # 分數計數
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 36)

######################恐龍物件######################
ds_x = 50  # 恐龍x位置
ds_y = LIMIT_LOW  # 恐龍y位置
ds_index = 0  # 恐龍圖片編號
jumpState = False  # 跳躍狀態
jumpValue = 0  # 跳躍值
jump_height = 13  # 跳躍高度
ds_center_x = ds_x + img_dinosaur[0].get_width() / 2  # 恐龍中心x位置
ds_center_y = ds_y + img_dinosaur[0].get_height() / 2  # 恐龍中心y位置
ds_detect_r = min(img_dinosaur[0].get_width(), img_dinosaur[0].get_height()) / 2  # 恐龍偵測半徑

######################仙人掌物件######################
cacti_x = bg_x - 100  # 障礙物x位置
cacti_y = LIMIT_LOW  # 障礙物y位置
cacti_shift = 10  # 仙人掌移動量
cacti_center_x = cacti_x + img_cacti.get_width() / 2  # 障礙物中心x位置
cacti_center_y = cacti_y + img_cacti.get_height() / 2  # 障礙物中心y位置
cacti_detect_r = max(img_cacti.get_width(), img_cacti.get_height()) / 2 - 15  # 障礙物偵測半徑

######################遊戲結束物件######################
gg = False  # 遊戲結束
gg_w = img_gg.get_width()  # 遊戲結束圖片寬度
gg_h = img_gg.get_height()  # 遊戲結束圖片高度


######################翼龍物件######################
ptera_x = bg_x - 100  # 障礙物x位置
ptera_y = PTERA_LIMIT_LOW  # 障礙物y位置
ptera_index = 0  # 翼龍圖片編號
ptera_shift = 10  # 翼龍移動量
ptera_center_x = ptera_x + img_ptera[0].get_width() / 2  # 翼龍中心x位置
ptera_center_y = ptera_y + img_ptera[0].get_height() / 2  # 翼龍中心y位置
ptera_detect_r = max(img_ptera[0].get_width(), img_ptera[0].get_height()) / 2 - 10  # 翼龍偵測半徑


######################循環偵測######################
while True:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and ds_y <= LIMIT_LOW:  # 判斷恐龍是否在地上
                jumpState = True  # 開啟跳躍狀態
            if event.key == K_RETURN and gg:
                score = 0
                gg = False
                cacti_x = bg_x - 100
                ptera_x = bg_x - 100
                ds_y = LIMIT_LOW
                jumpState = False

    

    if gg:
        game_over()
    else:
        bg_update()
        # move_cacti()
        move_dinosaur()
        score_update()

        if enemy_random ==0:
            move_cacti()
            gg = is_hit(ds_center_x, ds_center_y, cacti_center_x, cacti_center_y, cacti_detect_r + ds_detect_r)
            pygame.draw.circle(screen, RED, (int(cacti_center_x), int(cacti_center_y)), cacti_detect_r + ds_detect_r, 1)
        else:
            move_ptera()
            gg = is_hit(ds_center_x, ds_center_y, ptera_center_x, ptera_center_y, ptera_detect_r + ds_detect_r)
            pygame.draw.circle(screen, RED, (int(ptera_center_x), int(ptera_center_y)), ptera_detect_r + ds_detect_r, 1)
    pygame.display.update()