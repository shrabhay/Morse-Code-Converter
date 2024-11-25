# ReadMe for Text to Morse Code Converter
## Overview
This Python script is a Text to Morse Code and Morse Code to Text Converter. It allows users to seamlessly switch between text and Morse code translations, providing a quick and interactive way to encode and decode messages.

---

## Features
* Text to Morse Code Conversion:
  * Converts any English text (letters, numbers, and special characters) to Morse code.
  * Maintains spaces between words for clarity.

* Morse Code to Text Conversion:
  * Decodes Morse code back into plain English text.
  * Handles proper spacing for words and characters for accurate conversion.

* Interactive Interface:
  * Simple menu-driven input to select the desired operation.
  * User-friendly guidelines for Morse code input formatting.

---

## How to Use
1. Clone or download the repository to your local machine.
2. Run the script in any Python environment (Python 3.x is recommended).
3. Follow the prompts to:
   * Convert text to Morse code.
   * Convert Morse code back to text.

### Example
* Text to Morse Code:
```text
Input: Hello World
Output: .... . .-.. .-.. ---   .-- --- .-. .-.. -..
```

* Morse Code to Text:
```text
Input: .... . .-.. .-.. ---   .-- --- .-. .-.. -..
Output: HELLO WORLD
```

---

## Input Guidelines

### Text to Morse Code
* Enter any English string containing letters, numbers, or supported special characters.
* Spaces between words will be maintained in the Morse code output.

### Morse Code to Text
* Follow these rules:
  * Separate letters within a word with 1 space.
  * Separate words with 3 spaces.

---

## Requirements
* Python 3.x
* No external libraries are required.

---

## Script Details

### Modules Used:
* `os`: To clear the terminal screen for a cleaner interface.

### Key Data Structures:
* `TTMC`: Dictionary mapping text to Morse code.
* `MCTT`: Reverse mapping from Morse code to text.

### Functions:
* `text_to_morse()`: Handles text to Morse code conversion.
* `morse_to_text()`: Handles Morse code to text conversion.

---

## Contributing
Feel free to fork the repository, submit issues, or suggest enhancements. Contributions are welcome!
