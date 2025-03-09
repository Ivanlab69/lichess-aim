import pygame
import random
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

# Load chess piece images
piece_img = pygame.image.load("piece.png")  # Replace with actual piece image
piece_img = pygame.transform.scale(piece_img, (50, 50))

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lichess Aim Trainer")

# Game variables
piece_x, piece_y = random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)
score = 0
start_time = time.time()
clicks = 0

def reset_piece():
    global piece_x, piece_y
    piece_x, piece_y = random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)

def draw_text(text, x, y):
    render = FONT.render(text, True, BLACK)
    screen.blit(render, (x, y))

# Main loop
running = True
while running:
    screen.fill(WHITE)
    screen.blit(piece_img, (piece_x, piece_y))
    draw_text(f"Score: {score}", 10, 10)
    draw_text(f"Clicks: {clicks}", 10, 40)
    draw_text(f"Time: {int(time.time() - start_time)}s", 10, 70)

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicks += 1
            x, y = event.pos
            if piece_x <= x <= piece_x + 50 and piece_y <= y <= piece_y + 50:
                score += 1
                reset_piece()

pygame.quit()
