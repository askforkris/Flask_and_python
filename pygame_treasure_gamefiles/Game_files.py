import pygame

pygame.init()

color = (255, 255, 255)
position = (0, 0)

# CREATING CANVAS
canvas = pygame.display.set_mode((500, 500))

# TITLE OF CANVAS
pygame.display.set_caption("Show Image")

image = pygame.image.load("images/gem2.png")
exit = False

while not exit:
    canvas.fill(color)
    canvas.blit(image, dest=position)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    pygame.display.update()
