"""
Campbell's Soup Can #4675
Produced: 2026-08-18 13:56:28
Worker: Cohere: North Mini Code (free) (cohere/north-mini-code:free)
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

# ANSI color definitions
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

def type_print(text, delay=0.04, color=""):
    """Print text character by character for an animated typing effect."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    # No newline added; caller will handle it

def draw_boxed_quote(quote, width=68):
    """Print the quote inside a colorful ASCII box with animation."""
    # Draw top border
    top = f"{CYAN}╔{'═' * (width - 2)}╗{RESET}"
    bottom = f"{CYAN}╚{'═' * (width - 2)}╝{RESET}"
    print(top)

    # Wrap the quote into lines that fit the box width
    words = quote.split()
    lines = []
    cur_line = []
    cur_len = 0
    for w in words:
        extra = 1 if cur_line else 0
        if cur_len + extra + len(w) <= width - 2:
            cur_line.append(w)
            cur_len += extra + len(w)
        else:
            lines.append(" ".join(cur_line))
            cur_line = [w]
            cur_len = len(w)
    if cur_line:
        lines.append(" ".join(cur_line))

    # Print each line with an animated typing effect
    for line in lines:
        # Print left border
        print(f"{CYAN}║{RESET}", end="")
        # Animate the line text in YELLOW
        type_print(line, color=YELLOW)
        # Print right border
        print(f"{CYAN}║{RESET}")

    # Draw bottom border
    print(bottom)

def main():
    woody_quote = "I'm not afraid of death; I just don't want to be there when it happens because I'm terrified of small spaces and coffins."
    draw_boxed_quote(woody_quote)

if __name__ == "__main__":
    main()