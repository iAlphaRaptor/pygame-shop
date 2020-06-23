import pygame
from shelf import Shelf
pygame.init()

SCREENWIDTH = 800
SCREENHEIGHT = 800
size = (SCREENWIDTH, SCREENHEIGHT)

BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)
BLUE   = (0, 0, 255)
RED    = (255, 0, 0)
GREY   = (150, 150, 150)
YELLOW = (246, 255, 77)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

carryOn = True

font = pygame.font.Font("Fonts/numberFont.ttf", 20)

shelfContents = [[0, "Apple", 5, 25],
                 [0, "Banana", 8, 15],
                 [0, "Bread", 15, 10],
                 [0, "Water", 4, 100],
                 [0, "Orange", 8, 15],
                 [0, "Orange", 8, 15],
                 [0, "Orange", 8, 15],
                 [0, "Orange", 8, 15],
                 [0, "Orange", 8, 15],
                 [0, "Orange", 8, 15],
                 [0, "Orange", 8, 15],
                 [0, "Orange", 8, 15],
                 [0, "Orange", 8, 15],
                 [0, "Orange", 8, 15],
                 [0, "Orange", 8, 15],
                 [0, "Orange", 8, 15],]

shelves = pygame.sprite.Group()
for i in range(len(shelfContents)):
    shelves.add(Shelf(shelfContents[i][0], GREY, BLACK, shelfContents[i][1], shelfContents[i][2], shelfContents[i][3]))
    current = shelves.sprites()[-1]
    current.rect.x = 35 + ((i % 4) * 185)
    current.rect.y = 125 + ((i // 4) * 155)


while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=False

    ## Main background
    screen.fill(BLACK)

    text = font.render("1000", True, WHITE, None)
    pygame.draw.ellipse(screen, YELLOW, (703, 13, 25, 25))
    screen.blit(text, (735, 10, 0, 0))

    shelves.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
