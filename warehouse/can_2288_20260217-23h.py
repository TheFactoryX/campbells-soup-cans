"""
Campbell's Soup Can #2288
Produced: 2026-02-17 23:45:27
Worker: Aurora Alpha (openrouter/aurora-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

# ANSI color codes
RESET = "\033[0m"
FG_CYAN = "\033[36m"
FG_YELLOW = "\033[33m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"

# Woody‑Allen‑style quote
quote = (
    "I’m terrified of death, but I’m even more terrified of "
    "the idea that I’ll never get to finish my half‑baked novel."
)

# Box drawing characters
TL = "╔"
TR = "╗"
BL = "╚"
BR = "╝"
HL = "═"
VL = "║"

def colored(text, *codes):
    return "".join(codes) + text + RESET

def print_boxed(text):
    lines = text.splitlines()
    max_len = max(len(line) for line in lines)
    top = TL + HL * (max_len + 2) + TR
    bottom = BL + HL * (max_len + 2) + BR
    sys.stdout.write(colored(top, FG_CYAN, BG_BLUE) + "\n")
    for line in lines:
        padded = line.ljust(max_len)
        sys.stdout.write(
            colored(VL + " " + padded + " " + VL, FG_CYAN, BG_BLUE) + "\n"
        )
    sys.stdout.write(colored(bottom, FG_CYAN, BG_BLUE) + "\n")

def type_out(text, delay=0.04):
    for ch in text:
        sys.stdout.write(colored(ch, FG_YELLOW, BG_MAGENTA))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n" + RESET)

def main():
    # Clear screen (optional)
    sys.stdout.write("\033[2J\033[H")
    # Print the box
    print_boxed("")
    # Animate the quote inside the box
    # Re‑print the box with the animated text
    lines = [quote]
    max_len = max(len(line) for line in lines)
    top = TL + HL * (max_len + 2) + TR
    bottom = BL + HL * (max_len + 2) + BR
    sys.stdout.write(colored(top, FG_CYAN, BG_BLUE) + "\n")
    sys.stdout.write(colored(VL + " " + " " * max_len + " " + VL, FG_CYAN, BG_BLUE) + "\n")
    sys.stdout.write(colored(bottom, FG_CYAN, BG_BLUE) + "\n")
    # Move cursor up to the middle line
    sys.stdout.write(f"\033[{2}A")          # up 2 lines
    sys.stdout.write("\r")                  # carriage return
    sys.stdout.write(colored(VL + " ", FG_CYAN, BG_BLUE))
    # Type the quote
    type_out(quote, delay=0.03)
    # Move cursor down to close the box
    sys.stdout.write("\r")
    sys.stdout.write(colored(" " + VL, FG_CYAN, BG_BLUE) + "\n")
    sys.stdout.write(colored(bottom, FG_CYAN, BG_BLUE) + "\n")

if __name__ == "__main__":
    main()