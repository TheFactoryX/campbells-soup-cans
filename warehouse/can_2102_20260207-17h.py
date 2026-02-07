"""
Campbell's Soup Can #2102
Produced: 2026-02-07 17:43:37
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time

def clear():
    """Clear the terminal screen."""
    print("\033[2J\033[H", end="")

def print_header():
    """Display a colored header with the name “Woody Allen”."""
    header = "Woody Allen"
    parts = header.split()
    colors = [196, 46, 208, 214]  # bright foreground colors
    for i, part in enumerate(parts):
        color = colors[i % len(colors)]
        print(f"\033[38;5;{color}m{part}\033[0m", end=" ")
    print()

def spinner(duration=2):
    """Show a quick rotating spinner character."""
    chars = '|/-\\'
    start = time.time()
    while time.time() - start < duration:
        for c in chars:
            print(f"\033[38;5;214m{c}\033[0m", end="\r")
            time.sleep(0.1)
        time.sleep(0.05)

def quoted_box(quote, bg_color=108, inner_margin=4):
    """Print the quote inside a nicely padded colored box."""
    lines = [line.rstrip() for line in quote.split('\n')]
    max_len = max(len(line) for line in lines)
    total_width = max_len + 2 * inner_margin + 2
    border = "+" + "-" * total_width + "+"
    print(f"\033[48;5;{bg_color}m{border}\033[0m")
    for line in lines:
        centered = line.center(total_width - 2 * inner_margin)
        print(f"\033[48;5;{bg_color}m|{centered}|\033[0m")
    print(f"\033[48;5;{bg_color}m{border}\033[0m")

def blink(quote, duration=2):
    """Make the quote blink for a few seconds."""
    start = time.time()
    while time.time() - start < duration:
        print(f"\033[5m{quote}\033[25m", end="\r")
        time.sleep(0.12)
    print("\033[0m")

def main():
    clear()
    print_header()
    spinner()
    # Ensure the spinner finishes cleanly on a new line
    print("\n")
    quote = (
        "I'm not afraid of death; "
        "I just don't want to be there when it happens."
    )
    quoted_box(quote, bg_color=108)
    blink(quote)
    time.sleep(1)  # a tiny pause before exit

if __name__ == "__main__":
    main()