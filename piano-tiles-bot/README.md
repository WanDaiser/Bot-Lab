# Piano Tiles Bot 🎹

Automated bot for Piano Tiles (Don't Tap the White Tile) style games using pixel detection and Windows API for fast clicking.

## Features

- **Pixel-Based Detection**: Monitors specific screen coordinates for black tiles
- **Fast Win32 API Clicking**: Uses `win32api` for faster mouse events than PyAutoGUI
- **Grid-Based System**: Checks a 4x4 grid of tile positions
- **Keyboard Control**: Press 'Q' to stop the bot at any time
- **Zero Latency**: Optimized for speed with minimal delay

## How It Works

1. **Pixel Monitoring**: Continuously checks RGB values at predefined coordinates
2. **Black Tile Detection**: Identifies tiles where `pixel[0] == 0` (black color)
3. **Instant Click**: Uses Win32 API to click detected tiles immediately
4. **Loop Execution**: Repeats until 'Q' key is pressed

## Technology Stack

- **PyAutoGUI**: Screen pixel reading
- **win32api/win32con**: Low-level mouse control for faster clicks
- **keyboard**: Keyboard event detection for exit control

## Installation

```bash
pip install pyautogui pywin32 keyboard
```

## Usage

1. Open a Piano Tiles game in your browser
2. Adjust coordinates in the script to match your screen resolution
3. Run the script:

```bash
python donttap.py
```

4. The bot will start clicking black tiles automatically
5. Press 'Q' to stop

## Configuration

The bot checks these coordinates in a 4x4 grid pattern:

```python
# Top row
(743, 360), (890, 349), (1010, 348), (1165, 338)

# Second row  
(1180, 485), (1031, 476), (862, 475), (740, 469)

# Third row
(751, 619), (902, 619), (1048, 617), (1182, 624)

# Bottom row
(1201, 800), (1012, 771), (875, 768), (730, 766)
```

**Note**: You may need to adjust these coordinates based on your screen resolution and game window position.

## Customization

### Finding Coordinates

Use this snippet to find tile positions on your screen:

```python
import pyautogui
import time

time.sleep(3)  # Position your mouse
x, y = pyautogui.position()
print(f"X: {x}, Y: {y}")
```

### Adjusting Click Delay

Modify the delay in the `click()` function:

```python
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)  # Adjust this value
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
```

## Performance

- **Click Speed**: ~10ms per click (Win32 API)
- **Detection Rate**: Checks all 16 positions per loop
- **Success Rate**: Depends on screen refresh rate and game speed

## Disclaimer

This project is created for educational purposes to demonstrate:
- Pixel-based game automation
- Windows API usage in Python
- Real-time screen monitoring techniques

Use responsibly and in accordance with the terms of service of any platforms you interact with.

## Author

**WanDaiser**  
GitHub: [@WanDaiser](https://github.com/WanDaiser)

## License

MIT License - See LICENSE file for details
