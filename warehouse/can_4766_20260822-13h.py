"""
Campbell's Soup Can #4766
Produced: 2026-08-22 13:00:37
Worker: LiquidAI: LFM2.5-2.6B (free) (liquid/lfm-2.5-2.6b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A Woody Allen-inspired philosophical quote displayed with vibrant colors,
ASCII art framing, and a touch of existential dread.
"""

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

TITLE = "WOODY'S EXISTENTIAL MOMENT"
QUOTE = (
    "I've spent forty years wondering why the universe "
    "keeps making sense only when I'm not looking at it. "
    "Perhaps it was always meant to be this way — "
    "a cosmic joke played exclusively on people who care "
    "too much about their place in the grand scheme."
)

def main():
    # Title banner
    print(TITLE, "=" * len(TITLE))
    print()

    # Create a decorative box using Unicode box-drawing characters
    # Top border
    top = f"{CYAN}╔══════════════════════════════════════════╗{RESET}"
    # Middle line with the colored quote
    middle = f"{BOLD}{YELLOW}{QUOTE}{RESET}"
    # Bottom border
    bottom = f"{MAGENTA}╚══════════════════════════════════════════╝{RESET}"

    print(top)
    print(middle)
    print(bottom)

if __name__ == "__main__":
    main()