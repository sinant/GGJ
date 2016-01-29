import pygame


pygame.init()
colors = {"white": (255, 255, 255),
           "black": (0, 0, 0),
           "red": (255, 0, 0)
           }

## resoltion
screenHeight = 600
screenWith = 800
resolution = (screenWith, screenHeight)
gameDisplay = pygame.display.set_mode(resolution)

fps = 60

## game title
pygame.display.set_caption('First Run')


size_x = 100
size_y = 100
moveSpeed = 10

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 100)

def messageToScreen (msg, color, pos_x, pos_y):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [pos_x, pos_y])

def GameLoop():

    gameExit = False
    x = screenWith/2 - size_x/2
    y = screenHeight/2 - size_y/2
    x_Change = 0
    y_Change = 0

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_Change = -moveSpeed
                    y_Change = 0
                elif event.key == pygame.K_RIGHT:
                    x_Change = moveSpeed
                    y_Change = 0
                elif event.key == pygame.K_UP:
                    y_Change = -moveSpeed
                    x_Change = 0
                elif event.key == pygame.K_DOWN:
                    y_Change = moveSpeed
                    x_Change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_Change = 0
                if event.key == pygame.K_RIGHT:
                    x_Change = 0
                if event.key == pygame.K_UP:
                    y_Change = 0
                if event.key == pygame.K_DOWN:
                    y_Change = 0

        x += x_Change
        y += y_Change

        # boundaries
        if x + size_x >= screenWith or x <= 0:
            x -= x_Change
        if y + size_y >= screenHeight or y <= 0:
            y -= y_Change

        gameDisplay.fill(colors["white"])
        pygame.draw.rect(gameDisplay, colors["black"], [x, y, size_x, size_y])

        pygame.display.update()
        clock.tick(fps)


GameLoop()

pygame.quit()
quit()

