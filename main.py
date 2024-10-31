import pygame

pygame.init()
frame_size_x = 400
frame_size_y = 800
window_screen = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption("Tetris quest")
clock = pygame.time.Clock()
# score = 0 
# high_score = 0 
game_init = False
font = pygame.font.SysFont(None, 32)
FPS = 60

def start_screen():
    game_message = font.render("press space to start", False, "white")
    game_message_rect = game_message.get_rect(
    center=(frame_size_x//2, frame_size_y//1.5))
    if game_init == False:
        window_screen.blit(game_message, game_message_rect)
    # score = display_score()

def game_active():
    if game_init== True:
        window_screen.fill((10,10,10))
    

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
