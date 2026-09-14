import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

PLAYER_START_X = 370
PLAYER_START_Y = 400

PLAYER_SPEED = 5

ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150

ENEMY_SPEED_X = 3
ENEMY_DROP_DISTANCE = 35

BULLET_SPEED = 8

NUM_OF_ENEMIES = 6

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Space Invader")

clock = pygame.time.Clock()


def load_image(filename, size):
    image = pygame.image.load(filename).convert_alpha()
    image = pygame.transform.smoothscale(image, size)
    return image


# Background

background = pygame.image.load("space.png").convert()

background = pygame.transform.smoothscale(
    background,
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)


# Icon

icon = pygame.image.load("ufo.png").convert_alpha()
icon = pygame.transform.smoothscale(icon, (32, 32))

pygame.display.set_icon(icon)


# Player

PLAYER_WIDTH = 64
PLAYER_HEIGHT = 64

playerImg = load_image(
    "player.png",
    (PLAYER_WIDTH, PLAYER_HEIGHT)
)

playerX = PLAYER_START_X
playerY = PLAYER_START_Y

playerX_change = 0


# Enemy

ENEMY_WIDTH = 55
ENEMY_HEIGHT = 55

enemyImg = load_image(
    "enemy.png",
    (ENEMY_WIDTH, ENEMY_HEIGHT)
)

enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []


for i in range(NUM_OF_ENEMIES):
    enemyX.append(
        random.randint(
            0,
            SCREEN_WIDTH - ENEMY_WIDTH
        )
    )

    enemyY.append(
        random.randint(
            ENEMY_START_Y_MIN,
            ENEMY_START_Y_MAX
        )
    )

    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_DROP_DISTANCE)


# Bullet

BULLET_WIDTH = 8
BULLET_HEIGHT = 25

bulletImg = load_image(
    "bullet.png",
    (BULLET_WIDTH, BULLET_HEIGHT)
)

bulletX = 0
bulletY = PLAYER_START_Y

bullet_state = "ready"


# Score

score_value = 0

font = pygame.font.Font(
    "freesansbold.ttf",
    32
)

textX = 10
textY = 10


# Game Over

over_font = pygame.font.Font(
    "freesansbold.ttf",
    64
)

game_over = False


def show_score(x, y):
    score = font.render(
        "Score : " + str(score_value),
        True,
        (255, 255, 255)
    )

    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render(
        "GAME OVER",
        True,
        (255, 255, 255)
    )

    text_rect = over_text.get_rect(
        center=(
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2
        )
    )

    screen.blit(over_text, text_rect)


def player(x, y):
    screen.blit(
        playerImg,
        (x, y)
    )


def enemy(x, y):
    screen.blit(
        enemyImg,
        (x, y)
    )


def fire_bullet(x, y):
    global bullet_state

    bullet_state = "fire"

    bullet_x = (
        x
        + PLAYER_WIDTH // 2
        - BULLET_WIDTH // 2
    )

    screen.blit(
        bulletImg,
        (bullet_x, y)
    )


def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    enemy_rect = pygame.Rect(
        enemy_x,
        enemy_y,
        ENEMY_WIDTH,
        ENEMY_HEIGHT
    )

    bullet_rect = pygame.Rect(
        bullet_x,
        bullet_y,
        BULLET_WIDTH,
        BULLET_HEIGHT
    )

    return enemy_rect.colliderect(bullet_rect)


# Game Loop

running = True

while running:

    screen.blit(
        background,
        (0, 0)
    )

    # Event handling

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -PLAYER_SPEED

            if event.key == pygame.K_RIGHT:
                playerX_change = PLAYER_SPEED

            if (
                event.key == pygame.K_SPACE
                and bullet_state == "ready"
                and not game_over
            ):
                bulletX = (
                    playerX
                    + PLAYER_WIDTH // 2
                    - BULLET_WIDTH // 2
                )

                bulletY = playerY

                bullet_state = "fire"

        if event.type == pygame.KEYUP:

            if event.key in (
                pygame.K_LEFT,
                pygame.K_RIGHT
            ):
                playerX_change = 0

    # Game continues only if the player is not defeated

    if not game_over:

        # Player movement

        playerX += playerX_change

        playerX = max(
            0,
            min(
                playerX,
                SCREEN_WIDTH - PLAYER_WIDTH
            )
        )

        # Enemy movement

        for i in range(NUM_OF_ENEMIES):

            enemyX[i] += enemyX_change[i]

            if (
                enemyX[i] <= 0
                or enemyX[i] >= SCREEN_WIDTH - ENEMY_WIDTH
            ):
                enemyX_change[i] *= -1
                enemyY[i] += enemyY_change[i]

            # Game Over condition

            if enemyY[i] + ENEMY_HEIGHT >= playerY:
                game_over = True
                break

            # Bullet collision

            if bullet_state == "fire":

                if isCollision(
                    enemyX[i],
                    enemyY[i],
                    bulletX,
                    bulletY
                ):

                    bulletY = playerY
                    bullet_state = "ready"

                    score_value += 1

                    enemyX[i] = random.randint(
                        0,
                        SCREEN_WIDTH - ENEMY_WIDTH
                    )

                    enemyY[i] = random.randint(
                        ENEMY_START_Y_MIN,
                        ENEMY_START_Y_MAX
                    )

            # Draw enemy

            enemy(
                enemyX[i],
                enemyY[i]
            )

        # Bullet movement

        if bullet_state == "fire":

            bulletY -= BULLET_SPEED

            if bulletY <= 0:

                bulletY = playerY
                bullet_state = "ready"

            else:

                fire_bullet(
                    bulletX,
                    bulletY
                )

    # Draw player

    player(
        playerX,
        playerY
    )

    # Draw score

    show_score(
        textX,
        textY
    )

    # Game over message

    if game_over:
        game_over_text()

    # Update display

    pygame.display.update()

    clock.tick(60)


pygame.quit()
