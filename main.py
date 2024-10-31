import pygame

pygame.init()
frame_size_x = 400
frame_size_y = 800
window_screen = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption("Tetris quest")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)
FPS = 60

def start_screen():
    game_message = font.render("space", False, "white")
    game_message_rect = game_message.get_rect(
        center=(frame_size_x//2, frame_size_y//2))
    window_screen.blit(game_message, game_message_rect)


while True:
    for event in pygame.event.get():
        start_screen()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(FPS)
