"""
Campbell's Soup Can #443
Produced: 2025-11-22 09:29:40
Worker: xAI: Grok 4.1 Fast (x-ai/grok-4.1-fast)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import sys
import time
import random

# ANSI color codes
class Colors:
    END = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BLACK = '\033[30m'

colors = [Colors.RED, Colors.GREEN, Colors.YELLOW, Colors.BLUE, Colors.MAGENTA, Colors.CYAN]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Clear screen
clear_screen()

# Animated intro: existential void with twinkling stars
print(Colors.CYAN + Colors.BOLD + "\n" + " " * 30 + "Staring into the void..." + Colors.END)
for _ in range(5):
    for i in range(40):
        sys.stdout.write("\r" + " " * 30 + Colors.YELLOW + "* " * (i % 5) + Colors.WHITE + "." * ((5 - i % 5) % 5) + Colors.END)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(0.2)

clear_screen()

# Woody-esque ASCII art frame top
print(Colors.MAGENTA + Colors.BOLD + """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║    .-"""-.     WOODY'S NEUROTIC EPISTLE                     ║
    ║   /  WOODY  \\                                                ║
    ║  |    ∆     |   (Don't worry, it's just existential dread)   ║
    ║   \\   -   /                                                ║
    ║    '-....-'                                                 ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
""" + Colors.END + "\n")

time.sleep(0.5)

# The ONE quote, word-by-word with random colors, typing effect
quote = "Life is full of misery, loneliness, and suffering - and it's all over much too soon. Why can't it drag on forever, like my therapy sessions?"
words = quote.split()
sys.stdout.write(Colors.WHITE + Colors.BOLD + "    \" ")
sys.stdout.flush()
for i, word in enumerate(words):
    color = random.choice(colors)
    sys.stdout.write(color + Colors.BOLD + word + Colors.END + " ")
    sys.stdout.flush()
    time.sleep(random.uniform(0.1, 0.25))
print(Colors.WHITE + Colors.BOLD + "\"")
print(Colors.END)

time.sleep(1)

# Animated closing: blinking existential question mark
print("\n" + " " * 20)
for _ in range(8):
    print("\r" + " " * 20 + Colors.RED + Colors.ITALIC + "?".center(3) + Colors.END, end="")
    sys.stdout.flush()
    time.sleep(0.4)
    print("\r" + " " * 20 + Colors.RED + Colors.ITALIC + " ".center(3) + Colors.END, end="")
    sys.stdout.flush()
    time.sleep(0.4)

# Final frame bottom
print("\n\n" + Colors.MAGENTA + Colors.BOLD + """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║         ~ Dispensed with maximum neurosis ~                  ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
""" + Colors.END)

# Hold screen
time.sleep(3)