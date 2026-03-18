"""
Campbell's Soup Can #2825
Produced: 2026-03-18 07:17:44
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time, os

# ANSI color codes
RESET   = "\033[0m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
MAGENTA = "\033[35m"

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()

    # Woody Allen‑style quote (feel free to swap it out)
    quote = "\"Life is full of misery, loneliness, and suffering - and it's all over much too soon.\""

    # Prepare the box dimensions
    inner_width = len(quote) + 4          # two spaces on each side    top_border    = "╔" + "═" * inner_width + "╗"
    bottom_border = "╚" + "═" * inner_width + "╝"

    # Draw the top border instantly
    print(CYAN + top_border + RESET)

    # Left side of the box
    sys.stdout.write(CYAN + "║  " + RESET)
    sys.stdout.flush()

    # Type‑out the quote character by character in a cheerful yellow    for ch in quote:
        sys.stdout.write(YELLOW + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.05)  # typing speed

    # Finish the line with the right side of the box
    print(CYAN + "  ║" + RESET)

    # Draw the bottom border instantly
    print(CYAN + bottom_border + RESET)

if __name__ == "__main__":
    main()