"""
Campbell's Soup Can #3143
Produced: 2026-04-05 10:54:47
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A single-file Python script that delivers a neurotic, existential quote
in Woody Allen's signature style, wrapped in ANSI colors and a typewriter animation.
"""

import sys
import time

# ─── ANSI COLOR & STYLE CODES ────────────────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"
ITALIC = "\033[3m"
DIM    = "\033[2m"
BLACK_BG = "\033[40m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
MAGENTA = "\033[35m"
GRAY   = "\033[90m"

# ─── UTILITIES ───────────────────────────────────────────────────────
def type_print(text, delay=0.04):
    """Print characters one by one with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def thinking_dots(text, cycles=3):
    """Simulate a 'thinking/loading' animation."""
    sys.stdout.write(f"\r{DIM}{text}")
    sys.stdout.flush()
    for i in range(cycles * 4):
        dots = "." * (i % 4)
        sys.stdout.write(f"\r{DIM}{text}{dots}   ")
        sys.stdout.flush()
        time.sleep(0.35)
    # Clear the thinking line
    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()

# ─── MAIN SHOW ───────────────────────────────────────────────────────
def main():
    # Clear screen politely
    print("\033[H\033[J", end="")
    
    print("\n" * 2)
    
    # ASCII Header
    print(f"  {CYAN}╔══════════════════════════════════════════════╗{RESET}")
    print(f"  {CYAN}║{RESET}  {MAGENTA}◉{RESET} {BOLD}THE EXISTENTIAL SCREENING ROOM{RESET}  {MAGENTA}◉{RESET}  {CYAN}║{RESET}")
    print(f"  {CYAN}╚══════════════════════════════════════════════╝{RESET}\n")
    
    # Loading sequence
    thinking_dots("  Projecting cosmic truths")
    print()
    
    # Decorative separators
    print(f"  {GRAY}{'~' * 52}{RESET}")
    print()
    
    # THE QUOTE
    quote = (
        f"{YELLOW}{BOLD}\""
        f"I don’t fear the infinite indifference of the cosmos; "
        f"I fear it’s quietly judging my posture. "
        f"I wandered into this existence searching for "
        f"profound, unshakable meaning, but my neuroticism "
        f"insists on asking if the universe accepts returns "
        f"on existential purchases."
        f"\"{RESET}"
    )
    
    # Typewriter delivery
    print("  " + quote)
    
    print(f"\n  {GRAY}{'~' * 52}{RESET}")
    print()
    
    # Attribution
    attribution = (
        f"  {DIM}{ITALIC}"
        f"— A man who definitely needs a new therapist, "
        f"and possibly a standing desk.{RESET}"
    )
    type_print(attribution, 0.05)
    
    # Cinematic exit
    print()
    print(f"  {CYAN}✨ {BOLD}*fade to black, cue the slightly unresolved jazz chords*{RESET} {CYAN}✨{RESET}")
    print("\n" * 2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{RESET}{DIM}Ah, the sweet escape hatch. Very existential.{RESET}\n")
        sys.exit(0)