"""
Campbell's Soup Can #1954
Produced: 2026-01-30 23:40:52
Worker: Qwen: Qwen2.5 7B Instruct (qwen/qwen-2.5-7b-instruct)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# ANSI escape codes for colors
COLORS = ['\033[91m', '\033[93m', '\033[94m', '\033[92m']

# ASCII art for Woody Allen
Woody_Arnold = """
      _                _
     (_)               (_)
  __ _ ___   _ __   ___ _ ___
 / _` / __| | '_ \ / _ \ / __|
| (_| \__ \ | |_) |  __/ \__ \
 \__,_|___/_| .__/ \___|_|___/
           | |
           |_|
"""

# Function to print with color
def print_colored(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.005)  # Adjust speed here
    print()

# Function to print with colored box and Woody Allen ASCII art
def print_with_box_and_ascii_art():
    text_color = random.choice(COLORS)
    quote_style = random.randint(1, 3)
    
    if quote_style == 1:
        quote = "I've never understood people who talk about the meaning of life. Don't they realize it's a load of shit?"
    elif quote_style == 2:
        quote = "If you're not Jewish, why is everyone at your 80th birthday party Jewish?"
    elif quote_style == 3:
        quote = "I never think of the future. It comes soon enough."
    
    print("\033[1m\033[4m" + "\033[96m" + "_" * 40 + "\033[0m")
    print("\033[1m", end='')
    print_colored(Woody_Arnold)
    print("\033[0m", end='')
    print("\n\n\033[1m\033[4m" + "\033[96m" + "_" * 40 + "\033[0m")
    print("\033[3m" + f"{text_color}{quote}\033[0m", flush=True)

print_with_box_and_ascii_art()
time.sleep(3)  # Delay before clearing the screen
print("\033[H\033[J")  # Clear the screen