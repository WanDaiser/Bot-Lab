"""
2048 Game Solver - Simulated Version
Plays 2048 without reading the screen. User provides initial state,
then the bot simulates the game internally and just presses arrow keys.
"""

from pynput.keyboard import Key, Controller
import pyautogui
import time
import random
import copy

keyboard = Controller()

# Manually calibrated tile center coordinates (4x4 grid)
TILE_COORDS = [
    [(629, 294), (744, 290), (864, 285), (989, 287)],  # Row 0
    [(622, 410), (760, 409), (877, 408), (970, 420)],  # Row 1
    [(655, 523), (750, 528), (880, 528), (988, 526)],  # Row 2
    [(626, 651), (746, 647), (875, 653), (991, 651)],  # Row 3
]

# Tile colors (will expand as we see more tiles)
TILE_COLORS = {
    (189, 172, 151): 0,  # Empty
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
}

def get_tile_center(row, col):
    """Get the manually calibrated coordinates for a tile"""
    return TILE_COORDS[row][col]

def color_distance(c1, c2):
    """Calculate color distance"""
    return sum((c1[i] - c2[i])**2 for i in range(3)) ** 0.5

def get_tile_value(color):
    """Find closest matching tile color"""
    min_dist = float('inf')
    best_value = 0
    
    for tile_color, value in TILE_COLORS.items():
        dist = color_distance(color, tile_color)
        if dist < min_dist:
            min_dist = dist
            best_value = value
    
    return best_value if min_dist < 30 else 0  # Tolerance of 30

def read_grid_from_screen():
    """Read current grid state from screen"""
    grid = [[0]*4 for _ in range(4)]
    
    for row in range(4):
        for col in range(4):
            x, y = get_tile_center(row, col)
            pixel_color = pyautogui.pixel(x, y)
            grid[row][col] = get_tile_value(pixel_color)
    
    return grid

def print_grid(grid):
    """Print the game grid in a nice format"""
    print("\n" + "="*25)
    for row in grid:
        print("|", end="")
        for cell in row:
            if cell == 0:
                print("     |", end="")
            else:
                print(f" {cell:4} |", end="")
        print()
    print("="*25)

def get_initial_state():
    """Get initial game state from user"""
    print("\n2048 Game Solver - Simulated Mode")
    print("="*50)
    print("Enter the initial game state.")
    print("Grid positions are 1-4 for both row and column.")
    print("Example: '1 1 2' means row 1, column 1, value 2")
    print("Enter 'done' when finished.")
    print()
    
    grid = [[0]*4 for _ in range(4)]
    
    while True:
        inp = input("Enter position (row col value) or 'done': ").strip()
        if inp.lower() == 'done':
            break
        
        try:
            parts = inp.split()
            if len(parts) != 3:
                print("Format: row col value (e.g., 1 1 2)")
                continue
                
            row, col, value = map(int, parts)
            
            if not (1 <= row <= 4 and 1 <= col <= 4):
                print("Row and column must be between 1 and 4")
                continue
                
            if value not in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]:
                print("Value must be a valid 2048 tile (2, 4, 8, 16, ...)")
                continue
            
            grid[row-1][col-1] = value
            print(f"Set position ({row}, {col}) to {value}")
            print_grid(grid)
            
        except ValueError:
            print("Invalid input. Use format: row col value")
    
    return grid

def slide_row_left(row):
    """Slide a single row to the left and merge tiles"""
    # Remove zeros
    non_zero = [x for x in row if x != 0]
    
    # Merge adjacent equal tiles
    merged = []
    i = 0
    while i < len(non_zero):
        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i+1]:
            merged.append(non_zero[i] * 2)
            i += 2
        else:
            merged.append(non_zero[i])
            i += 1
    
    # Pad with zeros
    result = merged + [0] * (4 - len(merged))
    return result

def move_left(grid):
    """Move all tiles left"""
    new_grid = []
    for row in grid:
        new_grid.append(slide_row_left(row))
    return new_grid

def move_right(grid):
    """Move all tiles right"""
    new_grid = []
    for row in grid:
        reversed_row = list(reversed(row))
        slid = slide_row_left(reversed_row)
        new_grid.append(list(reversed(slid)))
    return new_grid

def move_up(grid):
    """Move all tiles up"""
    # Transpose, slide left, transpose back
    transposed = [[grid[row][col] for row in range(4)] for col in range(4)]
    moved = move_left(transposed)
    return [[moved[col][row] for col in range(4)] for row in range(4)]

def move_down(grid):
    """Move all tiles down"""
    # Transpose, slide right, transpose back
    transposed = [[grid[row][col] for row in range(4)] for col in range(4)]
    moved = move_right(transposed)
    return [[moved[col][row] for col in range(4)] for row in range(4)]

def grids_equal(grid1, grid2):
    """Check if two grids are the same"""
    for i in range(4):
        for j in range(4):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True

def can_move(grid, direction):
    """Check if a move is valid (changes the grid)"""
    moves = {
        'left': move_left,
        'right': move_right,
        'up': move_up,
        'down': move_down
    }
    new_grid = moves[direction](grid)
    return not grids_equal(grid, new_grid)

def add_random_tile(grid):
    """Add a new tile (2 or 4) to a random empty position"""
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    
    if not empty_cells:
        return grid
    
    row, col = random.choice(empty_cells)
    grid[row][col] = 2 if random.random() < 0.9 else 4
    return grid

def evaluate_grid(grid):
    """Evaluate grid quality using heuristics"""
    score = 0
    
    # Corner strategy - prefer max value in corners
    corners = [grid[0][0], grid[0][3], grid[3][0], grid[3][3]]
    max_corner = max(corners)
    score += max_corner * 10
    
    # Empty cells bonus
    empty_count = sum(row.count(0) for row in grid)
    score += empty_count * 100
    
    # Monotonicity - prefer rows/columns in order
    for row in grid:
        if all(row[i] >= row[i+1] for i in range(3) if row[i] != 0 and row[i+1] != 0):
            score += 50
    
    for col in range(4):
        column = [grid[row][col] for row in range(4)]
        if all(column[i] >= column[i+1] for i in range(3) if column[i] != 0 and column[i+1] != 0):
            score += 50
    
    # Merge potential
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1] and grid[i][j] != 0:
                score += grid[i][j] * 2
            if grid[j][i] == grid[j+1][i] and grid[j][i] != 0:
                score += grid[j][i] * 2
    
    return score

def choose_best_move(grid):
    """Choose the best move based on evaluation"""
    directions = ['left', 'up', 'down', 'right']
    best_move = None
    best_score = -1
    
    for direction in directions:
        if can_move(grid, direction):
            # Simulate the move
            moves = {
                'left': move_left,
                'right': move_right,
                'up': move_up,
                'down': move_down
            }
            new_grid = copy.deepcopy(grid)
            new_grid = moves[direction](new_grid)
            
            score = evaluate_grid(new_grid)
            
            if score > best_score:
                best_score = score
                best_move = direction
    
    return best_move

def is_game_over(grid):
    """Check if no moves are possible"""
    return not any(can_move(grid, d) for d in ['left', 'right', 'up', 'down'])

def press_key(direction):
    """Press the arrow key for the given direction"""
    keys = {
        'left': Key.left,
        'right': Key.right,
        'up': Key.up,
        'down': Key.down
    }
    keyboard.press(keys[direction])
    time.sleep(0.03)
    keyboard.release(keys[direction])

def main():
    print("\n" + "="*50)
    print("2048 GAME SOLVER - SCREEN READING MODE")
    print("="*50)
    print("\nThis bot reads the game from screen and plays automatically!")
    print("Coordinates calibrated for your screen.")
    print()
    
    print("Open play2048.co and start a game.")
    print("\nIMPORTANT: Click on the game board to focus it!")
    print("The bot will start in 3 seconds.")
    print("Press Ctrl+C to stop anytime.")
    print("="*50)
    
    for i in range(3, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)
    
    move_count = 0
    
    while True:
        # Read current grid from screen
        grid = read_grid_from_screen()
        
        # Check if game over
        if is_game_over(grid):
            print("\nGame Over! No valid moves available.")
            break
        
        move_count += 1
        
        print(f"\n{'='*50}")
        print(f"Move {move_count}")
        print('='*50)
        
        print("\nCurrent grid (from screen):")
        print_grid(grid)
        
        # Choose best move
        move = choose_best_move(grid)
        
        if move is None:
            print("\nGame Over! No valid moves available.")
            break
        
        print(f"\nBest move: {move.upper()}")
        
        # Press the actual key
        press_key(move)
        
        # Wait for animation to complete
        time.sleep(0.15)
        
        # Check for high score
        max_tile = max(max(row) for row in grid)
        if max_tile >= 2048:
            print(f"\nAchievement! Reached {max_tile} tile!")
        
        # Safety check
        if move_count > 1000:
            print("\nReached 1000 moves, stopping to prevent infinite loop.")
            break
    
    print("\n" + "="*50)
    print("GAME FINISHED")
    print("="*50)
    print(f"Total moves: {move_count}")
    print(f"Highest tile: {max(max(row) for row in grid)}")
    print_grid(grid)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nBot stopped by user.")
    except Exception as e:
        print(f"\n\nError: {e}")
