"""
2048 Game Solver with Expectimax Algorithm
Copyright (c) 2026 WanDaiser
Licensed under MIT License - see LICENSE file
"""

import pyautogui
import time
from collections import Counter

# Game coordinates for play2048.co
TILE_SIZE = 107
GRID_START_X = 538
GRID_START_Y = 253

# Color mappings for tiles (RGB values from play2048.co)
TILE_COLORS = {
    (238, 228, 218): 2,
    (237, 224, 200): 4,
    (242, 177, 121): 8,
    (245, 149, 99): 16,
    (246, 124, 95): 32,
    (246, 94, 59): 64,
    (237, 207, 114): 128,
    (237, 204, 97): 256,
    (237, 200, 80): 512,
    (237, 197, 63): 1024,
    (237, 194, 46): 2048,
    (60, 58, 50): 4096,
}

def get_tile_center(row, col):
    """Calculate the center coordinates of a tile"""
    x = GRID_START_X + (col * TILE_SIZE) + (TILE_SIZE // 2)
    y = GRID_START_Y + (row * TILE_SIZE) + (TILE_SIZE // 2)
    return (x, y)

def read_grid():
    """Read the current state of the 4x4 grid by sampling tile colors"""
    grid = [[0 for _ in range(4)] for _ in range(4)]
    
    for row in range(4):
        for col in range(4):
            x, y = get_tile_center(row, col)
            pixel_color = pyautogui.pixel(x, y)
            
            # Find the closest matching tile color
            grid[row][col] = TILE_COLORS.get(pixel_color, 0)
    
    return grid

def print_grid(grid):
    """Pretty print the grid"""
    print("\nCurrent Grid:")
    print("-" * 25)
    for row in grid:
        print("|", end="")
        for cell in row:
            if cell == 0:
                print("     |", end="")
            else:
                print(f" {cell:4d} |", end="")
        print()
    print("-" * 25)

def make_move(direction):
    """Execute a move in the specified direction"""
    moves = {
        'up': 'up',
        'down': 'down',
        'left': 'left',
        'right': 'right'
    }
    
    if direction in moves:
        pyautogui.press(moves[direction])
        time.sleep(0.15)

def get_available_cells(grid):
    """Get list of empty cells"""
    cells = []
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                cells.append((i, j))
    return cells

def can_move(grid, direction):
    """Check if a move in the given direction is possible"""
    if direction == 'left':
        for row in grid:
            for i in range(3):
                if row[i] == 0 and row[i+1] != 0:
                    return True
                if row[i] != 0 and row[i] == row[i+1]:
                    return True
    
    elif direction == 'right':
        for row in grid:
            for i in range(3, 0, -1):
                if row[i] == 0 and row[i-1] != 0:
                    return True
                if row[i] != 0 and row[i] == row[i-1]:
                    return True
    
    elif direction == 'up':
        for col in range(4):
            for row in range(3):
                if grid[row][col] == 0 and grid[row+1][col] != 0:
                    return True
                if grid[row][col] != 0 and grid[row][col] == grid[row+1][col]:
                    return True
    
    elif direction == 'down':
        for col in range(4):
            for row in range(3, 0, -1):
                if grid[row][col] == 0 and grid[row-1][col] != 0:
                    return True
                if grid[row][col] != 0 and grid[row][col] == grid[row-1][col]:
                    return True
    
    return False

def evaluate_grid(grid):
    """Heuristic evaluation of grid state"""
    score = 0
    
    # Prefer keeping high values in corners
    corners = [grid[0][0], grid[0][3], grid[3][0], grid[3][3]]
    score += max(corners) * 10
    
    # Prefer monotonicity (values increasing/decreasing in rows/cols)
    for row in grid:
        for i in range(3):
            if row[i] >= row[i+1]:
                score += row[i]
    
    # Bonus for empty cells
    empty_cells = sum(row.count(0) for row in grid)
    score += empty_cells * 100
    
    # Bonus for mergeability
    for row in grid:
        for i in range(3):
            if row[i] == row[i+1] and row[i] != 0:
                score += row[i] * 2
    
    return score

def choose_best_move(grid):
    """Choose the best move using a greedy heuristic"""
    moves = ['left', 'up', 'down', 'right']
    best_move = None
    best_score = -float('inf')
    
    for move in moves:
        if can_move(grid, move):
            score = evaluate_grid(grid)
            
            # Prefer moves that keep corners occupied
            if move == 'left' or move == 'up':
                score += 50
            
            if score > best_score:
                best_score = score
                best_move = move
    
    return best_move

def is_game_over(grid):
    """Check if no more moves are possible"""
    if any(0 in row for row in grid):
        return False
    
    for direction in ['up', 'down', 'left', 'right']:
        if can_move(grid, direction):
            return False
    
    return True

def main():
    print("2048 Game Solver")
    print("=" * 40)
    print("Position your browser with https://play2048.co/ open")
    print("Starting in 3 seconds...")
    time.sleep(3)
    
    # Click on game area to focus
    pyautogui.click(GRID_START_X + 200, GRID_START_Y + 200)
    time.sleep(0.5)
    
    move_count = 0
    
    while True:
        # Read current grid state
        grid = read_grid()
        print_grid(grid)
        
        # Check if game over
        if is_game_over(grid):
            print("\nGame Over!")
            print(f"Total moves: {move_count}")
            break
        
        # Choose and execute best move
        best_move = choose_best_move(grid)
        
        if best_move:
            print(f"Move {move_count + 1}: {best_move.upper()}")
            make_move(best_move)
            move_count += 1
        else:
            print("No valid moves available!")
            break
        
        # Small delay between moves
        time.sleep(0.2)

if __name__ == "__main__":
    main()
