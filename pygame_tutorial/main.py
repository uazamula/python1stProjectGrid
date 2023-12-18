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


def player_animation():
    global player_surf, player_index
    if player_rect.bottom < HEDGEHOG_L_BOTTOM:
        player_surf = player_jump
    else:
        player_index += 0.08
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]


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

score_surf = test_font.render('My game', False, (64, 64, 64))
score_rect = score_surf.get_rect(center=(400, 50))

# Obstacles
snail_frame1 = pygame.image.load('graphics/hedgehog_l.png').convert_alpha()
snail_frame2 = pygame.image.load('graphics/hedgehog_r.png').convert_alpha()

snail_frame1 = pygame.transform.rotozoom(snail_frame1, 0, 0.25)
snail_frame2 = pygame.transform.rotozoom(snail_frame2, 0, 0.25)
snail_frames = [snail_frame1, snail_frame2]
snail_frame_index = 0

snail_surf = snail_frames[snail_frame_index]

HEDGEHOG_L_BOTTOM = screen_height - 10
HEDGEHOG_D_BOTTOM = HEDGEHOG_L_BOTTOM - 5

hedgehog_vert_1 = pygame.image.load('graphics/hedgehog_d.png').convert_alpha()
hedgehog_vert_2 = pygame.image.load('graphics/hedgehog.png').convert_alpha()

hedgehog_vert_1 = pygame.transform.rotozoom(hedgehog_vert_1, 0, 0.25)
hedgehog_vert_2 = pygame.transform.rotozoom(hedgehog_vert_2, 0, 0.25)

fly_frames = [hedgehog_vert_1, hedgehog_vert_2]
fly_frame_index = 0

hedgehog_d_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []

MAX_X = 600
snail_x_pos = MAX_X
player_walk1 = pygame.image.load('graphics/ballerina_a.png').convert_alpha()
player_walk2 = pygame.image.load('graphics/ballerina_d.png').convert_alpha()
player_walk = [player_walk1, player_walk2]
player_index = 0
player_surf = player_walk[player_index]

player_jump = pygame.image.load('graphics/ballerina_b.png').convert_alpha()

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

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 300)

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
                # snail_rect.x = ground_rect.bottomright[0]
                game_active = True
                start_time = pygame.time.get_ticks() // 1000

        if game_active:
            if event.type == obstacle_timer:
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
            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index=1
                else: snail_frame_index=0
                snail_surf = snail_frames[snail_frame_index]
            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index=1
                else: fly_frame_index=0
                hedgehog_d_surf = fly_frames[fly_frame_index]


    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, ground_rect)
        score = display_score()

        screen.blit(test_surface1, (50, 50))

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= ground_rect.bottom:
            player_rect.bottom = ground_rect.bottom

        player_animation()

        screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        game_active = collisions(player_rect, obstacle_rect_list)

        mouse_pos = pygame.mouse.get_pos()

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
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
