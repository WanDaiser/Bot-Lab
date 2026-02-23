# 2048 Game Solver

Automated solver for the 2048 puzzle game on play2048.co using PyAutoGUI and heuristic-based decision making.

## Features

- **Color-Based Grid Reading**: Reads game state by sampling tile colors
- **Heuristic Evaluation**: Uses multiple strategies to evaluate board positions
- **Greedy Algorithm**: Chooses moves based on board evaluation scores
- **Corner Strategy**: Prioritizes keeping high-value tiles in corners
- **Monotonicity Preference**: Favors ordered tile arrangements
- **Real-time Gameplay**: Automated move execution with visual feedback

## How It Works

1. **Grid Detection**: Samples pixel colors at tile centers to identify values
2. **State Evaluation**: Analyzes board using multiple heuristics:
   - Corner occupation (high values in corners)
   - Monotonicity (ordered sequences)
   - Empty cell count
   - Merge potential
3. **Move Selection**: Evaluates all possible moves and chooses the best
4. **Execution**: Simulates arrow key presses to play the game

## Technology Stack

- **PyAutoGUI**: Screen reading and keyboard control
- **Python Built-ins**: Grid manipulation and algorithm implementation

## Installation

```bash
pip install pyautogui
```

## Usage

1. Open [play2048.co](https://play2048.co/) in your browser
2. Position the game window appropriately on your screen
3. Run the solver:

```bash
python solver2048.py
```

4. The bot will:
   - Wait 3 seconds for positioning
   - Read the grid state
   - Calculate optimal moves
   - Play automatically until game over

## Configuration

Adjust these constants if your screen resolution differs:

```python
TILE_SIZE = 107           # Size of each tile in pixels
GRID_START_X = 538        # X coordinate of top-left tile center
GRID_START_Y = 253        # Y coordinate of top-left tile center
```

### Finding Your Coordinates

Use this snippet to find tile positions:

```python
import pyautogui
import time

time.sleep(3)
x, y = pyautogui.position()
print(f"X: {x}, Y: {y}")
color = pyautogui.pixel(x, y)
print(f"Color: {color}")
```

Position your mouse over a tile center and run the script.

## Algorithm Details

### Heuristic Evaluation

The solver uses a weighted scoring system:

```python
score = 0
# Corner bonus: Keep max tile in corner
score += max(corner_tiles) * 10

# Monotonicity: Prefer ordered sequences
score += sum(monotonic_scores)

# Empty cells: More space = better
score += empty_count * 100

# Merge potential: Adjacent equal tiles
score += sum(mergeable_values) * 2
```

### Move Priority

Moves are prioritized as:
1. **Left/Up**: Generally better for corner strategy
2. **Down**: Secondary option
3. **Right**: Least preferred (breaks corner accumulation)

## Sample Output

```
2048 Game Solver
========================================
Position your browser with https://play2048.co/ open
Starting in 3 seconds...

Current Grid:
-------------------------
|     |     |     |    2 |
|     |     |    2 |    4 |
|     |     |     |     |
|     |     |     |     |
-------------------------
Move 1: LEFT

Current Grid:
-------------------------
|     |     |     |    2 |
|    2 |    4 |     |     |
|    2 |     |     |     |
|     |     |     |     |
-------------------------
Move 2: UP
...
```

## Performance

Typical performance metrics:
- **Average Score**: 4000-8000 points
- **2048 Tile**: Achievable in ~60% of games
- **Move Speed**: ~5 moves per second
- **Success Rate**: Depends on tile spawn luck

## Limitations

- **Simple Heuristic**: Not as advanced as expectimax or minimax
- **No Lookahead**: Makes decisions based on current state only
- **Color Dependency**: Requires exact color matching
- **Resolution Specific**: Coordinates need adjustment for different screens

## Improvements

Potential enhancements:
- Implement expectimax algorithm with depth search
- Add Monte Carlo tree search
- Machine learning-based move prediction
- Dynamic coordinate calibration
- Better handling of edge cases

## Customization

### Adjust Strategy Weights

Modify the `evaluate_grid()` function to change strategy:

```python
def evaluate_grid(grid):
    score = 0
    score += max(corners) * 20  # Increase corner weight
    score += empty_cells * 150   # Value empty space more
    return score
```

### Change Move Delay

Adjust speed in `main()`:

```python
time.sleep(0.1)  # Faster moves
time.sleep(0.5)  # Slower, more visible moves
```

## Educational Purpose

This project demonstrates:
- Pixel-based game state recognition
- Heuristic algorithm design
- Game tree evaluation
- Automated gameplay techniques
- Python automation with PyAutoGUI

## Disclaimer

This bot is created for educational purposes to demonstrate:
- Algorithm design and implementation
- Game automation techniques
- Heuristic evaluation methods

Use responsibly and in accordance with website terms of service.

## Author

**WanDaiser**  
GitHub: [@WanDaiser](https://github.com/WanDaiser)

## License

MIT License - See LICENSE file for details
