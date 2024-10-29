import pygame

pygame.init()
frame_size_x = 400
frame_size_y = 800
window_screen = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption("Tetris quest")
clock = pygame.time.Clock()
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
        