"""
Campbell's Soup Can #197
Produced: 2025-11-11 04:39:02
Worker: Qwen: Qwen3 14B (free) (qwen/qwen3-14b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# ASCII banner
banner = """
\033[1;32m   _____ _     _        _   _ _   \n  / ____| |   | |      | | | | |  \n | |    | |   | |      | | | | |  \n | |    | |___| |______| |_| | |__\n  \_____|______|______|_____|_____|\n\033[0m
"""

# Introduce the quote
intro = "\033[1;33m[Woody Allen's Philosophical Gem] \033[0m\n"

# The actual quote
quote_text = "I fear death, but I'm afraid of life too because it's so much more expensive."

# Build the box around the quote
border = "+" + "-" * 60 + "+\n"
middle_line = "| " + quote_text.ljust(58) + " |\n"
boxed = "\033[1;32m" + border + "\033[1;34m" + middle_line + "\033[1;32m" + border + "\033[0m"

# Author line with blinking effect
author = "\n\033[5;31m- Woody Allen\033[0m"

# Typing anim: banner
type_text(banner, 0.02)

# Typing anim: intro
type_text(intro, 0.02)

# Typing anim: box
type_text(boxed, 0.01)

# Typing anim: author
type_text(author, 0.03)