"""
Campbell's Soup Can #3940
Produced: 2026-06-15 12:42:36
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def animate_print(text, delay=0.05):
    """Print text with a typewriter effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the line

def main():
    # ANSI colour codes
    CYAN   = '\033[36m'
    YELLOW = '\033[33m'
    RESET  = '\033[0m'

    # Woody Allen‑style quote (original)
    quote = (
        "“I’m not afraid of the dark; I’m afraid of what’s in it — "
        "like my ex, my student loans, and the existential dread of choosing a Netflix show.”"
    )

    # Calculate inner width (quote + two spaces padding each side)
    inner_width = len(quote) + 4
    top_border    = '╔' + '═' * inner_width + '╗'
    middle_line   = '║  ' + quote + '  ║'
    bottom_border = '╚' + '═' * inner_width + '╝'

    # Print the box with a little colour and typewriter flair
    for line, colour in [(top_border, CYAN),
                         (middle_line, YELLOW),
                         (bottom_border, CYAN)]:
        sys.stdout.write(colour)
        animate_print(line, delay=0.02)
        sys.stdout.write(RESET)
        time.sleep(0.3)  # pause between lines for dramatic effect

if __name__ == '__main__':
    main()