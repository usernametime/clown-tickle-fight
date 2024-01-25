import pygame
import os

def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join(os.getcwd(), name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()

class Clown(pygame.sprite.Sprite):
    def __init__(self, side, image):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png(image)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.side = side
        self.speed = 10
        self.moveUp = False
        self.moveDown = False
        self.moveLeft = False
        self.moveRight = False
        if self.side == "left":
            self.rect.midleft = self.area.midleft
        elif self.side == "right":
            self.rect.midright = self.area.midright

    def update(self):  
        if self.moveUp:
            self.rect.move_ip(0, -self.speed)
        elif self.moveDown:
            self.rect.move_ip(0, +self.speed)
        elif self.moveLeft:
            self.rect.move_ip(-self.speed, 0)
        elif self.moveRight:
            self.rect.move_ip(+self.speed, 0)
   
    def moveup(self, move):
        if move:
            self.moveUp = True
            self.moveDown = False
        else:
            self.moveUp = False

    def movedown(self, move):
        if move:
            self.moveUp = False
            self.moveDown = True
        else:
            self.moveDown = False

    def moveleft(self, move):
        if move:
            self.moveLeft = True
            self.moveRight = False
        else:
            self.moveLeft = False

    def moveright(self, move):
        if move:
            self.moveLeft = False
            self.moveRight = True
        else:
            self.moveRight = False