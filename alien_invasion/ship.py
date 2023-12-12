import pygame
#from alien_invasion import AlienInvasion

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship2.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right:
            self.rect.x+=1
        if self.moving_left:
            self.rect.x-=1

    def blitme(self):
        self.screen.blit(self.image, self.rect)