"""
Campbell's Soup Can #3184
Produced: 2026-04-07 21:58:17
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Woody Allen‑style quote (original)
quote = (
    "I spend so much time worrying about the afterlife "
    "that I forget to enjoy the nachos in front of me."
)

# Decorative ASCII art header
header = r"""
   _____ _          _   _             
  / ____| |        | | (_)            
 | |    | |__   ___| |_ _  ___  _ __  
 | |    | '_ \ / __| __| |/ _ \| '_ \ 
 | |____| | | | (__| |_| | (_) | | | |
  \_____|_| |_|\___|\__|_|\___/|_| |_|
"""

def slow_print(text, delay=0.005):
    """Print text character by character with a tiny delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the line

def main():
    # Clear screen (optional, works on most terminals)
    print("\033[2J\033[H", end="")

    # Print header in cyan
    print(CYAN + header + RESET)

    # Print a colorful box around the quote
    box_width = len(quote) + 4
    top_bottom = "╔" + "═" * box_width + "╗"
    sides = "║" + " " * box_width + "║"

    print(YELLOW + top_bottom + RESET)
    print(YELLOW + "║" + RESET, end="")
    slow_print(f"  {quote}  ", delay=0.0001)  # quote printed with typewriter effect
    print(YELLOW + "║" + RESET)
    print(YELLOW + top_bottom + RESET)

    # Footer with a splash of color
    footer = f"{MAGENTA}— Stay curious, stay hungry (for nachos){RESET}"
    print("\n" + footer.center(box_width + 4))

if __name__ == "__main__":
    main()