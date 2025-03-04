import pygame
import random

pygame.init()
frame_size_x = 390
frame_size_y = 800
window_screen = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption("Tetris quest")
clock = pygame.time.Clock()
game_init = False
color = (0, 0, 255)
font = pygame.font.SysFont(None, 32)
FPS = 60
moving_block = []
static_block = []
should_spawn = True  # variable acting as a state
last_spawn_time = 0  # Track the last time a block was spawned
spawn_interval = 1000  # Interval in milliseconds (1000 ms = 1 second)


def start_screen():
    game_message = font.render("press space to start", False, "white")
    game_message_rect = game_message.get_rect(
        center=(frame_size_x//2, frame_size_y//1.5))
    if game_init == False:
        window_screen.blit(game_message, game_message_rect)


def game_active():
    if game_init == True:
        window_screen.fill((10, 10, 10))
        spawn_block_init()
        block_gravity()
        draw_static_blocks()


def spawn_block_init():
    global should_spawn
    if should_spawn == True:
        spawn_blocks()
        should_spawn = False

# spawn blocks only spawn once because once it spawns, should_spawn is set to true, then statement will not run anymore


def spawn_blocks():
    randnum = random.randint(1, 2)
    randcoordinates = random.randint(0, 12) * 30
    randcoordinates2 = random.randint(0, 11) * 30
    print(randcoordinates)
    # print(randnum)
    if randnum == 1:
        rectangleblock = pygame.Rect(30, 30, 60, 30)
        rectangleblock.bottomleft = (randcoordinates, 30)
        moving_block.append(rectangleblock)

    if randnum == 2:
        tallblock = pygame.Rect(30, 30, 30, 55)
        tallblock.bottomleft = (randcoordinates2, 30)
        moving_block.append(tallblock)


def block_gravity():
    global should_spawn
    for i, block in enumerate(moving_block):
        # Check for collisions with other blocks
        should_move = True

        # Check collision with other blocks
        if (block.collidelist(static_block) != -1):
            should_move = False
            static_block.append(block)
            moving_block.remove(block)
            should_spawn = True

        # adjust movement
        if should_move:
            if block.bottom < 798:
                block.move_ip(0, 5)

        if block.bottom >= 799:
            static_block.append(block)
            moving_block.remove(block)
            should_spawn = True

        pygame.draw.rect(window_screen, color, block)

        # cleanup blocks that are off screen
        if block.midtop[1] > 800:
            moving_block.remove(block)


def draw_static_blocks():
    for i, block in enumerate(static_block):
        pygame.draw.rect(window_screen, color, block)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if (moving_block):
                    if (moving_block[0].right < 389):
                        moving_block[0].move_ip(30, 0)

            if event.key == pygame.K_LEFT:
                if (moving_block):
                    if (moving_block[0].left > 1):
                        moving_block[0].move_ip(-30, 0)

            if event.key == pygame.K_SPACE:
                game_init = True
                print("Game active")
    start_screen()
    game_active()
    pygame.display.update()
    clock.tick(FPS)
