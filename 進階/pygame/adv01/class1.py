######################匯入模組######################
import pygame
import sys
import math
######################初始化######################
WHITE = (205, 157, 201)
pygame.init()  # 啟動 Pygame
width = 640  # 設定視窗寬度
height = 320  # 設定視窗高度

######################建立視窗######################
screen = pygame.display.set_mode((width, height))  # 設定視窗大小
pygame.display.set_caption("My Game")  # 設定視窗標題

######################建立畫布######################
bg = pygame.Surface((width, height))
bg.fill(WHITE)
######################建立畫布######################
#pygame.draw.circle(bg, (0, 0, 225), (200, 100), 30, 0)
#pygame.draw.rect(bg, (0, 255, 0), [270, 130, 60, 40], 5)
#pygame.draw.ellipse(bg, (225, 0, 0), [130, 160, 60, 35], 5)
#pygame.draw.line(bg, (225, 0, 255), (280, 220), (320, 220), 3)
#pygame.draw.polygon(bg, (100, 200, 45), [[100, 100], [0, 200], [200, 200]], 0)
#pygame.draw.arc(bg, (225, 10, 0), [100, 100, 100, 50], math.radians(180),math.radians(0), 2)
######################cycle ur mom######################
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    print(pygame.mouse.get_pos())
    screen.blit(bg, (0, 0))
    pygame.display.update()
    if event.type == pygame.QUIT:
        sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.draw.circle(bg, (0, 0, 225), (200, 100), 30, 0)
pygame.draw.rect(bg, (0, 255, 0), [270, 130, 60, 40], 5)
pygame.draw.ellipse(bg, (225, 0, 0), [130, 160, 60, 35], 5)
pygame.draw.line(bg, (225, 0, 255), (280, 220), (320, 220), 3)
pygame.draw.polygon(bg, (100, 200, 45), [[100, 100], [0, 200], [200, 200]], 0)
pygame.draw.arc(bg, (225, 10, 0), [100, 100, 100, 50], math.radians(180),
                math.radians(0), 2)
