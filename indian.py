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

        # Background image
        self.background = None

    def mouseClicked(self,mousePosX,mousePosY):
        self.platform_list.update(mousePosX,mousePosY)
        win = True

        for elem in self.platform_list:
            if elem.clicked is False:
                win = False
        print(win)
        if win is True:
            self.win()

    def win(self):
        print ("WON")

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(colors["blue"])

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)

    def createNode(self, posX, posY, width, height):
        node = Node(posX, posY, width, height)
        self.platform_list.add(node)

def gameLoop():

    level = Level()
    level.createNode(50,50,50,50)
    level.createNode(150,50,50,50)
    level.createNode(250,50,50,50)
    level.createNode(350,50,50,50)
    level.createNode(450,50,50,50)

    gameExit = False

    while not gameExit:
        gameDisplay.fill(colors["white"])


        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y positions of the mouse click
                x, y = event.pos
                level.mouseClicked(x,y)



        level.draw(gameDisplay)
        pygame.display.update()


gameLoop()

pygame.quit()
quit()