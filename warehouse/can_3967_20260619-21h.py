"""
Campbell's Soup Can #3967
Produced: 2026-06-19 21:34:50
Worker: Google: Gemma 4 31B (free) (google/gemma-4-31b-it:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def typewriter_effect(text, delay=0.05, color="\033[0m"):
    """Prints text character by character for dramatic effect."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")

def main():
    # ANSI Colors
    GOLD = "\033[33m"
    CYAN = "\033[36m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    RED = "\033[31m"

    # The Quote
    quote = "I've decided that the only way to deal with the crushing weight of existential dread is to treat it like a mild case of indigestion: ignore it until it goes away, or until I find a very expensive piece of cake."
    
    # ASCII Decoration
    border_top = " ╔══════════════════════════════════════════════════════════════════════════════════════════╗ "
    border_bot = " ╚══════════════════════════════════════════════════════════════════════════════════════════╝ "
    
    # A little "neurotic" animation before the quote
    loading_msgs = [
        "Analyzing the futility of existence...",
        "Adjusting glasses...",
        "Panic attack in 3... 2... 1...",
        "Searching for a psychiatrist who accepts insurance...",
        "Questioning the meaning of this Python script..."
    ]

    print("\n" * 2)
    
    # Intro Animation
    for msg in loading_msgs:
        sys.stdout.write(f"\r{CYAN}{msg}{RESET}")
        sys.stdout.flush()
        time.sleep(0.6)
        # Add some random "glitch" effect
        sys.stdout.write(f"\r{RED}{msg} (Wait, is this working?){RESET}")
        sys.stdout.flush()
        time.sleep(0.4)

    print("\n\n")

    # The Final Reveal
    print(f"{GOLD}{BOLD}{border_top}{RESET}")
    
    # Split quote into a few lines to fit the box
    words = quote.split()
    line = ""
    for word in words:
        if len(line) + len(word) < 70:
            line += word + " "
        else:
            print(f" {GOLD}│{RESET} {BOLD}{line.strip():<68} {GOLD}│{RESET}")
            line = word + " "
    print(f" {GOLD}│{RESET} {BOLD}{line.strip():<68} {GOLD}│{RESET}")
    
    print(f"{GOLD}{BOLD}{border_bot}{RESET}")
    
    # Sign-off
    time.sleep(0.5)
    typewriter_effect("\n— Woody-ish", delay=0.1, color=CYAN)
    
    print("\n" * 2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}Even my interruptions are existential!{RESET}")