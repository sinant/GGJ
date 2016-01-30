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
#gameDisplay = pygame.display.set_mode(resolution ,pygame.FULLSCREEN)
gameDisplay = pygame.display.set_mode(resolution)

fps = 30
pi = 22/7.0

#left triangle part
leftTriangle = ((0, 2), (0, 598), (380, 309))
#right triangle part
rightTriangle = ((800, 2), (800, 598), (400, 312))
#top triangle part
topTriangle = ((2, 0), (798, 0), (390, 309))
#bottom triangle part
bottomTriangle = ((2, 600), (798, 600), (390, 312))

## game title
pygame.display.set_caption("Table Select Screen")

def drawCircle(screen,color,position,radius,width):
    pygame.draw.circle(screen, color, position, radius, width)

def drawPolygon(screen,color,pointList,width):
    #pygame.draw.polygon(gameDisplay, (255, 0, 0), ((10, 10), (30, 400), (50, 100)), 1)
    pygame.draw.polygon(screen, color, pointList, width)

#Checks if mouse inside polygon
def isInside(x,y,poly):

    n = len(poly)
    inside = False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside

def returnCharacter(characterName):
    return characterName

def gameLoop():

    gameExit = False

    while not gameExit:
        gameDisplay.fill(colors["white"])

        #Draws left triangle
        drawPolygon(gameDisplay, colors["red"], leftTriangle, 1)

        #Draws right triangle
        drawPolygon(gameDisplay, colors["blue"], rightTriangle, 1)

        #Draws top triangle
        drawPolygon(gameDisplay, colors["black"], topTriangle, 1)

        #draws bottom triangle
        drawPolygon(gameDisplay, colors["green"], bottomTriangle, 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y positions of the mouse click
                x, y = event.pos

                print ("X= %s || Y= %s" % (x,y))

                if isInside(x,y,topTriangle):
                    return 1
                if isInside(x,y,bottomTriangle):
                    return 2
                if isInside(x,y,leftTriangle):
                    return 3
                if isInside(x,y,rightTriangle):
                    return 4
        pygame.display.update()
    pygame.quit()
    quit()

gameLoop()