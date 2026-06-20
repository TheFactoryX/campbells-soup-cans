"""
Campbell's Soup Can #3971
Produced: 2026-06-20 10:13:17
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time

# ANSI color codes for a playful terminal display
GREEN  = '\033[92m'   # bright green
YELLOW = '\033[93m'   # bright yellow
BOLD   = '\033[1m'    # bold text
ITALIC = '\033[3m'    # italic text (supported by many terminals)
RESET  = '\033[0m'    # reset all formatting

# A classic Woody Allen‑style philosophical quote
quote = "I'm not afraid of death; I'm just worried I might not have enough salsa for the cosmic fajita."

# Build a simple ASCII box around the quote
padding = 4
box_width = len(quote) + padding

# Top and bottom borders
top_bottom = YELLOW + '+' + '-' * box_width + '+' + RESET

# The middle line containing the quote, colored and bold
middle_line = (YELLOW + '|' + RESET +
               ' ' +
               GREEN + BOLD + quote + RESET +
               ' ' +
               YELLOW + '|' + RESET)

# A tiny "Woody head" ASCII art for flavor (italic and green)
woody_head = f"""
{ITALIC}{GREEN}   (   _._   ){RESET}
{ITALIC}{GREEN}  (  -_-  ){RESET}
{ITALIC}{GREEN} (  o o  ){RESET}
   {YELLOW}---oOO0-(_)-0OOo---
"""

# Print everything with short pauses to create a gentle "reveal" effect
print()                         # leading blank line
print(woody_head)               # whimsical header
time.sleep(0.5)                 # pause for drama

print(top_bottom)               # top border
time.sleep(0.3)                 # pause

print(middle_line)              # quote line
time.sleep(0.3)                 # pause

print(top_bottom)               # bottom border
print()                         # final blank line (clean exit)