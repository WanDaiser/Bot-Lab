# Game Automation Bots C### Don't Tap Game Bot

Pixel-based automation using Win32 API for ultra-fast tile detection and clicking.ection

A collection of Python automation bots demonstrating computer vision, pixel detection, and web automation techniques for various browser-based games.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Projects Overview

### Number Memory Bot (Featured)

Advanced computer vision bot using OpenCV template matching and custom Non-Maximum Suppression algorithm.

**Technologies:** OpenCV, NumPy, PIL, PyAutoGUI  
**[View Project →](./number-memory-bot/)**

**Key Features:**
- Custom NMS algorithm for duplicate elimination
- Template-based digit recognition
- Confidence scoring system
- Automated 50-round gameplay

---

### 2048 Game Solver

Heuristic-based puzzle solver with color detection and automated gameplay.

**Technologies:** PyAutoGUI, Python algorithms  
**[View Project →](./2048-game-solver/)**

**Key Features:**
- Color-based grid state reading
- Heuristic evaluation algorithm
- Corner strategy optimization
- Real-time move execution

---

### � Don't Tap Game Bot

Pixel-based automation using Win32 API for ultra-fast tile detection and clicking.

**Technologies:** PyAutoGUI, win32api, keyboard  
**[View Project →](./piano-tiles-bot/)**

**Key Features:**
- Win32 API for low-latency clicks
- 4x4 grid monitoring system
- Real-time pixel detection
- Keyboard interrupt support

---

### Typing Practice Automation

Selenium-based web automation for 10-finger typing practice.

**Technologies:** Selenium, ChromeDriver, XPath  
**[View Project →](./typing-automation/)**

**Key Features:**
- Dynamic XPath element selection
- Browser automation
- Configurable typing speed
- 3000+ word automation

---

## Technology Stack

| Category | Technologies |
|----------|-------------|
| **Computer Vision** | OpenCV, NumPy, PIL |
| **GUI Automation** | PyAutoGUI, win32api |
| **Web Automation** | Selenium, ChromeDriver |
| **Image Processing** | Template Matching, Pixel Detection |
| **Algorithms** | Non-Maximum Suppression, Grid Monitoring |

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Install All Dependencies

```bash
# Computer Vision (Number Memory Bot)
pip install opencv-python numpy pillow pyautogui

# Pixel Detection (Piano Tiles Bot)
pip install pyautogui pywin32 keyboard

# Web Automation (Typing Bot)
pip install selenium webdriver-manager
```

Or install from requirements.txt:

```bash
pip install -r requirements.txt
```

## Quick Start

### Number Memory Bot

```bash
cd number-memory-bot
python numbermemory.py
```

### 2048 Game Solver

```bash
cd 2048-game-solver
python solver2048.py
```

### Don't Tap Game Bot

```bash
cd piano-tiles-bot
python donttap.py
```

### Typing Automation

```bash
cd typing-automation
python otoyazar.py
```

## Project Structure

```
game-automation-bots/
├── README.md                    # This file
├── LICENSE                      # MIT License
├── requirements.txt             # All dependencies
├── .gitignore                   # Git ignore rules
│
├── number-memory-bot/           # Featured Project
│   ├── README.md
│   ├── numbermemory.py
│   └── templates/               # Digit templates (0-9)
│       ├── 0/
│       ├── 1/
│       └── ...
│
├── 2048-game-solver/
│   ├── README.md
│   └── solver2048.py
│
├── piano-tiles-bot/
│   ├── README.md
│   └── donttap.py
│
└── typing-automation/
    ├── README.md
    └── otoyazar.py
```

## Educational Value

These projects demonstrate:

1. **Computer Vision Fundamentals**
   - Template matching algorithms
   - Image preprocessing techniques
   - Multi-object detection

2. **Automation Techniques**
   - GUI automation with PyAutoGUI
   - Low-level Windows API usage
   - Web scraping and interaction

3. **Algorithm Implementation**
   - Custom NMS algorithm
   - Coordinate-based detection
   - Dynamic element selection

4. **Software Engineering**
   - Code organization
   - Error handling
   - Documentation practices

## Use Cases

- **Learning**: Understand automation and CV concepts
- **Portfolio**: Showcase technical skills to employers
- **Research**: Study game automation techniques
- **Practice**: Improve Python programming skills

## Disclaimer

These bots are created for **educational purposes** to demonstrate:
- Computer vision techniques
- Python automation capabilities
- Software development practices

**Important Notes:**
- Use responsibly and ethically
- Respect terms of service of platforms
- Not intended for competitive advantage
- For learning and demonstration only

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## Roadmap

Future enhancements:
- Implement expectimax algorithm for 2048
- Add Monte Carlo tree search
- Create more game solvers
- Improve AI decision making

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**WanDaiser**  
GitHub: [@WanDaiser](https://github.com/WanDaiser)

---

If you find this project useful, please consider giving it a star on GitHub!

**Note:** Always use automation tools responsibly and in accordance with applicable terms of service.
