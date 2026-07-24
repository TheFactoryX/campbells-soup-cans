"""
Campbell's Soup Can #4307
Produced: 2026-07-24 03:45:32
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

def main():
    # Woody Allen‑style quote
    quote = "I don't believe in an afterlife, although I am bringing a change of underwear just in case."

    # ANSI colour codes
    RED   = '\033[31m'
    GREEN = '\033[32m'
    YELLOW= '\033[33m'
    BLUE  = '\033[34m'
    MAGENTA= '\033[35m'
    CYAN  = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
    BOLD  = '\033[1m'

    # Choose colours
    BOX_COLOR = MAGENTA + BOLD
    QUOTE_COLOR = CYAN + BOLD
    FACE_COLOR = YELLOW

    # Simple Woody Allen‑ish face
    face = f"{FACE_COLOR}  (•̀ᴗ•́)و  {RESET}"
    print(face)

    # Box dimensions
    inner_width = len(quote) + 4   # two spaces padding each side
    top_border    = f"{BOX_COLOR}╔{'═'*inner_width}╗{RESET}"
    bottom_border = f"{BOX_COLOR}╚{'═'*inner_width}╝{RESET}"
    print(top_border)

    # Left border
    sys.stdout.write(f"{BOX_COLOR}║ {RESET}")
    # Typewriter effect for the quote
    for ch in quote:
        sys.stdout.write(f"{QUOTE_COLOR}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(0.07)  # typing speed
    # Right border and newline
    sys.stdout.write(f" {BOX_COLOR}║{RESET}\n")
    print(bottom_border)

if __name__ == "__main__":
    main()