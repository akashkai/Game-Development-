import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
GRID_SIZE = WIDTH // 3

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Fonts
FONT = pygame.font.Font(None, 75)

# Game variables
grid = [[None, None, None], [None, None, None], [None, None, None]]
current_player = "X"
game_over = False


def draw_grid():
    for x in range(1, 3):
        pygame.draw.line(screen, BLACK, (x * GRID_SIZE, 0), (x * GRID_SIZE, HEIGHT), 5)
        pygame.draw.line(screen, BLACK, (0, x * GRID_SIZE), (WIDTH, x * GRID_SIZE), 5)


def draw_marks():
    for row in range(3):
        for col in range(3):
            if grid[row][col] == "X":
                color = RED
            elif grid[row][col] == "O":
                color = BLUE
            else:
                continue

            mark = FONT.render(grid[row][col], True, color)
            screen.blit(
                mark,
                (col * GRID_SIZE + GRID_SIZE // 4, row * GRID_SIZE + GRID_SIZE // 4),
            )


def check_winner():
    global game_over
    # Check rows and columns
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] is not None:
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] is not None:
            return grid[0][i]

    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] is not None:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] is not None:
        return grid[0][2]

    # Check for tie
    for row in grid:
        for cell in row:
            if cell is None:
                return None

    return "Tie"


def reset_game():
    global grid, current_player, game_over
    grid = [[None, None, None], [None, None, None], [None, None, None]]
    current_player = "X"
    game_over = False


# Main game loop
while True:
    screen.fill(WHITE)
    draw_grid()
    draw_marks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // GRID_SIZE, x // GRID_SIZE

            if grid[row][col] is None:
                grid[row][col] = current_player
                winner = check_winner()
                if winner:
                    game_over = True
                    if winner != "Tie":
                        print(f"{winner} wins!")
                    else:
                        print("It's a tie!")
                current_player = "O" if current_player == "X" else "X"

        if game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

    pygame.display.flip()
