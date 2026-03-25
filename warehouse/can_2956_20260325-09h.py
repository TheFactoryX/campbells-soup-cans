"""
Campbell's Soup Can #2956
Produced: 2026-03-25 09:08:54
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sysimport time

def typewriter(s, delay=0.03):
    """Print string s character by character with a small delay."""
    for ch in s:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    # ANSI color codes
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    # Woody Allen‑style quote (split into lines for box formatting)
    quote_lines = [
        "I’m not scared of death; I just don’t want to be there when it happens…",
        "...and if I did show up, I’d probably be late and forget my existential",
        "crisis while searching for my glasses."
    ]

    # Box dimensions
    BOX_WIDTH = 70                     # total width including borders
    INNER_WIDTH = BOX_WIDTH - 4        # space for text (two spaces padding each side)
    TOP_BOTTOM = CYAN + "╔" + "═" * (BOX_WIDTH - 2) + "╗" + RESET
    BOTTOM =     CYAN + "╚" + "═" * (BOX_WIDTH - 2) + "╝" + RESET

    # Print top border with a typewriter effect    typewriter(TOP_BOTTOM, delay=0.005)

    # Print empty line inside box
    typewriter(CYAN + "║" + RESET + " " * INNER_WIDTH + CYAN + "║" + RESET, delay=0.005)

    # Print each quote line, centered‑ish inside the box
    for line in quote_lines:
        # Ensure line fits; truncate if necessary (shouldn't happen with our quote)
        if len(line) > INNER_WIDTH:
            line = line[:INNER_WIDTH-3] + "..."
        padded = line.ljust(INNER_WIDTH)
        typewriter(CYAN + "║" + RESET + YELLOW + padded + RESET + CYAN + "║" + RESET, delay=0.005)

    # Print empty line inside box
    typewriter(CYAN + "║" + RESET + " " * INNER_WIDTH + CYAN + "║" + RESET, delay=0.005)

    # Print bottom border
    typewriter(BOTTOM, delay=0.005)

    # Reset terminal colors (just in case)
    print(RESET, end='')

if __name__ == "__main__":
    main()