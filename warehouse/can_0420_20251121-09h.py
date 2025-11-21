"""
Campbell's Soup Can #420
Produced: 2025-11-21 09:33:21
Worker: xAI: Grok 4.1 Fast (x-ai/grok-4.1-fast)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random

# ANSI color codes
RESET = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BG_BLACK = '\033[40m'
BG_BLUE = '\033[44m'

colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]

def clear_screen():
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def typewriter_print(text, delay=0.05, color_cycle=True):
    for i, char in enumerate(text):
        if color_cycle and char.isalpha():
            color = random.choice(colors)
            sys.stdout.write(color + char + RESET)
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_spinning_loader(message, duration=2):
    chars = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in chars:
            sys.stdout.write(f'\r{BOLD}{CYAN}{message} {char}{RESET}')
            sys.stdout.flush()
            time.sleep(0.1)

# Main program
clear_screen()

# Neurotic intro animation
print_spinning_loader("Summoning Woody's Neurotic Wisdom...", 3)
clear_screen()

# ASCII Art Woody-esque head (glasses, anxious expression)
head = f"""
{BOLD}{YELLOW}
     .-""""""-.
   .'          '.
  /   {ITALIC}O      O{RESET}{YELLOW}   \\
 :           `    :
 |                |
 :    .------.    :
  \\  '        '  /
   '.          .'
     '-......-'
{RESET}
"""

print(head)
time.sleep(0.5)

# The quote
quote = "Existence precedes essence, Sartre said. But for me, it's neuroses that precede breakfast—every damn morning."

print(f"{BOLD}{MAGENTA}Woody's Wisdom:{RESET}\n")

# Boxed quote with typewriter effect and color highlights
border_color = CYAN
quote_color = WHITE

top_border = f"{BOLD}{border_color}╔{'═' * 62}╗{RESET}"
side = f"{BOLD}{border_color}║{RESET}"
bottom_border = f"{BOLD}{border_color}╚{'═' * 62}╝{RESET}"

print(top_border)
print(f"{side} {BOLD}{BLUE}'{RESET} {quote_color}", end='')
typewriter_print(f"'{RESET}{BOLD}{border_color}", color_cycle=False)
print(f"{side}{' ' * 62}{BOLD}{border_color}║{RESET}")
print(bottom_border)

time.sleep(2)

# Fade out effect (neurotic existential void)
print(f"\n{ITALIC}{MAGENTA}...and poof, back to the void.{RESET}")
for _ in range(10):
    print('\r' + ' ' * 80, end='', flush=True)
    time.sleep(0.2)
clear_screen()

# Final static colorful quote for posterity
print(f"{BOLD}{GREEN}{head}{RESET}")
print(f"{BOLD}{MAGENTA}“{quote}”{RESET}")
print(f"\n{ITALIC}{YELLOW}- A neurotic philosopher{RESET}")