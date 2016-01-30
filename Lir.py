import pygame, os
import time
import random
from pygame.locals import *

pygame.init()
colors = {"white": (255, 255, 255),
           "black": (0, 0, 0),
           "red": (255, 0, 0),
          "blue": (0, 0, 255)
           }

#Select screen resolutions
screenHeight = 600
screenWith = 800
resolution = (screenWith, screenHeight)

#gameDisplay = pygame.display.set_mode(resolution,pygame.FULLSCREEN)
gameDisplay = pygame.display.set_mode(resolution)

fps = 30

## game title
pygame.display.set_caption("Select Screen")

clock = pygame.time.Clock()

class Button(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, posX, posY, width, height, button):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()
        self.button = button
        self.image = pygame.Surface([width, height])
        #self.image.fill(colors["red"])
        #self.up = pygame.image.load("gr_up.png")
        #self.image = self.up
        self.rect = self.image.get_rect()
        if self.button == "UP":
            self.image = pygame.image.load("gr_up.png")
        elif self.button == "DOWN":
            self.image = pygame.image.load("gr_down.png")
        elif self.button == "LEFT":
            self.image = pygame.image.load("gr_left.png")
        elif self.button == "RIGHT":
            self.image = pygame.image.load("gr_right.png")


        self.rect.x = posX
        self.rect.y = posY

    def update(self):
        self.move(5)

    def move(self,speed):
        self.rect.x -= speed

class Triger(pygame.sprite.Sprite):
    def __init__(self,posX,posY,width,height,level):
        super().__init__()
        self.image = pygame.Surface([width, height])
        #self.image.fill(colors["black"])

        self.tryChance = 3

        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
        self.level = level
    def update(self):
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)

        if( len (block_hit_list) != 0):
            for block in block_hit_list:
                self.lastButton = block.button
                #self.checkButton(block.button)

        else:
            self.lastButton = "NONE"

    def checkButton(self, pressedbutton):
        print(pressedbutton)
        if (self.lastButton == "NONE"):
            return
        elif pressedbutton == self.lastButton:
            if self.tryChance < 3 :
                self.tryChance += 1
                print(self.tryChance)
        elif pressedbutton != self.lastButton:
            self.tryChance -= 1
            print(self.tryChance)
            if self.tryChance <= 0:
                level.lose()



class Level(object):

    def __init__(self):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()

        # Background image
        self.background = None
        self.createButton(900, 50, 40, 40)
        self.timeS = time.time()
    def update(self):
        """ Update everything in this level."""
        if time.time() - self.timeS >= 2:

            self.createButton(900, 50, 40, 40)
            self.timeS = time.time()

        self.platform_list.update()


    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(colors["blue"])

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)

    def createButton(self, posX, posY, width, height):
        type = random.choice(("UP", "DOWN", "LEFT", "RIGHT"))
        button = Button(posX, posY, width, height, type)
        self.platform_list.add(button)

    def lose(self):
        print("YOU LOSE!!!!!!!")

level = Level()
def GameLoop():


    trigger = Triger(100, 50, 100, 100, level)
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                gameExit = True


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    pressedbutton = "LEFT"
                    trigger.checkButton(pressedbutton)
                elif event.key == pygame.K_RIGHT:
                    pressedbutton = "RIGHT"
                    trigger.checkButton(pressedbutton)
                elif event.key == pygame.K_UP:
                    pressedbutton = "UP"
                    trigger.checkButton(pressedbutton)
                elif event.key == pygame.K_DOWN:
                    pressedbutton = "DOWN"
                    trigger.checkButton(pressedbutton)

        level.update()
        trigger.update()

        # trigger.draw(gameDisplay)
        level.draw(gameDisplay)
        pygame.display.update()
        clock.tick(fps)

GameLoop()


pygame.quit()