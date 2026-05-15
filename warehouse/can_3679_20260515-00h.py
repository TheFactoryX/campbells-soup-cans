"""
Campbell's Soup Can #3679
Produced: 2026-05-15 00:10:01
Worker: Poolside: Laguna XS.2 (free) (poolside/laguna-xs.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Philosophical Quote Generator
Because existential dread tastes better with a side of self-deprecation.
"""

import time
import sys

# ANSI Color Codes
RESET = '\033[0m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'

def typewriter_effect(text, delay=0.03, color=""):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_box(text, border_color=CYAN, text_color=YELLOW):
    """Print text inside a decorative box"""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    
    print(border_color + "┌" + "─" * (max_len + 2) + "┐" + RESET)
    for line in lines:
        print(border_color + "│" + RESET + text_color + " " + line.ljust(max_len) + " " + border_color + "│" + RESET)
    print(border_color + "└" + "─" * (max_len + 2) + "┘" + RESET)

def main():
    # Clear screen (works on most terminals)
    print('\033[2J\033[H', end='')
    
    # ASCII Art Header
    print(CYAN + """
    ╔════════════════════════════════════════╗
    ║     🤔 PHILOSOPHICAL QUOTE GENERATOR 🤔  ║
    ║         (Woody Allen Style)            ║
    ╚════════════════════════════════════════╝
    """ + RESET)
    
    time.sleep(0.5)
    
    # Philosophical quote in Woody Allen's style
    quote = """I'm not afraid of the dark; I'm afraid of the\nabsence of light. But honestly,\nI'm too lazy to turn on the lamp,\nso I'll just sit here in the dark\nwith my existential crisis\nand contemplate whether\nthe universe cares enough\nabout me to notice I'm here."""

    print(MAGENTA + "┌─ Woody Allen Approved Philosophy ─┐" + RESET)
    print(BOLD + quote + RESET)
    print(MAGENTA + "└───────────────────────────────────┘" + RESET)
    
    print()
    time.sleep(0.3)
    
    # Author attribution with style
    print(CYAN + "        ~ A neurotic contemplation ~" + RESET)
    print(YELLOW + "           (Probably not wise)" + RESET)
    
    print()
    time.sleep(0.5)
    
    # Additional philosophical commentary
    print(GREEN + "💡 Moral of the story: Always keep a nightlight," + RESET)
    print(RED + "   and maybe a therapist on speed dial." + RESET)
    
    print()
    print(BOLD + BLUE + "✨ Now go forth and question everything... or just watch Netflix. ✨" + RESET)

if __name__ == "__main__":
    main()