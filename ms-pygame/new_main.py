import pygame


pygame.init()
clock = pygame.time.Clock()
running = True

maze_size = (5, 5)
cell_size = (70, 70)

window_size = ((cell_size[0] * maze_size[0]), (cell_size[1] * maze_size[1]))
window = pygame.display.set_mode(window_size)
window.fill((255, 255, 255))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()
