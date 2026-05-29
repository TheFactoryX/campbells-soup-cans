"""
Campbell's Soup Can #3810
Produced: 2026-05-29 08:51:40
Worker: Owl Alpha (openrouter/owl-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI color codes
class Color:
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'
    ITALIC = '\033[3m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewrite(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_line(char='─', length=70, color=Color.CYAN):
    print(color + char * length + Color.RESET)

def wait(seconds=0.5):
    time.sleep(seconds)

quote = (
    '"I don\'t believe in an afterlife, although\n'
    ' I am bringing a change of underwear."\n'
    '                          — Woody Allen'
)

title = "WOODY ALLEN"
subtitle = "~ In His Own Words ~"

box_top = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                          ║"""

box_bottom = """║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════════╝"""

# Start animation
clear_screen()

# Fade-in effect
fade_steps = [Color.DIM, Color.WHITE, Color.WHITE]
for step_color in fade_steps:
    print(step_color + "\n\n")
    typewrite("                                      " + title, 0.07)
    wait(0.3)
    clear_screen()

wait(0.2)
print("\n\n")

# Flash effect to reveal title
for i in range(2):
    if i % 2 == 0:
        typewrite(Color.BOLD + Color.YELLOW + "                                      " + title, 0.06)
        wait(0.15)
    else:
        print("\033[2J\033[H")  # Clear screen quickly
        wait(0.1)

clear_screen()
print("\n\n")

# Final formatted display
print(Color.BOLD + Color.YELLOW + "                                  " + title + Color.RESET)
print(Color.CYAN + "                             " + subtitle + Color.RESET)
print()

# Animated line reveal
draw_line('═', 70, Color.YELLOW)
wait(0.3)

# Quote with animated reveal
lines = quote.split('\n')
for line in lines:
    time.sleep(0.05)
    print(Color.WHITE + Color.ITALIC + "  " + line + Color.RESET)

wait(0.3)
draw_line('═', 70, Color.YELLOW)

wait(0.5)

# Bonus micro-animation: existential dots
wait(0.2)
print()
print(Color.DIM + "  [Existential dread loading", end="")
for i in range(3):
    wait(0.3)
    print(".", end="", flush=True)
print(" complete]" + Color.RESET)

wait(0.3)

# Final flourish
print()
print(Color.CYAN + Color.BOLD)
flourish_text = "         ☽  " + "•" * 3 + " WOODY ALLEN " + "•" * 3 + "  ☾"
print(flourish_text)
print(Color.RESET)

print()
print(Color.DIM + "                 \"The universe is not indifferent to your suffering.\"" + Color.RESET)
print(Color.DIM + "                                   — Also Woody Allen" + Color.RESET)
print()

# Bottom border
draw_line('─', 70, Color.CYAN)

wait(0.2)
print()
print(Color.BOLD + Color.YELLOW + "                          ★ FIN ★" + Color.RESET)
print()

# Fading out effect
for color in [Color.DIM, '\033[37;2m', '\033[30;2m']:
    print(color + "              (mind still racing about mortality...)" + Color.RESET)
    wait(0.15)
print()