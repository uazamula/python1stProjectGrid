import pygame
from sys import exit
from random import randint


def display_score():
    current_time = pygame.time.get_ticks() // 1000 - start_time
    score_surf = test_font.render('Score: ' + str(current_time), False,
                                  (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == HEDGEHOG_L_BOTTOM:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(hedgehog_d_surf, obstacle_rect)

            obstacle_list = [obstacle for obstacle in obstacle_list if
                             obstacle.x > 0]
        return obstacle_list
    else:
        return []


def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
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

test_font = pygame.font.Font('fonts/next_bravo.ttf', 30)
test_surface1 = pygame.Surface((50, 40))
test_surface1.fill('Red')
sky_surface = pygame.image.load('graphics/sky.jpg').convert()
ground_surface = pygame.image.load('graphics/grass.png').convert_alpha()
ground_surface = pygame.transform.scale(ground_surface, (screen_width, 193))
ground_rect = ground_surface.get_rect(
    midbottom=(screen_width // 2, screen_height))
# test_surface = pygame.image.load()

score_surf = test_font.render('My game', False, (64, 64, 64))
score_rect = score_surf.get_rect(center=(400, 50))

# Obstacles
snail_surf = pygame.image.load('graphics/hedgehog_l.png').convert_alpha()

hh_width = snail_surf.get_rect().width // 4
hh_height = snail_surf.get_rect().height // 4
snail_surf = pygame.transform.scale(snail_surf, (
    hh_width, hh_height))

obstacle_surf = snail_surf
HEDGEHOG_L_BOTTOM = screen_height - 10
HEDGEHOG_D_BOTTOM = HEDGEHOG_L_BOTTOM - 5
ground_x, ground_y = ground_surface.get_rect().bottomright
snail_rect = snail_surf.get_rect(
    bottomright=(screen_width - 10, HEDGEHOG_L_BOTTOM))

hedgehog_d_surf = pygame.image.load('graphics/hedgehog_d.png').convert_alpha()
hedgehog_d_surf = pygame.transform.rotozoom(hedgehog_d_surf, 0, 0.25)
hedgehog_d_rect = hedgehog_d_surf.get_rect(
    bottomright=(screen_width - 10, HEDGEHOG_D_BOTTOM))
obstacle_rect_list = []

MAX_X = 600
snail_x_pos = MAX_X
player_surf = pygame.image.load('graphics/ballerina_a.png').convert_alpha()

player_rect = player_surf.get_rect(midbottom=(screen_width // 2, screen_height))

player_gravity = -0

player_stand = pygame.image.load('graphics/ballerina_b.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = test_font.render('Runner', False, (64, 64, 64))
game_name_rect = game_name.get_rect(center=(400, 25))

game_message = test_font.render('Press space to run', False, (64, 64, 64))
game_message_rect = game_message.get_rect(center=(400, 325))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print('collision pl with mouse')

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (player_rect.collidepoint(
                        event.pos)) and (
                        player_rect.bottom >= ground_rect.bottom):
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and (
                        player_rect.bottom >= ground_rect.bottom):
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_rect.x = ground_rect.bottomright[0]
                game_active = True
                start_time = pygame.time.get_ticks() // 1000

        # if event.type == pygame.KEYUP:
        #     print('keyup')
        #     if event.key == pygame.K_SPACE:
        #         player_gravity=0
        if event.type == obstacle_timer and game_active:
            if randint(0, 2):
                obstacle_rect_list.append(snail_surf.get_rect(
                    bottomright=(
                        randint(screen_width + 100, screen_width + 300),
                        HEDGEHOG_L_BOTTOM)))
            else:
                obstacle_rect_list.append(hedgehog_d_surf.get_rect(
                    bottomright=(
                        randint(screen_width + 100, screen_width + 300),
                        HEDGEHOG_D_BOTTOM)))

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, ground_rect)
        score = display_score()
        # pygame.draw.rect(screen, '#d0c8fc', score_rect, 10, 5)
        # pygame.draw.line(screen, 'Green', (0, 0), pygame.mouse.get_pos(), 5)
        # pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50, 200, 100, 150))
        # pygame.draw.rect(screen,'Pink', score_rect,36)

        screen.blit(test_surface1, (50, 50))

        # screen.blit(score_surf, score_rect)

        # snail_x_pos -= 2
        # if snail_x_pos <= -hh_width + 10:
        #     snail_x_pos = MAX_X

        # screen.blit(snail_surface, (snail_x_pos, 300))

        # snail_rect.x -= 6
        # if snail_rect.x <= -hh_width + 10:
        #     snail_rect.x = screen_width

        screen.blit(snail_surf, snail_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= ground_rect.bottom:
            player_rect.bottom = ground_rect.bottom

        screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        game_active = collisions(player_rect,obstacle_rect_list)

        # keys = pygame.key.get_pressed()
        # print(keys[pygame.K_SPACE])

        if player_rect.colliderect(snail_rect):
            game_active = False
            print('collision player with hedgehog')
        mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     print('collision pl vs mouse')
        #     print(pygame.mouse.get_pressed())
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom=(80,300)
        player_gravity=0

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
