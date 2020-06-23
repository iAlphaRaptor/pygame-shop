import pygame, random
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
PINK   = (199, 0, 162)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

carryOn = True
gameState = "play"
currentUnlock = 4
money = 1000000

font = pygame.font.Font("Fonts/numberFont.ttf", 25)
buttonFont = pygame.font.Font("Fonts/numberFont.ttf", 35)

shop = pygame.sprite.Sprite()
shop.image = pygame.Surface([61, 60])
shop.rect = shop.image.get_rect()
shop.rect.x = 705
shop.rect.y = 32.5

shop.image.fill(WHITE)
shopImage = pygame.image.load("Images/shop.png")
smallShopImage = pygame.transform.scale(shopImage, (60, 60))
shop.image.blit(smallShopImage, (0, 0))


buyButton = pygame.sprite.Sprite()
buyButton.image = pygame.Surface([500, 150])
buyButton.rect = buyButton.image.get_rect()
buyButton.rect.x = 150
buyButton.rect.y = 350

buyButton.image.fill(PINK)
pygame.draw.rect(buyButton.image, BLACK, (10, 10, 480, 130))
buttonText = buttonFont.render("BUY NEXT ITEM?", True, WHITE, None)
buyButton.image.blit(buttonText, (250 - (buttonFont.size("BUY NEXT ITEM?")[0] / 2), 15))
pygame.draw.ellipse(buyButton.image, YELLOW, (175, 75, 50, 50))
costText = buttonFont.render(str((currentUnlock + 2) * 20), True, YELLOW, None)
buyButton.image.blit(costText, (235, 75))

shelfContents = [[0, "Apple", 20, 25, False],
                 [1, "Banana", 2, 15, False],
                 [2, "Bread", 3, 10, False],
                 [3, "Water", 10, 100, False],
                 [4, "Orange", 10, 15, False],
                 [5, "Orange", 8, 15, True],
                 [6, "Orange", 8, 15, True],
                 [7, "Orange", 8, 15, True],
                 [8, "Orange", 8, 15, True],
                 [9, "Orange", 8, 15, True],
                 [10, "Orange", 8, 15, True],
                 [11, "Orange", 8, 15, True],
                 [12, "Orange", 8, 15, True],
                 [13, "Orange", 8, 15, True],
                 [14, "Orange", 8, 15, True],
                 [15, "Orange", 8, 15, True]]

shelves = pygame.sprite.Group()
for i in range(len(shelfContents)):
    shelves.add(Shelf(shelfContents[i][0], GREY, BLACK, shelfContents[i][1], shelfContents[i][2], shelfContents[i][3], shelfContents[i][4]))
    current = shelves.sprites()[-1]
    current.rect.x = 35 + ((i % 4) * 185)
    current.rect.y = 125 + ((i // 4) * 155)


while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            if gameState == "play":
                for shelf in shelves:
                    if shelf.isClicked(mousex, mousey):
                        if shelf.quantity > 0 and not shelf.locked:
                            money = shelf.buy(money)
                if shop.rect.collidepoint(mousex, mousey):
                    gameState = "shop"
            elif gameState == "shop":
                if buyButton.rect.collidepoint(mousex, mousey):
                    if money >= (currentUnlock + 2) * 20 and currentUnlock <= 14:
                        money -= (currentUnlock + 2) * 20
                        shelves.sprites()[currentUnlock+1].locked = False
                        currentUnlock += 1

                        buyButton.image.fill(PINK)
                        pygame.draw.rect(buyButton.image, BLACK, (10, 10, 480, 130))
                        buttonText = buttonFont.render("BUY NEXT ITEM?", True, WHITE, None)
                        buyButton.image.blit(buttonText, (250 - (buttonFont.size("BUY NEXT ITEM?")[0] / 2), 15))
                        pygame.draw.ellipse(buyButton.image, YELLOW, (175, 75, 50, 50))
                        costText = buttonFont.render(str((currentUnlock + 2) * 20), True, YELLOW, None)
                        buyButton.image.blit(costText, (235, 75))
                else:
                    gameState = "play"


    shelves.update()
    for s in shelves:
        s.updateDisplay()

    shop.update()
    buyButton.update()

    ## Main background
    screen.fill(BLACK)

    text = font.render(str(money), True, WHITE, None)
    pygame.draw.ellipse(screen, YELLOW, (35, 45, 35, 35))
    screen.blit(text, (78, 42, 0, 0))

    shelves.draw(screen)
    screen.blit(shop.image, shop.rect)

    if gameState == "shop":
        screen.blit(buyButton.image, buyButton.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
