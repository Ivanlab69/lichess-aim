import pygame
import random
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)
HIGHLIGHT_COLOR = (0, 255, 0)
FONT = pygame.font.Font(None, 36)
SQUARE_SIZE = 75

# Load chess piece images
piece_img = pygame.image.load("piece.png")  # Replace with actual piece image
piece_img = pygame.transform.scale(piece_img, (50, 50))

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lichess Aim Trainer")

# Game variables
piece_col, piece_row = random.randint(0, 7), random.randint(0, 7)
target_col, target_row = random.randint(0, 7), random.randint(0, 7)
score = 0
start_time = time.time()
clicks = 0
piece_dragging = False
piece_x, piece_y = piece_col * SQUARE_SIZE + 12, piece_row * SQUARE_SIZE + 12

def draw_board():
    for row in range(8):
        for col in range(8):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    
    # Highlight target square
    pygame.draw.rect(screen, HIGHLIGHT_COLOR, (target_col * SQUARE_SIZE, target_row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)

def reset_piece():
    global piece_col, piece_row, target_col, target_row, piece_x, piece_y
    piece_col, piece_row = random.randint(0, 7), random.randint(0, 7)
    target_col, target_row = random.randint(0, 7), random.randint(0, 7)
    piece_x, piece_y = piece_col * SQUARE_SIZE + 12, piece_row * SQUARE_SIZE + 12

def draw_text(text, x, y):
    render = FONT.render(text, True, BLACK)
    screen.blit(render, (x, y))

# Main loop
running = True
while running:
    screen.fill(WHITE)
    draw_board()
    screen.blit(piece_img, (piece_x, piece_y))
    draw_text(f"Score: {score}", 620, 10)
    draw_text(f"Clicks: {clicks}", 620, 40)
    draw_text(f"Time: {int(time.time() - start_time)}s", 620, 70)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if piece_x <= x <= piece_x + 50 and piece_y <= y <= piece_y + 50:
                piece_dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if piece_dragging:
                piece_dragging = False
                piece_col, piece_row = x // SQUARE_SIZE, y // SQUARE_SIZE
                if piece_col == target_col and piece_row == target_row:
                    score += 1
                    reset_piece()
            clicks += 1
        elif event.type == pygame.MOUSEMOTION and piece_dragging:
            piece_x, piece_y = event.pos
            piece_x -= 25  # Centering the piece while dragging
            piece_y -= 25

pygame.quit()

