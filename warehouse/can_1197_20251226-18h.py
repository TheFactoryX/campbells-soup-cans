"""
Campbell's Soup Can #1197
Produced: 2025-12-26 18:45:09
Worker: Kwaipilot: KAT-Coder-Pro V1 (free) (kwaipilot/kat-coder-pro:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen's Existential Crisis Generator
A single file of neurotic humor in a box
"""

import time
import sys
import random

# ANSI color codes - the neurotic palette
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
DARK_GRAY = "\033[90m"

# Background colors for extra existential dread
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"
BG_BLACK = "\033[40m"

def type_writer(text, delay=0.03):
    """Simulate Woody typing with existential dread"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_anxious_heart():
    """Draw a heart with anxiety lines"""
    heart = [
        "    {}❤{}    ".format(RED, RESET),
        "   {}<3 {}   ".format(RED, RESET),
        "  {}<3  {}  ".format(RED, RESET),
        " {}<3   {} ".format(RED, RESET),
        "{}<3    {}{}".format(RED, RESET, DARK_GRAY),
        "{}<3   {} {}".format(RED, RESET, DARK_GRAY),
        " {}<3  {}  {}".format(RED, RESET, DARK_GRAY),
        "  {}<3 {}   {}".format(RED, RESET, DARK_GRAY),
        "   {}<3{}    {}".format(RED, RESET, DARK_GRAY),
        "    {}<3{}    {}".format(RED, RESET, DARK_GRAY)
    ]
    
    # Add shaky lines around the heart
    for i, line in enumerate(heart):
        if i < len(heart) - 2:
            line += "  " + "~" * (i + 1) if i % 2 == 0 else "  " + "—" * (i + 1)
        print(line)
        time.sleep(0.1)

def draw_nervous_eye():
    """Draw a big, nervous eye"""
    eye_art = [
        "    " + " " * 10 + WHITE + "👁" + RESET + "     " + " " * 10,
        "   " + " " * 9 + WHITE + "/   \\" + RESET + "    " + " " * 9,
        "  " + " " * 8 + WHITE + "|  •  |" + RESET + "   " + " " * 8,
        " " + " " * 7 + WHITE + "\\ ___ /" + RESET + "    " + " " * 7,
        "  " + " " * 8 + MAGENTA + "•••••" + RESET + "     " + " " * 8,
        "   " + " " * 9 + MAGENTA + "••••" + RESET + "      " + " " * 9,
        "    " + " " * 10 + MAGENTA + "•••" + RESET + "       " + " " * 10,
        "     " + " " * 11 + MAGENTA + "••" + RESET + "        " + " " * 11,
        "      " + " " * 12 + MAGENTA + "•" + RESET + "         " + " " * 12
    ]
    
    for line in eye_art:
        print(line)
        time.sleep(0.05)

def print_woody_quote():
    """Print a neurotic philosophical quote in Woody Allen's style"""
    
    # Clear screen with style
    print("\033[2J\033[H", end="")
    
    # Title sequence with shaky text
    title = "WOODY ALLEN'S EXISTENTIAL CRISIS GENERATOR"
    print("\n" + " " * 5 + BOLD + YELLOW + "=" * 50 + RESET)
    print(" " * 10 + BOLD + RED + title + RESET)
    print(" " * 5 + BOLD + YELLOW + "=" * 50 + RESET + "\n")
    
    # Draw the anxious visual
    print(" " * 20 + ITALIC + "Behold, the visual metaphor:" + RESET)
    print()
    draw_anxious_heart()
    print()
    
    # The moment of truth
    print(" " * 15 + BOLD + BLUE + "AND NOW..." + RESET)
    time.sleep(1)
    
    # Quote reveal with typewriter effect
    print("\n" + " " * 10 + BOLD + WHITE + "THE QUOTE:" + RESET + "\n")
    
    # Our Woody Allen-style quote
    quote = "I don't mind dying, I just don't want to be there when it happens. And honestly, I'd prefer it happened while I was at the dentist - at least then I'd have a legitimate excuse to be in that much pain."
    
    # Print quote with dramatic pauses
    type_writer(" " * 5 + ITALIC + quote + RESET, 0.04)
    
    # Signature
    time.sleep(1)
    type_writer("\n" + " " * 20 + BOLD + MAGENTA + "~ Woody, probably" + RESET)
    
    # Eye follows you
    time.sleep(1.5)
    print("\n" + " " * 15 + BOLD + CYAN + "THE EYE SEES ALL:" + RESET)
    draw_nervous_eye()
    
    # Final existential tagline
    time.sleep(1)
    print("\n" + " " * 10 + BOLD + RED + "Life: It's not the end that scares me..." + RESET)
    time.sleep(0.8)
    print(" " * 10 + BOLD + RED + "...it's the awkward small talk on the way there." + RESET)
    
    # Blinking cursor of doom
    print("\n" + " " * 30 + WHITE + "█" + RESET, end="")
    for _ in range(3):
        time.sleep(0.5)
        print("\b ", end="", flush=True)
        time.sleep(0.5)
        print("\b█", end="", flush=True)
    print("\b" + " " * 30 + BOLD + DARK_GRAY + "cursor of existential dread" + RESET)

if __name__ == "__main__":
    print_woody_quote()