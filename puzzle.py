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
pygame.display.set_caption("Chin-Puzzle Game Screen")

class Plot(pygame.sprite.Sprite):

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

class Piece(pygame.sprite.Sprite):

    def __init__(self,posX,posY,width,height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(colors["red"])

        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY

        self.clicked = False

        self.width = width
        self.height = height

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

        self.plot_list = pygame.sprite.Group()
        self.piece_list = pygame.sprite.Group()
        self.win = False
        # Background image
        #self.background = pygame.image.load("in_background.png")
        self.hand = pygame.image.load("in_hand.png")

    def draw(self, screen):
        # Draw the background
        screen.fill(colors["blue"])
        screen.blit(self.background, (0, 0))
        self.platform_list.draw(screen)

    def createPlot(self, posX, posY, width, height):
        plot = Plot(posX, posY, width, height)
        self.plot_list.add(plot)

    def createPiece(self, posX, posY, width, height):
        piece = Piece(posX, posY, width, height)
        self.plot_list.add(piece)

class Selected:
    def __init__(self):

        self.plot = None
        self.piece = None

    def selectPiece(self,piece):
        self.plot = None
        self.piece = piece

    def selectPlot(self,plot):
        if (self.piece != None):
            self.plot = plot
            self.movePieceToPlot(self.piece, self.plot)

    def movePieceToPlot(self,piece , plot):
        x = plot.rect.centerx
        y = plot.rect.centery

        piece.rect.centerx = x
        piece.rect.centery = y