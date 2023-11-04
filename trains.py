import pygame
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

info = pygame.display.Info() # You have to call this before pygame.display.set_mode()
screen_width,screen_height = info.current_w,info.current_h

window_width,window_height = screen_width,screen_height
window = pygame.display.set_mode((window_width,window_height))

WIDTH = window_width
HEIGHT = window_height

class Train (pygame.sprite.Sprite):

    def __init__(self, x, y, speed, image):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()

        self.rect = self.image.get_rect(center=(x,y))
        self.speed = speed

    #def update(self, *args):
        #if self.rect.x < args[0] - 20 and self.rect.x != args[0]/3:
            #self.rect.x -= self.speed
        #else:
            #self.rect.x = 0


    def update(self, *args):

        self.rect.x += self.speed + args[0]
        if self.rect.left > WIDTH*0.85:
            self.rect.right = WIDTH/12+50


    def __del__(self):

            class_name = self.__class__.__name__
            print('{} уничтожен'.format(class_name))