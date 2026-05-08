"""
Campbell's Soup Can #3602
Produced: 2026-05-08 06:09:43
Worker: Baidu: Qianfan-OCR-Fast (free) (baidu/qianfan-ocr-fast:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

# Create ANSI color red
RED = "\033[91m"
RESET = "\033[0m"

# Clear screen function (cross platform)
def clear_screen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

# Print with red color
def print_red(text):
    print(RED + text + RESET)

# Animated quote function
def print_phrase(text, interval=0.2):
    for char in text:
        print_red(char, end='', flush=True)
        time.sleep(interval)
    print("\n")

# Display quote with ASCII art
def display_quote():
    clear_screen()
    print("\033[107;37m", end='')  # Dark gray background
    
    frames = [
        r"___          ___  ___  ___  ___",
        r"\                  \    |    |   ",
        r"\                 \  \  |  |   ",
        r" \_ __           \_  \_  _  \  ",
        r"  \_ \ \___  ___    \_  \ \ \ \ ",
        r"  /_/ \_  )/  /     /_   \_\_/\_",
        r"  | | \     ||_     \_    |\___ |\ ",
        r"  \_||_\_    |_|\_    /  /-'\_ _/\_",
        "",
        r"\_                  /",
        "/   Discover the",
        "\   profound",
        " \  revealment",
        " *"
    ]

    y_offset = 0
    delay = 0.3
    
    for row in frames:
        for i in range(8):
            w = len(row) + i
            for x in range(w):
                print(" " * x + row[(len(row) + i - w)] + " " * (x + 1), end='')
        print()
        
        # Add delay between frames
        time.sleep(delay)
        
        # Move up/down lines with ASCII art
        if y_offset < 7:
            y_offset += 0.1 if time.time() % 0.2 < 0.1 else 0
        else:
            y_offset -= 0.1 if time.time() % 0.2 < 0.1 else 0
            
        # Column animation
        print("-" * w)

        print()
        time.sleep(delay * 0.7)
        y_offset += 1 if time.time() % 0.2 < 0.1 else -1
        if y_offset >= len(frames): y_offset = 0

    print("Welcome to the existential party...", end='')
    for _ in range(35):
        print("-", end='', flush=True)
        time.sleep(0.1)
    print("\n\n")
    
    clear_screen()
    print_phrase(
        "The only thing we have to fear is the effects that our own thoughts are having on us. In other words, what we think we are, we are; the rest is just an annoying illusion—the effects of our own thought on us. Life is full of chains, Woody, but chaos is even worse—even if you buy yourself freedom, you never get to truly choose your fate. "
    )

# Run the philosophical dance
def main():
    print_phrase("Initializing existential intergalactic travel...", end='')
    for i in range(35):
        print(".", end='', flush=True)
        time.sleep(0.1)
    print("\n")
    
    display_quote()
    
    print("\033[107;30m", end='')  # Black on white
    print("""
                              ___    _ 
        ____ ___  ___  ____ __/ |__ | (_)
      / ___/ _ \\/ __ |/ ___/ _  / / / 
     | |  / _, \\\__ \\\__ \N9 1/ /__ (__ 
     |___/_/ \_\\___/|___/____/_______|
    
""")
    
    print("Party over!")

# Run the program
if __name__ == "__main__":
    main()