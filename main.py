import pygame
import random

pygame.init()
frame_size_x = 400
frame_size_y = 800
window_screen = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption("Tetris quest")
clock = pygame.time.Clock()
game_init = False
color = (0, 0, 255)
font = pygame.font.SysFont(None, 32)
FPS = 60
blocks = []

last_spawn_time = 0  # Track the last time a block was spawned
spawn_interval = 5000  # Interval in milliseconds (1000 ms = 1 second)

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

def spawn_block_init():
    global last_spawn_time
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time >= spawn_interval:
        spawn_blocks()
        last_spawn_time = current_time

def spawn_blocks():
    randnum = random.randint(1,2)
    print(randnum)
    if randnum == 1:
        block = pygame.Rect(30, 30, 60, 60)
        block_2 = pygame.Rect (60,30,60,60)
        block_united1 = pygame.Rect.union(block,block_2,)
        blocks.append(block_united1)
    else:
        block_3 = pygame.Rect(30,30,60,60)
        block_4 = pygame.Rect(30,60,60,60)
        block_united2 = pygame.Rect.union(block_3,block_4)
        blocks.append(block_united2)
            
def block_gravity():
    for block in blocks:
        if block.bottom > 798:
            block.move_ip(0,0)
        else:
            block.move_ip(0, 5)
        pygame.draw.rect(window_screen, color, block)

        # cleanup
        if block.midtop[1] > 800:
            blocks.remove(block)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_init = True
                print("Game active")
    start_screen()
    game_active()
    pygame.display.update()
    clock.tick(FPS)