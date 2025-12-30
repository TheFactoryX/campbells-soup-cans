"""
Campbell's Soup Can #1278
Produced: 2025-12-30 13:05:29
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time

# ANSI color codes
RED    = "\033[31m"
GREEN  = "\033[32m"
BLUE   = "\033[34m"
CYAN   = "\033[36m"
MAGENTA= "\033[35m"
YELLOW = "\033[33m"
RESET  = "\033[0m"

# Woody Allen‑style quote
QUOTE = "I’m not afraid of death; I just don’t want to be there when it happens."

# Simple box dimensions
WIDTH = 60
BORDER_TOP    = "+" + "-" * (WIDTH-2) + "+"
BORDER_MIDDLE = "|" + " " * (WIDTH-2) + "|"

def typewriter(s, delay=0.04):
    """Print text character‑by‑character for a playful effect."""
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def center(text, width):
    """Center `text` inside a field of `width` spaces."""
    padding = (width - len(text)) // 2
    return " " * padding + text + " " * (width - padding - len(text))

def main():
    # Decorated output
    print(f"{RED}{BORDER_TOP}{RESET}")
    print(f"{BLUE}{BORDER_MIDDLE}{RESET}")

    # Wrap quote to fit the box width
    wrapped = ""
    line_len = 0
    for word in QUOTE.split():
        if line_len + len(word) > WIDTH-4:   # leave margin for '|'
            wrapped += "\n"
            line_len = 0
        if line_len:
            wrapped += " "
        wrapped += word
        line_len += len(word) + 1

    # Print each centered wrapped line inside the middle border
    for wrapped_line in wrapped.split("\n"):
        centered = center(f"{CYAN}{wrapped_line}{RESET}", WIDTH-2)
        print(f"{BLUE}|{RESET}{centered}{BLUE}|{RESET}")

    print(f"{RED}{BORDER_MIDDLE}{RESET}")

    # Add a tiny animation / signature
    typewriter(f"{GREEN} — Woody Allen{RESET}", delay=0.07)

if __name__ == "__main__":
    main()