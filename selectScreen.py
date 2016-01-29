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
pygame.display.set_caption("Select Screen")


def drawRectangle(screen,color,positionAndSize):
    pygame.draw.rect(screen,color,positionAndSize)

def gameLoop():

    gameExit = False

    while not gameExit:
        gameDisplay.fill(colors["white"])

        #top-left
        drawRectangle(gameDisplay,colors["red"],(0,0,400,300))

        #top-right
        drawRectangle(gameDisplay,colors["blue"],(400,0,400,300))

        #bottom-left
        drawRectangle(gameDisplay,colors["black"],(0,300,400,300))

        #bottom-right
        drawRectangle(gameDisplay,colors["green"],(400,300,400,300))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y positions of the mouse click
                x, y = event.pos

                print ("X= %s || Y= %s", x, y)

                #Top-Left Rectangle Click
                if x < 400 and y < 300:
                    print("Top-Left Rectangle")

                #Top-Right Rectangle Click
                if x > 400 and y < 300:
                    print("Top-Right Rectangle")

                #Bottom-Left Rectangle Click
                if x < 400 and y > 300:
                    print("Bottom-Left Rectangle")

                #Bottom-Right Rectangle Click
                if x > 400 and y > 300:
                    print("Bottom-Right Rectangle")


        pygame.display.update()


gameLoop()

pygame.quit()
quit()