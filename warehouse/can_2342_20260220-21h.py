"""
Campbell's Soup Can #2342
Produced: 2026-02-20 21:42:42
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time

def animate_text(text: str, delay: float = 0.02, color: str = None, blink: bool = False) -> None:
    """
    Print a string one character at a time with a short delay.
    Optional ANSI colour (red, green, yellow, blue, magenta, cyan) and blinking.
    """
    reset = "\033[0m"
    attr = ""
    if color == "red":
        attr += "\033[31m"
    elif color == "green":
        attr += "\033[32m"
    elif color == "yellow":
        attr += "\033[33m"
    elif color == "blue":
        attr += "\033[34m"
    elif color == "magenta":
        attr += "\033[35m"
    elif color == "cyan":
        attr += "\033[36m"
    if blink:
        attr += "\033[5m"

    for ch in text:
        print(f"{attr}{ch}", end="", flush=True)
        time.sleep(delay)
    print(reset)  # reset colour/blink after the whole line

def main() -> None:
    interior_width = 58  # characters inside the box (excluding the side borders)

    # Box borders
    border_top = f"┌{'─' * interior_width}┐"
    border_bottom = f"└{'─' * interior_width}┘"

    # Empty interior rows (filled with spaces)
    top_inter = f"│{' ' * interior_width}│"
    bottom_inter = f"│{' ' * interior_width}│"

    # Display the opening frame
    print(border_top)
    time.sleep(0.07)

    # Fill the top interior row slowly
    animate_text(top_inter, delay=0.015, color=None)

    # Woody‑Allen‑style existential quote (split into lines)
    quote_lines = [
        "I'm not afraid of dying; I just don't want",
        "to be there for the encore.",
        "The universe is a cosmic punchline, and I'm",
        "the nervous kid waiting for the laugh track.",
        "In conclusion, I'm both the author and",
        "the footnote."
    ]

    # Wrap each line inside the box and animate
    quoted = "\n".join(
        f"│{line}{' ' * (interior_width - len(line))}│"
        for line in quote_lines
    )
    animate_text(quoted, delay=0.018, color="cyan", blink=True)

    # Fill the bottom interior row
    time.sleep(0.07)
    animate_text(bottom_inter, delay=0.015, color=None)

    # Closing frame
    print(border_bottom)

    # A final pause before exiting
    time.sleep(2)
    print("\n--- Existential Mini‑Film End ---\n")

if __name__ == "__main__":
    main()