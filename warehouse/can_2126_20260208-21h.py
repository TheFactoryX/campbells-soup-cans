"""
Campbell's Soup Can #2126
Produced: 2026-02-08 21:42:58
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, random, sys

# ANSI color codes
COLORS = [f"\033[3{r:1d}m" for r in range(30, 38)]
RESET = "\033[0m"

# Woody‑Allen‑styled ASCII art (self‑deprecating nervous type)
ART = r"""
   ___               ___             
  /_// \   ___ ___   /_// \   ____  
 /_ \ / \ /_ \ _ \ /_ \ / \ /__//\  
/_/ /_/\_/___//_/ /_/ /_/\_/__/ /   (© Upstage AI, 2026)
"""

def colored(txt, color_code):
    """Wrap a string in an ANSI color."""
    return f"{color_code}{txt}{RESET}"

def animate_print(text):
    """Print a quote char‑by‑char with random colors (like a nervous typing)."""
    for i in range(len(text)):
        sys.stdout.write("\r" + colored(text[:i], random.choice(COLORS)))
        sys.stdout.flush()
        time.sleep(0.04)
    # final full quote (reset color)
    sys.stdout.write("\r" + colored(text, random.choice(COLORS)))
    sys.stdout.flush()

def centered_box(msg):
    """Show the quote nicely inside a box."""
    width = len(msg) + 8
    border = "+{}+\n".format("-" * width)
    line = "| {} |\n".format(msg)
    sys.stdout.write(f"{color_code}{border}{line}{RESET}")

if __name__ == "__main__":
    # The quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens."

    # Prepare a final static color (white) for the box
    final_color = random.choice(COLORS) if random.choice([True, False]) else "\033[37m"

    # 1️⃣ Show a cute little ASCII art with a color splash
    sys.stdout.write("\033[32m{}\n\n".format(ART))
    time.sleep(1)

    # 2️⃣ Type the quote in a jittery Woody style
    animate_print(quote)

    # 3️⃣ Pause a beat before the nice final view
    time.sleep(0.5)

    # 4️⃣ Put the quote in a centered box, flashing like a nervous heart
    centered_box(quote)

    # Add a tiny existential "..." after a heartbeat
    time.sleep(0.2)
    sys.stdout.write("\033[36m...\033[0m\n")