"""
Campbell's Soup Can #3300
Produced: 2026-04-15 17:19:04
Worker: Anthropic: Claude Opus 4 (anthropic/claude-opus-4)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

# ANSI color codes
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'

# Clear screen
print('\033[2J\033[H')

# ASCII art glasses
glasses = f"""
{CYAN}     ___________     ___________
    /           \\___/           \\
   |    {WHITE}O   O{CYAN}    |    {WHITE}O   O{CYAN}    |
   |             |             |
    \\___________/ \\___________/{RESET}
"""

# Typewriter effect function
def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Print glasses with wobble animation
for i in range(3):
    print('\033[2J\033[H')
    print(' ' * (i % 2) + glasses)
    time.sleep(0.2)

# Print "WOODY ALLEN says..." with style
print(f"\n{YELLOW}{BOLD}{'=' * 50}{RESET}")
typewriter(f"{MAGENTA}{BOLD}   WOODY ALLEN says...{RESET}", 0.08)
print(f"{YELLOW}{BOLD}{'=' * 50}{RESET}\n")

# The philosophical quote
quote = "My therapist says I have a preoccupation with death, which is ridiculous — I haven't thought about it since breakfast when I realized my cereal expires before I do."

# Build the quote box
quote_lines = []
words = quote.split()
current_line = ""
for word in words:
    if len(current_line + word) > 40:
        quote_lines.append(current_line.strip())
        current_line = word + " "
    else:
        current_line += word + " "
quote_lines.append(current_line.strip())

# Animated quote appearance
max_width = max(len(line) for line in quote_lines)
print(f"{BLUE}╔{'═' * (max_width + 4)}╗{RESET}")

for i, line in enumerate(quote_lines):
    # Random neurotic color for each line
    colors = [RED, GREEN, YELLOW, CYAN, MAGENTA]
    color = random.choice(colors)
    
    # Add some jitter to simulate neurotic energy
    jitter = ' ' * random.randint(0, 2)
    
    print(f"{BLUE}║{RESET} {jitter}{color}{line.ljust(max_width)}{RESET} {BLUE}║{RESET}")
    time.sleep(0.3)

print(f"{BLUE}╚{'═' * (max_width + 4)}╝{RESET}")

# Existential ending
print(f"\n{DIM}*nervously adjusts glasses*{RESET}")
time.sleep(1)

# Final flourish with blinking question
for _ in range(3):
    print(f"\r{WHITE}{'But who's counting?':^50}{RESET}", end='')
    time.sleep(0.5)
    print(f"\r{DIM}{'But who's counting?':^50}{RESET}", end='')
    time.sleep(0.5)

print("\n")