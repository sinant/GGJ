import pygame

pygame.init()
colors = {"white": (255, 255, 255),
          "black": (0, 0, 0),
          "red": (255, 0, 0),
          "blue": (0,0,255),
          "green": (0,255,0)
           }

#Select screen resolutions
screenHeight = 600
screenWith = 800
resolution = (screenWith, screenHeight)
#gameDisplay = pygame.display.set_mode(resolution,pygame.FULLSCREEN)
gameDisplay = pygame.display.set_mode(resolution)

fps = 30

## game title
pygame.display.set_caption("Indian Game Screen")

class Node(pygame.sprite.Sprite):

    def __init__(self,posX,posY,width,height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(colors["green"])

        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY

        self.clicked = False

        self.width = width
        self.height = height

    def update(self,mousePosX,mousePosY):
        self.changeColor(mousePosX,mousePosY)

    def changeColor(self,mousePosX, mousePosY):
        if self.checkIfClicked(mousePosX,mousePosY):
            self.image.fill(colors["red"])

    def checkIfClicked(self,mousePosX, mousePosY):
        x = self.rect.x
        y = self.rect.y
        width = self.width
        height = self.height

        if(mousePosX >= x and mousePosX <= x + width) and (mousePosY >= y and mousePosY <= y+height):
            self.clicked = True
            return True

        else:
            return False


class Level(object):
    def __init__(self):

        self.platform_list = pygame.sprite.Group()
        self.win = False
        # Background image
        self.background = pygame.image.load("in_background.png")
        self.hand = pygame.image.load("in_hand.png")
    def mouseClicked(self,mousePosX,mousePosY):
        self.platform_list.update(mousePosX,mousePosY)
        win = True

        for elem in self.platform_list:
            if elem.clicked is False:
                win = False
        print(win)
        if win is True:
            self.youWin()

    def youWin(self):
        self.win = True

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(colors["blue"])
        screen.blit(self.background, (0, 0) )
        self.platform_list.draw(screen)
        screen.blit(self.hand, (457,122))
        # Draw all the sprite lists that we have


    def createNode(self, posX, posY, width, height):
        node = Node(posX, posY, width, height)
        self.platform_list.add(node)

def gameLoop():

    level = Level()
    level.createNode(463,302,50,50)
    level.createNode(457,265,50,50)
    level.createNode(506,272,50,50)
    level.createNode(497,234,50,50)
    level.createNode(501,184,50,50)
    level.createNode(495,150,50,50)
    level.createNode(543,140,50,50)
    level.createNode(562,122,50,50)
    level.createNode(611,126,50,50)
    level.createNode(560,189,50,50)
    level.createNode(560,239,50,50)
    level.createNode(554,286,50,50)
    level.createNode(528,318,50,50)
    level.createNode(550,368,50,50)
    level.createNode(578,417,50,50)
    level.createNode(566,429,50,50)
    level.createNode(614,428,50,50)
    level.createNode(659,399,50,50)
    level.createNode(666,354,50,50)
    level.createNode(676,316,50,50)
    level.createNode(676,270,50,50)
    level.createNode(656,267,50,50)
    level.createNode(660,161,50,50)
    level.createNode(605,176,50,57)
    level.createNode(602,232,50,50)
    level.createNode(664,211,50,57)
    level.createNode(604,278,52,57)
    level.createNode(600,334,50,57)
    level.createNode(489,350,50,57)
    level.createNode(502,406,50,57)
    level.createNode(529,462,50,15)
    gameExit = False

    while not gameExit:
        gameDisplay.fill(colors["white"])

        if level.win is True:
            return True

        for event in pygame.event.get():

            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y positions of the mouse click
                x, y = event.pos
                print(x, y)
                level.mouseClicked(x,y)



        level.draw(gameDisplay)
        pygame.display.update()



