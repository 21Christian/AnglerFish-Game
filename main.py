
import pygame.sprite
from angler_fish import *
from fish import *
from toxic_fish import *
from shark import *
import time


# Initialization of the game

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('AnglerFish')
background = pygame.transform.scale(pygame.image.load('assets/underwater.png'), (screen_width, screen_height))
menu_screen = background
RED = (250, 0, 0)
GREEN = (0, 255, 0)
clock = pygame.time.Clock()
screen_font = pygame.font.SysFont("AnisaSans.ttf", 25)
game_over_font = pygame.font.SysFont("AnisaSans.ttf", 50)

fish_spawning = 120
toxic_fish_spawning = 220
shark_spawning = 500
score_count = 0
level_count = 1000
fish_count = 0
toxic_fish_count = 0
shark_count = 0
chances = 5
level = 1

# groups
player = BigFish(rectangle, rectangle2)
big_fish = pygame.sprite.Group(player)
small_fishes = pygame.sprite.Group()
toxic_fishes = pygame.sprite.Group()
sharks = pygame.sprite.Group()
moving = False


# functions
def spawning_logic():
    global fish, fish_count, toxic_fish_count, shark, shark_count, chances

    if fish_count == fish_spawning:
        fish = Fish(fish_pic, healthy_fish_y)
        small_fishes.add(fish)
        fish.attack = True
        fish_count = 0
        if fish.rect.x >= 800:
            chances -= 1

    if toxic_fish_count == toxic_fish_spawning:
        fish = ToxicFish(toxic_fish_pic, toxic_fish_y)
        toxic_fishes.add(fish)
        fish.attack = True
        toxic_fish_count = 0

    if shark_count == shark_spawning:
        shark = Shark(shark_pic, shark_y)
        sharks.add(shark)
        shark.attack = True
        shark_count = 0

def groups_update():
    big_fish.update()
    big_fish.draw(screen)
    small_fishes.update()
    small_fishes.draw(screen)
    toxic_fishes.update()
    toxic_fishes.draw(screen)
    sharks.update()
    sharks.draw(screen)

def collision(player, friends, toxic_fish, sharks):
    global game_active, chances
    for friend in friends:
        if pygame.sprite.spritecollideany(player, friends):
            player.heal = True
            friend.kill()


    for enemy in toxic_fish:
        if pygame.sprite.spritecollideany(player, toxic_fish):
            player.damage = True
            enemy.kill()

    for shark in sharks:
        if pygame.sprite.spritecollideany(player, sharks):
            game_active = False
            shark.kill()

def resume():
    playagain_surf = screen_font.render('To resume the game press "space" ...', False, 'Black')
    playagain_rect = playagain_surf.get_rect(center=(500, 125))
    screen.blit(playagain_surf, playagain_rect)
    pygame.display.update()

    resume = True
    while resume:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    resume = False
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def healthbar():
    pygame.draw.rect(screen, RED, (player.rect.x, player.rect.y, 40, 5))
    pygame.draw.rect(screen, GREEN, (player.rect.x, player.rect.y, player.health, 5))

def text():
    level_surf = screen_font.render('Level: ' + str(level), False, 'WHITE')
    level_rect = level_surf.get_rect(center=(750, 20))
    screen.blit(level_surf, level_rect)

def game_over():
    game_over_surf = game_over_font.render('You lost :(', False, 'RED')
    game_over_rect = game_over_surf.get_rect(center=(screen_height/2, screen_height/2))
    screen.blit(game_over_surf, game_over_rect)

    restart_surf = screen_font.render('To play again press enter...', False, 'RED')
    restart_rect = restart_surf.get_rect(center=(screen_height / 2, 200))
    screen.blit(restart_surf, restart_rect)



def player_input():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            player.up = True
        if event.key == pygame.K_DOWN:
            player.down = True
        if event.key == pygame.K_LEFT:
            player.forward = True
        if event.key == pygame.K_RIGHT:
            player.backward = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            player.up = False
        if event.key == pygame.K_DOWN:
            player.down = False
        if event.key == pygame.K_LEFT:
            player.forward = False
        if event.key == pygame.K_RIGHT:
            player.backward = False



def level_update():
    global score_count, fish_spawning, toxic_fish_spawning, shark_spawning, level, fish_speed, shark_speed
    if score_count >= level_count:
        fish_spawning -= 10
        toxic_fish_spawning -= 20
        shark_spawning -= 50
        score_count = 0
        level += 1
    if level >= 5:
        fish_spawning = 70
        toxic_fish_spawning = 120
        shark_spawning = 250
    if level >= 3:
        fish_speed += 1
        shark_speed += 2

game_active = True

while game_active:
    score_count += 1
    fish_count += 1
    toxic_fish_count += 1
    shark_count += 1
    healthy_fish_y = random.randint(20, screen_height - 20)
    toxic_fish_y = random.randint(20, screen_height - 20)
    shark_y = random.randint(20, screen_height - 20)

    if game_active == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            player_input()
        spawning_logic()

        if player.health <= 0 or chances <= 0:
            game_over()
            time.sleep(2)
            game_active = False

        level_update()
        screen.blit(background, (0, 0))
        collision(player, small_fishes, toxic_fishes, sharks)
        text()
        groups_update()
        healthbar()
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
