import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Background")

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 120, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Wave animation variables
wave_offset = 0
wave_speed = 2
amplitude = 50  # Wave height
frequency = 0.05  # Wave frequency

def draw_wavy_background():
    global wave_offset
    for y in range(0, HEIGHT, 20):  # Wave spacing
        for x in range(0, WIDTH, 10):  # Point spacing
            wave = math.sin((x * frequency) + wave_offset) * amplitude
            pygame.draw.circle(screen, BLUE, (x, int(y + wave)), 2)
    wave_offset += wave_speed * 0.1  # Animate the wave

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_wavy_background()
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 frames per second

pygame.quit()
