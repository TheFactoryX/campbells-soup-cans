"""
Campbell's Soup Can #4098
Produced: 2026-07-05 08:17:24
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
COLORS = {
    "reset": "\033[0m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bold": "\033[1m",
}

def color(text, c):
    return f"{COLORS.get(c, '')}{text}{COLORS['reset']}"

def spinner(msg, delay=0.1):
    """Simple spinner animation."""
    frames = ["|", "/", "-", "\\"]
    for _ in range(3):  # three cycles
        for frame in frames:
            sys.stdout.write(f"\r{color(msg, 'cyan')} {frame}")
            sys.stdout.flush()
            time.sleep(delay)
    sys.stdout.write("\r" + " " * (len(msg) + 2) + "\r")  # clear line
    sys.stdout.flush()

def print_boxed_quote():
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens."
    )
    # Prepare lines
    lines = [
        "",
        color("╔══════════════════════════════════════════════════════════════════════╗", "yellow"),
        color("║", "yellow") + " " * 68 + color("║", "yellow"),
        color("║", "yellow")
        + color("   " + quote.center(62) + "   ", "white", bold=True)
        + color("║", "yellow"),
        color("║", "yellow") + " " * 68 + color("║", "yellow"),
        color("╚═══════════════════════════════════════════════════════════════════════╝", "yellow"),
        "",
    ]

    # Print with a little pause for effect
    for line in lines:
        print(line)
        time.sleep(0.05)

def main():
    spinner("Loading Woody Allen wisdom", 0.08)
    print_boxed_quote()

if __name__ == "__main__":
    main()