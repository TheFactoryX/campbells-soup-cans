"""
Campbell's Soup Can #5272
Produced: 2026-11-24 00:51:14
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Style Philosophical Quote Printer
A neurotic, existential, and self-deprecating quote in a fancy box.
"""

import textwrap
import os
import time

# Clear screen for better visual effect
os.system('cls' if os.name == 'nt' else 'clear')

# The quote in classic Woody Allen style
quote = "I'm not afraid of death; I just don't want to be there when it happens. Then again, what if I'm already there and just too anxious to notice?"

# Colors using ANSI escape codes
RESET = '\033[0m'
BOLD = '\033[1m'
RED = '\033[31m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
CYAN = '\033[36m'
WHITE = '\033[37m'
BG_BLUE = '\033[44m'
BG_YELLOW = '\033[43m'

# Print a dramatic intro
print(f"{CYAN}{BOLD}")
print("╔══════════════════════════════════════════════════════════════╗")
print("║               WOODY ALLEN'S NEUROTIC WISDOM                ║")
print("╚══════════════════════════════════════════════════════════════╝")
print(RESET)
time.sleep(1)

# Typing effect for the intro
intro = f"\n{YELLOW}{BOLD}A philosophical musing from the master of existential dread...{RESET}\n"
for char in intro:
    print(char, end='', flush=True)
    time.sleep(0.03)

time.sleep(0.5)

# Create a fancy box for the quote
width = 70
inner_width = width - 6  # Account for padding and borders

# Wrap the quote to fit the box
wrapped_lines = textwrap.wrap(quote, inner_width)

# Calculate center padding for each line
max_line_len = max(len(line) for line in wrapped_lines)
padding = (inner_width - max_line_len) // 2

# Print the quote box
print(f"\n{BLUE}{BOLD}╔{'═' * (width - 2)}╗{RESET}")

# Top empty line
print(f"{BLUE}{BOLD}║{' ' * (width - 2)}║{RESET}")

# Quote lines with background color
for line in wrapped_lines:
    centered_line = ' ' * padding + line + ' ' * (inner_width - len(line) - padding)
    print(f"{BLUE}{BOLD}║ {BG_YELLOW}{WHITE}{BOLD}{centered_line}{RESET} {BLUE}{BOLD}║{RESET}")

# Bottom empty line
print(f"{BLUE}{BOLD}║{' ' * (width - 2)}║{RESET}")

# Bottom border
print(f"{BLUE}{BOLD}╚{'═' * (width - 2)}╝{RESET}")

# Add some neurotic footnotes
footnotes = [
    f"\n{RED}P.S. I probably said something wrong. It's what I do.",
    f"{RED}P.P.S. This quote is likely misattributed. Like everything else in my life.",
    f"{RED}P.P.P.S. If you're still reading, you might need therapy too."
]

for note in footnotes:
    for char in note:
        print(char, end='', flush=True)
        time.sleep(0.02)
    time.sleep(0.3)

print(f"\n\n{CYAN}{BOLD}*Dramatic pause for existential contemplation*{RESET}")
time.sleep(1)
print(f"{YELLOW}Thanks for sharing my existential crisis!{RESET}")