"""
Campbell's Soup Can #5081
Produced: 2026-10-08 16:29:05
Worker: Apodex: Apodex 1.1 Mini (free) (apodex/apodex-1.1-mini:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Woody Allen Style Philosophical Generator
Pure Python, no external dependencies, ANSI escape codes for color.
Prints ONE neurotic, existential quote with animated ASCII art.
"""
import os
import sys
import time
import random
import ctypes

# --- ANSI Color Codes ---
RESET   = "\033[0m"
BOLD    = "\033[1m"
UNDER   = "\033[4m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
RED     = "\033[31m"
YELLOW  = "\033[33m"
WHITE   = "\033[37m"
GREEN   = "\033[32m"
BLUE    = "\033[34m"
RAINBOW = [RED, YELLOW, GREEN, CYAN, MAGENTA, RED]

# --- Windows ANSI Support (Enable Virtual Terminal Processing) ---
if os.name == 'nt':
    try:
        windll = ctypes.windll.kernel32
        windll.SetConsoleMode(windll.GetStdHandle(-11), 7)  # 7 = ENABLE | ENABLE_WRAP
    except Exception:
        pass

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_slow(text, delay=0.04, color=WHITE):
    """Prints text one character at a time (typewriter effect)."""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def rainbow_text(text, delay=0.03):
    """Prints text in a shifting rainbow pattern."""
    cols = RAINBOW
    for i, char in enumerate(text):
        sys.stdout.write(cols[i % len(cols)] + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def disable_wrap():
    """Attempts to disable line wrapping for smoother animations."""
    try:
        sys.stdout.write("\033[?7l")
        sys.stdout.flush()
    except Exception:
        pass

def shake_quote(text, times=6):
    """Jitters the quote horizontally for emphasis."""
    try:
        sys.stdout.write("\r")  # Reset to start of current line
        for i in range(times):
            offset = random.randint(1, 4)
            sys.stdout.write("\033[%dG" % offset)
            sys.stdout.write(RED + BOLD + text + RESET)
            sys.stdout.flush()
            time.sleep(0.05)
        sys.stdout.write("\r\033[0G" + RESET + "\n")
        sys.stdout.flush()
    except Exception:
        print("\n" + RED + text + RESET)

def main():
    clear_screen()
    time.sleep(0.3)
    
    # --- ASCII Art: The Existential Head (Typewriter Style) ---
    art = [
        "         . - ~ ~ ~ - .         ",
        "      .  *  ( 0 )  *  .      ",
        "     '   *  (_____)  *   '    ",
        "        .  ~ ~ ~ ~  .         ",
        "     (  _  )  (  _  )         ",
        "    (__) (__) (__) (__)       ",
    ]
    for line in art:
        type_slow(line, delay=0.06, color=CYAN)
        time.sleep(0.1)
    
    print(" " * 10)
    type_slow("THE WOODY ALLEN PHILOSOPHY", delay=0.1, color=WHITE)
    print("-" * 40)
    time.sleep(0.5)
    
    # --- The ONE Quote ---
    quote = "The universe is a cold, indifferent void... " \
            "but at least the void doesn't have to worry about paying alimony. " \
            "That's the real existential dread."
    
    print(" " * 5)
    disable_wrap()
    rainbow_text(quote, delay=0.05)
    print(" " * 5)
    time.sleep(0.5)
    
    # --- Neurotic Internal Monologue ---
    print(BOLD + "INTERNAL MONOLOGUE:" + RESET)
    print(" " * 5)
    type_slow("You're alone in the universe...", delay=0.06, color=MAGENTA)
    type_slow("And nobody is paying you...", delay=0.06, color=MAGENTA)
    type_slow("So stop worrying about it.", delay=0.06, color=MAGENTA)
    print(" " * 5)
    
    # --- Final Shake Effect ---
    print(BOLD + "FINAL VERDICT:" + RESET)
    print(" " * 5)
    shake_quote(quote, times=7)
    print(" " * 5)
    time.sleep(1)
    
    clear_screen()
    print(RESET + "The end... or maybe just the intermission." + RESET)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print(RESET)
        sys.exit(0)