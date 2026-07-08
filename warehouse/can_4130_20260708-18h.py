"""
Campbell's Soup Can #4130
Produced: 2026-07-08 18:45:45
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
RESET   = "\033[0m"
BOLD    = "\033[1m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
MAGENTA = "\033[35m"

def typewriter(text, delay=0.05):
    """Print text character by character with a small delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def spinner(duration=1.0):
    """Show a simple spinning animation for `duration` seconds."""
    chars = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    idx = 0
    while time.time() < end_time:
        sys.stdout.write('\r' + chars[idx % len(chars)] + ' ')
        sys.stdout.flush()
        time.sleep(0.1)
        idx += 1
    sys.stdout.write('\r')  # clear spinner line
    sys.stdout.flush()

def main():
    # Original Woody Allen‑style quote
    quote = ("I'm not afraid of the unknown; I'm just terrified "
             "that it will be surprisingly similar to my known life.")

    # Visual elements
    spinner(1.2)                           # brief animation before the quote

    # Compute box width (quote + 2 spaces padding + 2 borders)
    inner_len = len(quote) + 4
    top_bottom = CYAN + BOLD + '┌' + '─' * inner_len + '┐' + RESET
    middle     = CYAN + BOLD + '│ ' + RESET + YELLOW + quote + RESET + CYAN + BOLD + ' │' + RESET
    bottom     = CYAN + BOLD + '└' + '─' * inner_len + '┘' + RESET

    # Print the decorative box
    print(top_bottom)
    typewriter(middle, delay=0.04)   # typewriter effect for the quote
    print(bottom)

    # Optional extra flair: a tiny "signature"
    time.sleep(0.3)
    print(MAGENTA + BOLD + "\n — Woody Allen (probably)" + RESET)

if __name__ == "__main__":
    main()