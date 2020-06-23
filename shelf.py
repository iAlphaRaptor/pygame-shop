import pygame
pygame.init()

font = pygame.font.Font("Fonts/numberFont.ttf", 25)

WHITE = (255, 255, 255)
YELLOW = YELLOW = (246, 255, 77)

class Shelf(pygame.sprite.Sprite):
    def __init__(self, index, backgroundColour, highlightColour, name, price, quantity, locked):
        super().__init__()


        self.index = index
        self.backgroundColour = backgroundColour
        self.highlightColour = highlightColour
        self.name = name
        self.price = price
        self.quantity = quantity
        self.locked = locked

        self.nameText = font.render(self.name, True, WHITE, None)
        self.priceText = font.render(str(self.price), True, YELLOW, None)
        self.quantityText = font.render("x"+str(self.quantity), True, WHITE, None)
        self.lockedText = font.render("LOCKED", True, WHITE, None)

        self.image = pygame.Surface([175, 140])
        self.rect = self.image.get_rect()

        self.image.fill(self.backgroundColour)
        if self.locked:
            self.image.blit(self.lockedText, (87.5 - (font.size("LOCKED")[0]), 70 - (font.size("LOCKED")[1])))
        else:
            pygame.draw.rect(self.image, self.highlightColour, (10, 10, 155, 50))
            pygame.draw.ellipse(self.image, YELLOW, (10, 110, 25, 25))
            self.image.blit(self.nameText, (87.5 - (font.size(self.name)[0] / 2), 35 - (font.size(self.name)[1] / 2)))
            self.image.blit(self.quantityText, (87.5 - (font.size("x"+str(self.quantity))[0] / 2), 60))
            self.image.blit(self.priceText, (37, 102))

    def updateDisplay(self):
        self.nameText = font.render(self.name, True, WHITE, None)
        self.priceText = font.render(str(self.price), True, YELLOW, None)
        self.quantityText = font.render("x"+str(self.quantity), True, WHITE, None)

        self.image.fill(self.backgroundColour)
        if self.locked:
            self.image.blit(self.lockedText, (87.5 - (font.size("LOCKED")[0] / 2), 70 - (font.size("LOCKED")[1] / 2)))
        else:
            pygame.draw.rect(self.image, self.highlightColour, (10, 10, 155, 50))
            pygame.draw.ellipse(self.image, YELLOW, (10, 110, 25, 25))
            self.image.blit(self.nameText, (87.5 - (font.size(self.name)[0] / 2), 35 - (font.size(self.name)[1] / 2)))
            self.image.blit(self.quantityText, (87.5 - (font.size("x"+str(self.quantity))[0] / 2), 60))
            self.image.blit(self.priceText, (37, 102))

    def buy(self, money):
        self.quantity -= 1
        return money + self.price

    def isClicked(self, mousex, mousey):
        return self.rect.collidepoint(mousex, mousey)
