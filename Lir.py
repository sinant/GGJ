import pygame
import time

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
        self.image.fill(colors["red"])

        self.rect = self.image.get_rect()
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
        self.image.fill(colors["black"])

        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
        self.level = level
    def update(self):
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            print("Trigger Enter")



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
        button = Button(posX, posY, width, height, "UP")
        self.platform_list.add(button)


def GameLoop():

    level = Level()
    trigger = Triger(100, 50, 100, 100, level)
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("LEFT")
                elif event.key == pygame.K_RIGHT:
                    print("RIGHT")
                elif event.key == pygame.K_UP:
                    print("UP")
                elif event.key == pygame.K_DOWN:
                    print("DOWN")

        level.update()
        trigger.update()

        # trigger.draw(gameDisplay)
        level.draw(gameDisplay)
        pygame.display.update()
        clock.tick(fps)

GameLoop()


pygame.quit()