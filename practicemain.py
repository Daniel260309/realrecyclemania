import pygame
import time
import random
# import math

pygame.init()

# Width and Height
display_width = 896
display_height = 415
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Icon
logo = pygame.image.load('logo.png')
pygame.display.set_icon(logo)
pygame.display.set_caption('Recycle Mania')

# Intro Background Image
introbg = pygame.image.load('menubg.png.')

# Help Button
helpdisplay = pygame.image.load('help.png')

# Play Button
playbutton = pygame.image.load('playbt.png')

# Help Button
helpbutton = pygame.image.load('helpbt.png')

# Exit Button
exitbutton = pygame.image.load('exit.png')

# Game Background Image
bg = pygame.image.load('gameSet.png')

# Clock
clock = pygame.time.Clock()

# Color
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
orange = (255, 165, 0)
purple = (128, 0, 128)

# Player Dimensions
player_width = 50
player_height = 50
playerImg = pygame.image.load('tile000.png')

# 9 Animations for Each movement
walkLeft = [pygame.image.load('tile027.png'), pygame.image.load('tile028.png'), pygame.image.load('tile029.png'),
            pygame.image.load('tile030.png'), pygame.image.load('tile031.png'), pygame.image.load('tile032.png'),
            pygame.image.load('tile033.png'), pygame.image.load('tile034.png'), pygame.image.load('tile035.png')]
walkRight = [pygame.image.load('tile036.png'), pygame.image.load('tile037.png'), pygame.image.load('tile038.png'),
             pygame.image.load('tile039.png'), pygame.image.load('tile040.png'), pygame.image.load('tile041.png'),
             pygame.image.load('tile042.png'), pygame.image.load('tile043.png'), pygame.image.load('tile044.png')]
walkUp = [pygame.image.load('tile054.png'), pygame.image.load('tile055.png'), pygame.image.load('tile056.png'),
          pygame.image.load('tile057.png'), pygame.image.load('tile058.png'), pygame.image.load('tile059.png'),
          pygame.image.load('tile060.png'), pygame.image.load('tile061.png'), pygame.image.load('tile062.png')]
walkDown = [pygame.image.load('tile045.png'), pygame.image.load('tile046.png'), pygame.image.load('tile047.png'),
            pygame.image.load('tile048.png'), pygame.image.load('tile049.png'), pygame.image.load('tile050.png'),
            pygame.image.load('tile051.png'), pygame.image.load('tile052.png'), pygame.image.load('tile053.png')]

# Animation (True or False)
left = False
right = False
up = False
down = False
walkCount = 0

# Item Images
appleImg = pygame.image.load('apple.png')
bananaImg = pygame.image.load('banana.png')
bottleImg = pygame.image.load('bottle.png')
cardboardImg = pygame.image.load('cardboard.png')
eggImg = pygame.image.load('egg.png.')
paperImg = pygame.image.load('paper.png')
deadfishImg = pygame.image.load('deadfish.png')

# Bin Images
trashbin = pygame.image.load('trash.png')
recyclebin = pygame.image.load('recycle.png')
compostbin = pygame.image.load('compst.png')

# Bin List
bincount = 0
binlist = [trashbin, recyclebin, compostbin]

# Item List
items = [appleImg, bananaImg, bottleImg, cardboardImg, eggImg, paperImg, deadfishImg]

# Sorting out the Images into the appropriate Bin
compostitems = [appleImg, bananaImg, eggImg]
recycleitems = [bottleImg, cardboardImg, paperImg]
trashitem = deadfishImg

# Y Position of the Items in the Conveyor belt
possibilitiesY = [(display_height * 0.80), (display_height * 0.40), (display_height * 0.60)]

# Changing the X position of the random items
randomImage = random.choice(items)
randomImage_X = display_width - 32
randomImage_Y = random.choice(possibilitiesY)
item_Xchange = -4
item_Ychange = 0

# Moving the items along the Conveyor belt
randomImage_X += item_Xchange
randomImage_Y += item_Ychange

# To determine the score and the missed ones
correct = 0
incorrect = 0

# Score Text
score_value = 0
scorefont = pygame.font.Font('freesansbold.ttf', 20)

# Game Over Text Position
textX = 800
textY = 10

# Carrying Item
carryingitem = []

binx = [30, 25, 40]
biny = [160, 242, 325]

trashx = 30
trashy = 160
recyclex = 25
recycley = 242
compostx = 40
composty = 325


def player(x, y):
    global walkCount
    gameDisplay.blit(bg, (0, 0))
    gameDisplay.blit(trashbin, (30, 160))
    gameDisplay.blit(recyclebin, (25, 242))
    gameDisplay.blit(compostbin, (40, 325))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        gameDisplay.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        gameDisplay.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    elif up:
        gameDisplay.blit(walkUp[walkCount // 3], (x, y))
        walkCount += 1
    elif down:
        gameDisplay.blit(walkDown[walkCount // 3], (x, y))
        walkCount += 1
    else:
        gameDisplay.blit(playerImg, (x, y))


# Game Over Message
def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf', 50)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(5)
    game_intro()


def crash():
    message_display('Game Over: Your score was ' + str(score_value))


# Displaying Score on the top right
def score_function(x, y):
    score = scorefont.render("Score : " + str(score_value), True, (255, 255, 255))
    gameDisplay.blit(score, (x, y))


def itemsprite():
    gameDisplay.blit(randomImage, (randomImage_X, randomImage_Y))


def menu():
    menuscreen = True
    while menuscreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            gameDisplay.blit(helpdisplay, (0, 0))
            gameDisplay.blit(exitbutton, (145, 66))
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and ((150 <= x <= 175) and (64 <= y <= 93)):
                game_intro()
        pygame.display.update()


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            gameDisplay.blit(introbg, (0, 0))
            gameDisplay.blit(playbutton, (display_width / 2 - 125, display_height / 2))
            gameDisplay.blit(helpbutton, (display_width / 2 - 64, display_height / 2 + 100))
            x, y = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN and (
                    (display_width / 2 - 125 <= x <= 617) and (display_height / 2 <= y <= 237)):
                game_loop()
            if event.type == pygame.MOUSEBUTTONDOWN and (
                    (display_width / 2 - 64 <= x <= 548) and (display_height / 2 + 100 <= y <= 463)):
                menu()

        pygame.display.update()


def game_loop():
    x = (display_width * 0.30)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0

    global randomImage

    gameexit = False
    while not gameexit:
        pygame.time.delay(20)
        global left
        global right
        global up
        global down
        global walkCount
        global randomImage_X
        global randomImage_Y
        global item_Xchange
        global score_value
        global item_Ychange
        global incorrect
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -5
                    left = True
                    right = False
                    up = False
                    down = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = 5
                    right = True
                    left = False
                    down = False
                    up = False
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    y_change = -5
                    up = True
                    down = False
                    left = False
                    right = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y_change = 5
                    down = True
                    up = False
                    left = False
                    right = False
                if event.key == pygame.K_ESCAPE:
                    game_intro()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                    right = False
                    left = False
                    up = False
                    down = False
                    walkCount = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    y_change = 0
                    right = False
                    left = False
                    up = False
                    down = False
                    walkCount = 0

        x += x_change
        y += y_change

        gameDisplay.fill(white)

        player(x, y)
        itemsprite()

        score_function(textX, textY)

        randomImage_X += item_Xchange

        if x >= display_width * 0.40 or x < 0:
            x_change = 0

        elif y >= display_height - player_height or y < display_height * 0.30:
            y_change = 0

        if randomImage_X <= display_width * 0.45:
            item_Xchange = 0
            if x_change == item_Xchange:
                item_Xchange = x_change
                item_Ychange = y_change
                randomImage_X += -2
                randomImage_Y += item_Ychange
                if 45 <= randomImage_X <= 94 and 158 <= randomImage_Y <= 255:
                    for randomImage in trashitem:
                        score_value += 1
                    else:
                        incorrect += 1
                        if incorrect == 1:
                            crash()
                if 47 <= randomImage_X <= 97 and 65 <= randomImage_Y <= 75:
                    for randomImage in recycleitems:
                        score_value += 1
                    else:
                        incorrect += 1
                        if incorrect == 1:
                            crash()
                if 42 <= randomImage_X <= 96 and 327 <= randomImage_Y <= 393:
                    for randomImage in compostitems:
                        score_value += 1
                        print(score_value)
                    else:
                        incorrect += 1
                        if incorrect == 1:
                            crash()


        pygame.display.update()
        clock.tick(70)


pygame.display.update()
game_intro()
game_loop()
pygame.quit()
quit()
