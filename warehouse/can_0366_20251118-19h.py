"""
Campbell's Soup Can #366
Produced: 2025-11-18 19:26:26
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import os
import time
import sys

# ANSI color codes
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

# Clear screen and hide cursor
print("\033c\033[?25l", end="")

try:
    # Get terminal size
    columns = os.get_terminal_size().columns
except:
    columns = 80

# ASCII art
art = rf"""
{YELLOW}       _,._ {RED}{' (behind existential dread)' if columns > 80 else ''}
{YELLOW}  .||/ \||.      {GREEN}?
{YELLOW}  ||\ /||        {GREEN}|
{YELLOW}  ||   ||   \O/  {GREEN}O
{YELLOW}  |\,./ |    |   {GREEN}|{RESET}
"""

def center_text(text, color=RESET):
    padding = (columns - len(text.strip())) // 2
    print(" " * padding + color + text + RESET)

# Typewriter effect with colors
def animate_line(text, color=RESET, delay=0.04):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Generate output with visual flair
time.sleep(0.5)
center_text(art.replace('\n', '\n'))

title = "~ WOODY ALLEN'S EXISTENTIAL QUESTION ~"
quote = [
    "\"The universe is expanding at an alarming rate, which I would find",
    "upsetting if I weren't already drowning in this metaphorical bowl",
    "of cosmic chicken soup that tastes suspiciously of despair and",
    "unsold screenplay drafts.\""
]

time.sleep(1)
center_text('▛' + '▀'* (len(title)+2) + '▜', RED)
center_text(f'▌ {YELLOW}{title}{RED} ▌', RED)
center_text('▙' + '▄'* (len(title)+2) + '▟', RED)
print()

time.sleep(0.8)
for line in quote:
    center_text(line, CYAN)
    time.sleep(0.3)

time.sleep(1)
center_text(f"{GREEN}    – from '{DIM}My Therapy Bills: Vol. XVII{MAGENTA}{BOLD}'", MAGENTA+BOLD)

# Reset and show cursor
print("\n" + RESET + "\033[?25h")