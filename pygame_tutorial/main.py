import random

import pygame
from sys import exit
from random import randint

height = 400-50


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'fly':
            fly_1 = pygame.image.load(
                'graphics/hedgehog_d.png').convert_alpha()
            fly_1 = pygame.transform.rotozoom(fly_1,0,0.25)
            fly_2 = pygame.image.load(
                'graphics/hedgehog.png').convert_alpha()
            fly_2 = pygame.transform.rotozoom(fly_2,0,0.25)

            self.frames = [fly_1, fly_2]
            y_pos = height - 10
        else:
            snail_1 = pygame.image.load(
                'graphics/hedgehog_l.png').convert_alpha()
            snail_1 = pygame.transform.rotozoom(snail_1,0,0.25)

            snail_2 = pygame.image.load(
                'graphics/hedgehog_r.png').convert_alpha()
            snail_2 = pygame.transform.rotozoom(snail_2,0,0.25)

            self.frames = [snail_1, snail_2]
            y_pos = height

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(
            midbottom=(random.randint(900, 1100), y_pos))

    def animation_state(self):

        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load(
            'graphics/ballerina_a.png').convert_alpha()
        player_walk2 = pygame.image.load(
            'graphics/ballerina_d.png').convert_alpha()
        self.player_walk = [player_walk1, player_walk2]
        self.player_index = 0
        self.player_jump = pygame.image.load(
            'graphics/ballerina_b.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(200, height))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= height:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= height:
            self.gravity = 0
            self.rect.bottom = height

    def animation_state(self):
        if self.rect.bottom < height:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    # TODO 3:22:40

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


def display_score():
    current_time = pygame.time.get_ticks() // 1000 - start_time
    score_surf = test_font.render('Score: ' + str(current_time), False,
                                  (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True


pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill('Gray')
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

test_font = pygame.font.Font('fonts/next_bravo.ttf', 30)

sky_surface = pygame.image.load('graphics/sky.jpg').convert()
ground_surface = pygame.image.load('graphics/grass.png').convert_alpha()
ground_surface = pygame.transform.scale(ground_surface, (screen_width, 193))
ground_rect = ground_surface.get_rect(
    midbottom=(screen_width // 2, screen_height))

score_surf = test_font.render('My game', False, (64, 64, 64))
score_rect = score_surf.get_rect(center=(400, 50))

MAX_X = 600
snail_x_pos = MAX_X

player_stand = pygame.image.load('graphics/ballerina_b.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Runner', False, (64, 64, 64))
game_name_rect = game_name.get_rect(center=(400, 25))

game_message = test_font.render('Press space to run', False, (64, 64, 64))
game_message_rect = game_message.get_rect(center=(400, 325))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('collision pl with mouse')

        if not game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks() // 1000

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(
                    Obstacle(random.choice(['fly', 'snail', 'snail'])))

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, ground_rect)
        score = display_score()

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        # Obstacle movement
        game_active = collision_sprite()

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        player_gravity = 0

        score_message = test_font.render(f'Your score: {score}', False,
                                         (63, 63, 63))
        score_message_rect = score_message.get_rect(center=(400, 330))
        screen.blit(game_name, game_name_rect)
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)  # the ceiling of framerate
