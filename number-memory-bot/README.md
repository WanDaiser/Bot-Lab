# Number Memory Bot

Advanced computer vision bot that automatically solves the [Human Benchmark Number Memory](https://humanbenchmark.com/tests/number-memory) game using OpenCV template matching.

## Features

- **Template Matching**: Uses OpenCV's template matching algorithm for digit recognition
- **Custom NMS Algorithm**: Implements Non-Maximum Suppression to eliminate duplicate detections
- **Multi-digit Recognition**: Can recognize sequences of any length
- **Confidence Scoring**: Filters detections based on confidence thresholds
- **Automated Gameplay**: Captures screen, recognizes digits, and inputs the answer automatically

## How It Works

1. **Screen Capture**: Takes a screenshot of the game area
2. **Template Loading**: Loads digit templates (0-9) from the templates folder
3. **Image Processing**: Converts to grayscale for better matching
4. **Digit Detection**: Uses `cv2.matchTemplate()` with correlation coefficient
5. **NMS Application**: Removes overlapping detections using custom algorithm
6. **Sorting**: Orders digits left-to-right based on x-coordinates
7. **Automation**: Inputs the detected number sequence into the game

## Technology Stack

- **OpenCV (cv2)**: Template matching and image processing
- **NumPy**: Array operations and numerical computing
- **PIL (Pillow)**: Screen capture functionality
- **PyAutoGUI**: Mouse/keyboard automation

## Installation

```bash
pip install opencv-python numpy pillow pyautogui
```

## Usage

1. Open the Number Memory game in your browser
2. Position the game window appropriately
3. Run the script:

```bash
python numbermemory.py
```

4. The bot will automatically:
   - Wait 2 seconds
   - Capture the screen
   - Recognize all digits
   - Input the answer
   - Repeat for 50 rounds

## Template System

The bot uses template images stored in `templates/0/`, `templates/1/`, ... `templates/9/` folders. Each folder contains sample images of that digit from the game.

## Configuration

You can adjust these parameters in the code:

- `TEMPLATE_DIR`: Path to template images
- `SCREEN_REGION`: Screen capture area (x1, y1, x2, y2)
- `threshold`: Confidence threshold for matches (default: 0.65)
- `min_distance`: Minimum distance for NMS (default: 15 pixels)

## Algorithm: Non-Maximum Suppression

The custom NMS algorithm prevents duplicate detections:

```python
def non_max_suppression(detections, min_distance=15):
    # Sort by x-coordinate
    # Compare each detection with kept ones
    # Keep higher confidence detections
    # Filter based on x and y distance
```

## Sample Output

```
[DEBUG] Loading template: templates/0/0.png
[DEBUG] Loading template: templates/1/1.png
...
[DEBUG] Digit 4 found at (512, 300) with confidence 0.892
[DEBUG] Digit 2 found at (568, 302) with confidence 0.871
[DEBUG] Digit 7 found at (624, 298) with confidence 0.903
Detected number: 427
Total digits: 3
Process completed!
```

## Educational Purpose

This project is created for educational purposes to demonstrate:
- Computer vision techniques
- Template matching algorithms
- Image processing with OpenCV
- Python automation capabilities

## Disclaimer

This bot is designed for learning and demonstration purposes. Use responsibly and in accordance with the terms of service of any platforms you interact with.

## Author

**WanDaiser**  
GitHub: [@WanDaiser](https://github.com/WanDaiser)

## License

MIT License - See LICENSE file for details
