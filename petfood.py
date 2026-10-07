import pygame, random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pet = pygame.Rect(380, 280, 40, 40)
food = [pygame.Rect(random.randint(20, 760),
                    random.randint(20, 560), 25, 25) for _ in range(8)]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    pet.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    pet.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5

    food = [f for f in food if not pet.colliderect(f)]

    screen.fill((80, 180, 90))
    pygame.draw.rect(screen, (50, 100, 220), pet)

    for f in food:
        pygame.draw.rect(screen, (255, 220, 0), f)

    if not food:
        font = pygame.font.Font(None, 45)
        text = font.render("All Food Collected!", True, "white")
        screen.blit(text, text.get_rect(center=(400, 300)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
