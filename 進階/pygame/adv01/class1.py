######################匯入模組######################
import pygame
import sys
import math
######################初始化######################
WHITE = (205, 157, 201)
pygame.init()
width = 640
height = 320

######################建立視窗######################
screen = pygame.display.set_mode((width, height))  # 設定視窗大小
pygame.display.set_caption("My Game")  # 設定視窗標題

######################建立畫布######################
bg = pygame.Surface((width, height))
bg.fill(WHITE)
######################建立畫布######################
# pygame.draw.circle(bg, (0, 0, 225), (200, 100), 30, 0)
# pygame.draw.rect(bg, (0, 255, 0), [270, 130, 60, 40], 5)
# pygame.draw.ellipse(bg, (225, 0, 0), [130, 160, 60, 35], 5)
# pygame.draw.line(bg, (225, 0, 255), (280, 220), (320, 220), 3)
# pygame.draw.polygon(bg, (100, 200, 45), [[100, 100], [0, 200], [200, 200]], 0)
# pygame.draw.arc(bg, (225, 10, 0), [100, 100, 100, 50], math.radians(180),math.radians(0), 2)
######################word######################
tpyxeface = pygame.font.get_default_font()
font = pygame.font.Font(tpyxeface, 24)
title = font.render("Start", True, (0, 0, 0))
tit_w = title.get_width()
tit_h = title.get_height()


######################world korea######################
def check_click(pos, x_min, y_min, x_max, y_max):
    x_match = x_min < pos[0] < x_max
    y_match = pos[1] > y_min and pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


######################迴圈######################
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
        pygame.draw.circle(bg, (0, 0, 225), (200, 100), 30, 0)
        pygame.draw.rect(bg, (0, 255, 0), [270, 130, 60, 40], 5)
        pygame.draw.ellipse(bg, (225, 0, 0), [130, 160, 60, 35], 5)
        pygame.draw.line(bg, (225, 0, 255), (280, 220), (320, 220), 3)
        pygame.draw.polygon(bg, (100, 200, 45),
                            [[100, 100], [0, 200], [200, 200]], 0)
        pygame.draw.arc(bg, (225, 10, 0), [100, 100, 100, 50],
                        math.radians(180), math.radians(0), 2)
    else:
        bg.fill((0, 0, 0))

    print(pygame.mouse.get_pos())
    screen.blit(bg, (0, 0))
    screen.blit(title, (0, 0))
    pygame.display.update()
