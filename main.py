import pygame
import random

if __name__ == "__main__":
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    lightred= pygame.Color(255,255,0)
    darkgreen = pygame.Color('#008000')
    yellow = pygame.Color('yellow')

    def draw_squre(screen):
        color= pygame.Color(50,150,50)
        pygame.draw.rect(screen, color, (20,20,100,100),0)#тень темный квадрат

        hsv =color.hsla# новая цветовая модель
        color.hsla=(hsv[0],hsv[1],hsv[2]+30,hsv[3])# светлый квадрат
        pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)


    def draw():
        screen.fill((0,0,0))#цвет фона
        font= pygame.font.Font(None, 50)#фон
        text = font.render('Hello, PyGame!', True,(100,255,100))#текст
        text_x = width//2 - text.get_width()//2#располоджение по центру
        text_y= height//2 - text.get_height()//2
        text_w=text.get_width()
        text_h= text.get_height()
        screen.blit(text,(text_x,text_y))#отрисовавает картину в нужных координатах\
        pygame.draw.rect(screen,(0,255,0),(text_x-10,text_y-10,text_w+20,text_h+20),5)#экран, цвет , ректанд , толщина


    def rect(screen):
        screen.fill((0,255,0))
        screen.fill(pygame.Color('Red'),pygame.Rect(10,10,60,60))

    def star_sky(screen):
        screen.fill(pygame.Color('Black'))
        for i in range(10000):
            screen.fill(pygame.Color('white'), (random.random()*width,random.random()*height,1,1))
    while pygame.event.wait().type != pygame.QUIT:
        # draw()
        # draw_squre(screen)
        rect(screen)
        star_sky(screen)
        pygame.display.flip()#смена кадроов

    pygame.quit()
