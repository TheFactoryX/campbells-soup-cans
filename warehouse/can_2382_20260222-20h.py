"""
Campbell's Soup Can #2382
Produced: 2026-02-22 20:43:42
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def print_woody_quote():
    # ANSI escape codes for colors
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "bold": "\033[1m",
        "reset": "\033[0m"
    }

    # Woody Allen style quote
    quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."
    attribution = "- Woody Allen"

    # Create a visually interesting box with the quote
    box_width = max(len(quote), len(attribution)) + 10
    box_top_bottom = f"{colors['cyan']}+{colors['reset']}{colors['yellow']}{'=' * (box_width - 2)}{colors['reset']}{colors['cyan']}+{colors['reset']}"
    box_middle = f"{colors['cyan']}|{colors['reset']}{' ' * (box_width - 2)}{colors['cyan']}|{colors['reset']}"

    # Print the box with a typewriter effect
    print(box_top_bottom)
    time.sleep(0.5)

    for char in quote:
        print(f"{colors['cyan']}|{colors['reset']}{colors['bold']}{colors['white']}{char}{colors['reset']}", end='', flush=True)
        time.sleep(0.05)
    print(f"{colors['cyan']}|{colors['reset']}")
    time.sleep(0.5)

    print(box_middle)
    time.sleep(0.5)

    for char in attribution:
        print(f"{colors['cyan']}|{colors['reset']}{colors['bold']}{colors['green']}{char}{colors['reset']}", end='', flush=True)
        time.sleep(0.05)
    print(f"{colors['cyan']}|{colors['reset']}")
    time.sleep(0.5)

    print(box_top_bottom)

if __name__ == "__main__":
    print_woody_quote()