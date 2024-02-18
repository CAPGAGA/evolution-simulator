import pygame

from Cell import Cell

CELL_NUM = 100
pygame.init()

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.display.set_caption('Evolution Simulator')
running = True
dt = 0


cells = []
for i in range(CELL_NUM):
    cells.append(Cell(screen.get_width(), screen.get_height()))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color(245, 245, 245))


    for cell in cells:
        cell.move()
        if cell.x_pos >= 10 and cell.x_pos <= screen.get_width()-10:
            pygame.draw.circle(screen, pygame.Color(cell.color), pygame.Vector2(cell.x_pos, cell.y_pos), cell.size)
    # pygame.draw.circle(screen, 'red', player_pos, 10)

    # keys = pygame.key.get_pressed()
    #
    # if keys[pygame.K_w]:
    #     player_pos.y -= 300 * dt
    #
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    #
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 * dt
    #
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()