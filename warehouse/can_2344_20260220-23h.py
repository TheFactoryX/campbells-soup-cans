"""
Campbell's Soup Can #2344
Produced: 2026-02-20 23:43:43
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import random, sys, time

# ANSI escape codes for a few basic colors
COLORS = "\033[31m\033[32m\033[33m\033[34m\033[35m\033[36m"

def random_color():
    """Return a random ANSI color code."""
    return random.choice(COLORS)

def reset_color():
    """Return code to reset terminal color."""
    return "\033[0m"

def print_border(width: int = 80):
    """Print a decorative top/bottom border."""
    border = "+" + "=" * width + "+" + "=" * width + "+"
    print(border)

def animate_text(text: str, delay: float = 0.04):
    """Print each character of `text` one‑by‑one with random colour."""
    for ch in text:
        sys.stdout.write(f"{random_color()}{ch}{reset_color}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def main():
    # Woody Allen‑style philosophical nugget (feel free to swap it!)
    QUOTE = (
        "I'm not afraid of death; I just don't want to be there when it happens.\n"
        "If the universe were truly infinite, you'd still be aware of this\n"
        "conversation… maybe."
    )

    # Top border
    print_border()
    # Print the quote inside a colourful box
    for line in QUOTE.splitlines():
        line_colour = random_color()
        line_restore = reset_color()
        sys.stdout.write(f"{line_colour}|{line:^{80}}|{line_restore}\n")
        sys.stdout.flush()
        time.sleep(0.07)               # tiny pause before the next line
    # Bottom border
    print_border()

    # Re‑type the quote with a lively animation for extra flair
    animate_text(QUOTE, delay=0.05)

    # End with a cheeky wink – ASCII art + colour
    wink = """
      ;-;
       ;)
    """
    print(f"{random_color()}WINK{reset_color()}{wink}")

if __name__ == "__main__":
    main()