# Educational Keylogger

This is a simple cross-platform keylogger developed for educational purposes and cybersecurity portfolios. The keylogger demonstrates basic keyboard input monitoring functionality on both Windows and Linux systems.

## Disclaimer

**IMPORTANT**: This software is for EDUCATIONAL PURPOSES ONLY. Unauthorized use of this keylogger to collect data from users without their explicit consent is illegal and unethical. The author assumes no liability for misuse of this software.

## Features

- Cross-platform compatibility (Windows and Linux)
- Timestamped keystroke logging
- Simple implementation for educational understanding
- Easy termination via ESC key

## Requirements

- Python 3.6+
- pynput library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Xieonie/educational-keylogger.git
   cd educational-keylogger
   ```

2. Install required dependencies:
   ```
   pip install pynput
   ```

## Usage

1. Run the keylogger:
   ```
   python keylogger.py
   ```

2. The keylogger will start running and create a log file:
   - On Windows: In your temp directory (`%TEMP%\keylog.txt`)
   - On Linux: In your home directory (`~/.keylog.txt`)

3. Press the ESC key to stop the keylogger.

## Step-by-Step Implementation Guide

1. **Setting up the environment**
   - Install Python 3.6 or newer
   - Install the pynput library using pip

2. **Understanding the keylogger components**
   - The keylogger uses pynput to monitor keyboard inputs
   - We use platform detection to handle OS-specific functionality
   - Key presses are logged with timestamps to a text file

3. **Code structure breakdown**
   - Platform detection determines the operating system
   - Log file location is set based on the detected OS
   - Keyboard listeners are configured to detect key press and release events
   - The on_press function logs each keystroke with a timestamp
   - The on_release function checks for the ESC key to stop the keylogger

4. **Running the keylogger**
   - Execute the script to start monitoring
   - All keystrokes are logged until ESC is pressed
   - Review the log file to see the captured keystrokes

5. **Extending the project**
   - Consider adding encryption for the log file
   - Implement more sophisticated logging mechanisms 
   - Add network capabilities to transmit logs (for educational purposes only)
   - Improve stealth by developing a background service

## Ethical Considerations

When including this project in your portfolio:

1. Always emphasize the educational purpose
2. Discuss the ethics of monitoring tools
3. Highlight the importance of consent and legal compliance
4. Demonstrate defensive measures against such tools

## License

This project is provided for educational purposes under the MIT License.

## Author

Xieonie 

## Acknowledgments

- The pynput library developers
- Cybersecurity community for educational resources