"""
Campbell's Soup Can #4074
Produced: 2026-07-02 21:33:07
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

def type_print(text: str, delay: float = 0.05) -> None:
    """Print text character by character with a short delay for a typing effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    # Ensure a newline after the whole string
    print()

def main() -> None:
    # ANSI color codes for a playful Woody Allen vibe
    CYAN = "\033[36m"       # border color
    YELLOW_BOLD = "\033[1;33m"  # quote text
    RESET = "\033[0m"       # reset all formatting

    # A philosophical quote in Woody Allen's neurotic, self‑deprecating style
    quote = "I'm not afraid of death; I just don't want my Facebook feed to go dark before I finish scrolling."

    # Build the ASCII "speech bubble" with embedded colors
    top_border = f"{CYAN}╔═════════════════════════════════════════════════════════╗{RESET}"
    middle_line = f"{CYAN}║{YELLOW_BOLD} {quote} {RESET}{CYAN}║{RESET}"
    bottom_border = f"{CYAN}╚═════════════════════════════════════════════════════════╝{RESET}"

    # Print the decorative frame with a smooth typing animation
    type_print(top_border)
    type_print(middle_line)
    type_print(bottom_border)

if __name__ == "__main__":
    main()