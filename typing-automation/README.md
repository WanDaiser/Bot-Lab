# Typing Practice Automation ⌨️

Selenium-based automation script for practicing 10-finger typing on Turkish typing practice websites.

## Features

- **Web Automation**: Uses Selenium WebDriver to interact with typing practice sites
- **XPath Element Selection**: Dynamically finds text elements to type
- **Automatic Text Input**: Types the practice text automatically
- **Speed Control**: Configurable typing delay for practice or demonstration
- **Browser Integration**: Works with Chrome WebDriver

## How It Works

1. **Browser Launch**: Opens Chrome and navigates to the typing practice site
2. **Element Location**: Finds the input field and text spans using XPath
3. **Text Extraction**: Reads each word from the practice text
4. **Automated Typing**: Types each word with space separator
5. **Loop Execution**: Continues for specified number of words (default: 3000)

## Technology Stack

- **Selenium**: Web browser automation
- **ChromeDriver**: Chrome browser control
- **XPath**: Dynamic element selection

## Installation

### Install Python Package

```bash
pip install selenium
```

### Install ChromeDriver

1. Check your Chrome version: `chrome://version`
2. Download matching ChromeDriver from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
3. Add ChromeDriver to PATH or place in project directory

**Or use automated installation:**

```bash
pip install webdriver-manager
```

Then modify the script:

```python
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

## Usage

```bash
python otoyazar.py
```

The script will:
1. Open Chrome browser
2. Navigate to the typing practice site
3. Start typing automatically
4. Continue until iteration limit is reached

## Configuration

### Target Website

Default: `https://www.m5bilisim.com/tr/on-parmak/calisma/kelime/?m=46`

Change the URL in the script:

```python
driver.get("YOUR_WEBSITE_URL")
```

### Typing Speed

Adjust the delay between keystrokes:

```python
time.sleep(0.00001)  # Decrease for faster, increase for slower
```

### Word Count

Change the loop limit:

```python
while i < 3000:  # Modify this number
```

### Element Selectors

The script uses these XPath selectors:

```python
gc = driver.find_element(By.ID, "yaziyaz")  # Input field
gv = driver.find_elements(By.XPATH, "//*[@id='satir']/span[" + str(i) + "]")  # Text spans
```

Adjust these if the website structure changes.

## Use Cases

- **Typing Practice**: Learn 10-finger typing technique
- **Speed Demonstration**: Show typing automation capabilities
- **Web Automation Learning**: Understand Selenium basics
- **XPath Practice**: Learn dynamic element selection

## Code Structure

```python
# 1. Setup
driver = webdriver.Chrome()
driver.get(URL)

# 2. Main Loop
while i < MAX_WORDS:
    input_field = find_input()
    text = find_text_span(i)
    input_field.send_keys(text + " ")
    i += 1

# 3. Cleanup
driver.quit()
```

## Troubleshooting

### ChromeDriver Not Found

```bash
# Error: 'chromedriver' executable needs to be in PATH

# Solution: Use webdriver-manager (recommended)
pip install webdriver-manager
```

### Element Not Found

```python
# Add explicit waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "yaziyaz"))
)
```

### Website Changes

If the website structure changes, inspect the page and update XPath selectors.

## Ethical Considerations

This tool is designed for:
- ✅ Personal typing practice
- ✅ Learning web automation
- ✅ Demonstrating technical skills

**Not intended for:**
- ❌ Cheating on typing tests
- ❌ Misrepresenting typing abilities
- ❌ Violating website terms of service

## Disclaimer

This project is created for educational purposes to demonstrate:
- Selenium WebDriver usage
- XPath element selection
- Browser automation techniques

Use responsibly and ethically. Always respect the terms of service of websites you interact with.

## Author

**WanDaiser**  
GitHub: [@WanDaiser](https://github.com/WanDaiser)

## License

MIT License - See LICENSE file for details
