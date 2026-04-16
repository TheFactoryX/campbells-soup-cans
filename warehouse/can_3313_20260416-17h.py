"""
Campbell's Soup Can #3313
Produced: 2026-04-16 17:44:02
Worker: Amazon: Nova Micro 1.0 (amazon/nova-micro-v1)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

def print_colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def slow_typewriter(text, speed=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()

def centered_box(text):
    text_length = len(text)
    box_length = text_length + 4
    print("┃" + " " * (box_length - 2) + "┃")
    print("┃ " + text + " ┃")
    print("┃" + " " * (box_length - 2) + "┃")

# Woody Allen style quote
quote = (
    "Philosophy is a lot like reading the ",
    "instructions for a TV set. You're not ",
    "actually supposed to follow them - you're ",
    "just happy they're there."
)

# Animated quote display
os.system("clear||cls")  # Clear screen for cross-platform compatibility
print(print_colored_text("Welcome to WoodySpeak!", "34;1"))  # Bold blue
print("\nA bit of existential joy from Woody Allen...\n")
time.sleep(2)

for line in quote:
    slow_typewriter(line, speed=0.05)
    time.sleep(1)

centered_box(
    print_colored_text(
        "Remember, it's not the journey:",
        "32;1"  # Bold green
    )
)
time.sleep(1)
centered_box(
    print_colored_text(
        "it's the arrivals that suck.",
        "31;1"  # Bold red
    )
)

print("\n" + "┃" + " " * 19 + "┃")
print("┃ " + print_colored_text("- Woody Allen", "35;1") + " ┃")  # Bold magenta
print("┃" + " " * 19 + "┃")